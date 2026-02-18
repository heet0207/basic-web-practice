import streamlit as st
import hashlib
import time
import random
import pandas as pd
from datetime import datetime
import sqlite3
import io

# -------------------------------
# Utility & Classes
# -------------------------------
def sha256(data):
    return hashlib.sha256(data.encode()).hexdigest()

class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = float(amount)
        self.timestamp = time.time()
        self.hash = self.generate_hash()

    def generate_hash(self):
        data = f"{self.sender}{self.receiver}{self.amount}{self.timestamp}"
        return sha256(data)
    
    def to_dict(self):
        return {
            "Sender": self.sender,
            "Receiver": self.receiver,
            "Amount": self.amount,
            "Timestamp": self.timestamp,
            "Hash": self.hash
        }

class MerkleTree:
    def __init__(self, hashes):
        self.root = self.build_tree(hashes)

    def build_tree(self, hashes):
        if not hashes:
            return None
        if len(hashes) == 1:
            return hashes[0]

        new_level = []
        for i in range(0, len(hashes), 2):
            left = hashes[i]
            right = hashes[i] if i + 1 == len(hashes) else hashes[i + 1]
            new_level.append(sha256(left + right))

        return self.build_tree(new_level)

class ValidatorNode:
    def __init__(self, node_id):
        self.node_id = node_id

    def validate_transaction(self, transaction):
        if transaction.amount <= 0:
            return False, "Amount <= 0"
        if transaction.sender == transaction.receiver:
            return False, "Sender == Receiver"

        is_honest = random.choices([True, False], weights=[0.8, 0.2])[0]
        if is_honest:
            return True, "Valid"
        else:
            return False, "Network Error/Malicious"

# -------------------------------
# DBMS Helper Functions
# -------------------------------
def get_db_connection():
    """Create an in-memory SQLite DB seeded with current session transactions."""
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    # Create transactions table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sender TEXT NOT NULL,
            receiver TEXT NOT NULL,
            amount REAL NOT NULL,
            timestamp REAL,
            hash TEXT,
            status TEXT DEFAULT 'pending',
            block_id INTEGER DEFAULT 1
        )
    """)

    # Create blocks table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS blocks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            merkle_root TEXT,
            finalized_at REAL,
            tx_count INTEGER
        )
    """)

    # Create audit_log table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS audit_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            event_time TEXT,
            event_type TEXT,
            message TEXT
        )
    """)

    # Seed transactions from session state
    for tx in st.session_state.transactions:
        cursor.execute("""
            INSERT INTO transactions (sender, receiver, amount, timestamp, hash, status)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (tx.sender, tx.receiver, tx.amount, tx.timestamp, tx.hash,
              'finalized' if st.session_state.block_finalized else 'pending'))

    # Seed block info
    if st.session_state.block_finalized and st.session_state.original_root:
        cursor.execute("""
            INSERT INTO blocks (merkle_root, finalized_at, tx_count)
            VALUES (?, ?, ?)
        """, (st.session_state.original_root, time.time(), len(st.session_state.transactions)))

    # Seed audit log
    for item in reversed(st.session_state.history):
        cursor.execute("""
            INSERT INTO audit_log (event_time, event_type, message)
            VALUES (?, ?, ?)
        """, (item['time'], item['type'], item['message']))

    conn.commit()
    return conn

PRESET_QUERIES = {
    "-- Select a preset query --": "",
    "All Transactions": "SELECT * FROM transactions;",
    "Transactions by Amount (DESC)": "SELECT sender, receiver, amount, status FROM transactions ORDER BY amount DESC;",
    "Pending Transactions": "SELECT * FROM transactions WHERE status = 'pending';",
    "Finalized Transactions": "SELECT * FROM transactions WHERE status = 'finalized';",
    "Top Senders by Volume": "SELECT sender, COUNT(*) AS tx_count, SUM(amount) AS total_sent FROM transactions GROUP BY sender ORDER BY total_sent DESC;",
    "Top Receivers by Volume": "SELECT receiver, COUNT(*) AS tx_count, SUM(amount) AS total_received FROM transactions GROUP BY receiver ORDER BY total_received DESC;",
    "Transaction Summary Stats": "SELECT COUNT(*) AS total_tx, SUM(amount) AS total_volume, AVG(amount) AS avg_amount, MIN(amount) AS min_amount, MAX(amount) AS max_amount FROM transactions;",
    "Unique Wallets": "SELECT DISTINCT sender AS wallet FROM transactions UNION SELECT DISTINCT receiver FROM transactions ORDER BY wallet;",
    "Transactions Above Avg Amount": "SELECT * FROM transactions WHERE amount > (SELECT AVG(amount) FROM transactions);",
    "Block Info": "SELECT * FROM blocks;",
    "Full Audit Log": "SELECT * FROM audit_log ORDER BY id DESC;",
    "Error Events in Log": "SELECT * FROM audit_log WHERE event_type IN ('error', 'warning') ORDER BY id DESC;",
    "Schema: transactions": "PRAGMA table_info(transactions);",
    "Schema: blocks": "PRAGMA table_info(blocks);",
    "Schema: audit_log": "PRAGMA table_info(audit_log);",
    "List All Tables": "SELECT name FROM sqlite_master WHERE type='table';",
}

# -------------------------------
# Logging Helper
# -------------------------------
def log_event(message, type="info"):
    timestamp = datetime.now().strftime("%H:%M:%S")
    entry = {"time": timestamp, "message": message, "type": type}
    st.session_state.history.insert(0, entry)

# -------------------------------
# Streamlit App Logic
# -------------------------------
def main():
    st.set_page_config(page_title="Blockchain Validator", layout="wide")
    st.title("⛓️ Blockchain Transaction Validator")

    if 'transactions' not in st.session_state:
        st.session_state.transactions = []
    if 'original_root' not in st.session_state:
        st.session_state.original_root = None
    if 'tampered_root' not in st.session_state:
        st.session_state.tampered_root = None
    if 'block_finalized' not in st.session_state:
        st.session_state.block_finalized = False
    if 'history' not in st.session_state:
        st.session_state.history = []
    if 'query_history' not in st.session_state:
        st.session_state.query_history = []

    # ---------------------------
    # SIDEBAR
    # ---------------------------
    with st.sidebar:
        st.header("⚙️ Network Actions")
        
        if st.session_state.block_finalized:
            if st.button("😈 Simulate Cyber Attack (Tamper)", type="primary"):
                if st.session_state.transactions:
                    idx = random.randint(0, len(st.session_state.transactions) - 1)
                    tx = st.session_state.transactions[idx]
                    old_amt = tx.amount
                    tx.amount = round(random.uniform(1000, 9999), 2)
                    tx.hash = tx.generate_hash()
                    hashes = [t.hash for t in st.session_state.transactions]
                    st.session_state.tampered_root = MerkleTree(hashes).root
                    log_event(f"ATTACK: Tx {idx} modified (${old_amt} -> ${tx.amount})", "error")
                    st.rerun()
        else:
            st.caption("Finalize block to enable tampering.")

        st.markdown("---")
        st.header("📜 Audit Log")
        
        if st.button("Clear History"):
            st.session_state.history = []
            st.rerun()

        for item in st.session_state.history:
            msg = f"**{item['time']}**\n{item['message']}"
            if item['type'] == 'success':
                st.success(msg)
            elif item['type'] == 'error':
                st.error(msg)
            elif item['type'] == 'warning':
                st.warning(msg)
            else:
                st.info(msg)

    # Tabs
    tab1, tab2, tab3 = st.tabs(["🌳 Merkle Tree & Tampering", "🤝 Consensus Protocol", "🗄️ DBMS Query"])

    # ---------------------------
    # TAB 1: Merkle Tree
    # ---------------------------
    with tab1:
        st.header("Merkle Tree Integrity Check")
        st.info("Step 1: Add transactions. Step 2: Finalize Block. Step 3: Use the Sidebar 'Simulate Attack' button or manually tamper below.")

        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.subheader("Add Transaction")
            with st.form("tx_form"):
                sender = st.text_input("Sender")
                receiver = st.text_input("Receiver")
                amount = st.number_input("Amount", min_value=0.01, step=1.0)
                submitted = st.form_submit_button("Add Transaction")
                
                if submitted:
                    if sender and receiver:
                        new_tx = Transaction(sender, receiver, amount)
                        st.session_state.transactions.append(new_tx)
                        st.session_state.block_finalized = False 
                        st.session_state.original_root = None
                        st.session_state.tampered_root = None
                        log_event(f"Tx Added: {sender} -> {receiver} (${amount})", "info")
                        st.success("Transaction Added")
                        st.rerun()
                    else:
                        st.error("Please fill sender and receiver")

        with col2:
            st.subheader("Current Block Data")
            if st.session_state.transactions:
                df = pd.DataFrame([t.to_dict() for t in st.session_state.transactions])
                st.dataframe(df[["Sender", "Receiver", "Amount", "Hash"]], use_container_width=True)
            else:
                st.warning("No transactions in block yet.")

        st.divider()

        if st.session_state.transactions:
            if not st.session_state.block_finalized:
                if st.button("🔒 Finalize Block & Generate Merkle Root"):
                    hashes = [tx.hash for tx in st.session_state.transactions]
                    tree = MerkleTree(hashes)
                    st.session_state.original_root = tree.root
                    st.session_state.block_finalized = True
                    log_event(f"Block Finalized. Root: {tree.root[:8]}...", "success")
                    st.rerun()
            else:
                st.success(f"✅ **Original Merkle Root:** `{st.session_state.original_root}`")

        if st.session_state.block_finalized and st.session_state.transactions:
            st.divider()
            current_hashes = [tx.hash for tx in st.session_state.transactions]
            current_root = MerkleTree(current_hashes).root
            
            if current_root != st.session_state.original_root:
                st.error("🚨 **INTEGRITY WARNING: TAMPERING DETECTED!**")
                st.markdown(f"""
                The Merkle Root of the current data does not match the finalized root.
                
                | Type | Merkle Root Hash |
                | :--- | :--- |
                | **Original** | `{st.session_state.original_root}` |
                | **Current** | `{current_root}` |
                """)
                if not st.session_state.tampered_root: 
                     st.session_state.tampered_root = current_root
                     log_event("🚨 TAMPERING DETECTED! Root Mismatch.", "error")
            else:
                st.info("✅ Data is intact. No tampering detected.")

            with st.expander("Manual Tampering (Advanced)"):
                t_col1, t_col2 = st.columns(2)
                with t_col1:
                    tx_options = {f"Tx {i}": i for i, tx in enumerate(st.session_state.transactions)}
                    sel_idx = st.selectbox("Select Tx", list(tx_options.keys()))
                    sel_val = tx_options[sel_idx]
                    new_val = st.number_input("New Amount", value=st.session_state.transactions[sel_val].amount)
                    if st.button("Apply Manual Change"):
                        st.session_state.transactions[sel_val].amount = new_val
                        st.session_state.transactions[sel_val].hash = st.session_state.transactions[sel_val].generate_hash()
                        log_event(f"Manual Edit on Tx {sel_val}", "warning")
                        st.rerun()

    # ---------------------------
    # TAB 2: Consensus
    # ---------------------------
    with tab2:
        st.header("Distributed Consensus")
        
        with st.form("consensus_form"):
            c_sender = st.text_input("Sender", "Alice")
            c_receiver = st.text_input("Receiver", "Bob")
            c_amount = st.number_input("Amount", value=50.0)
            validate_btn = st.form_submit_button("Broadcast to Network")

        if validate_btn:
            tx = Transaction(c_sender, c_receiver, c_amount)
            log_event(f"Broadcast: {c_sender}->{c_receiver}", "info")
            st.write("📡 Broadcasting to validators...")
            time.sleep(1)

            validators = [ValidatorNode(i) for i in range(1, 6)]
            approvals = 0

            cols = st.columns(5)
            for i, validator in enumerate(validators):
                is_valid, reason = validator.validate_transaction(tx)
                if is_valid:
                    approvals += 1
                with cols[i]:
                    st.markdown(f"**Node {validator.node_id}**")
                    if is_valid:
                        st.success("✅ APPROVED")
                    else:
                        st.error("❌ REJECTED")

            threshold = len(validators) // 2
            if approvals > threshold:
                st.success(f"✅ **APPROVED ({approvals}/5)**")
            else:
                st.error(f"❌ **REJECTED ({approvals}/5)**")

    # ---------------------------
    # TAB 3: DBMS Query
    # ---------------------------
    with tab3:
        st.header("🗄️ DBMS Query Interface")
        st.markdown("""
        Interact with the blockchain data using **SQL queries** powered by an in-memory **SQLite** database.
        The database is automatically seeded with the current session's transactions, blocks, and audit logs.
        """)

        # Schema Overview
        with st.expander("📋 Database Schema Reference", expanded=False):
            schema_col1, schema_col2, schema_col3 = st.columns(3)
            with schema_col1:
                st.markdown("""
                **`transactions`**
                | Column | Type |
                |---|---|
                | id | INTEGER PK |
                | sender | TEXT |
                | receiver | TEXT |
                | amount | REAL |
                | timestamp | REAL |
                | hash | TEXT |
                | status | TEXT |
                | block_id | INTEGER |
                """)
            with schema_col2:
                st.markdown("""
                **`blocks`**
                | Column | Type |
                |---|---|
                | id | INTEGER PK |
                | merkle_root | TEXT |
                | finalized_at | REAL |
                | tx_count | INTEGER |
                """)
            with schema_col3:
                st.markdown("""
                **`audit_log`**
                | Column | Type |
                |---|---|
                | id | INTEGER PK |
                | event_time | TEXT |
                | event_type | TEXT |
                | message | TEXT |
                """)

        st.divider()

        # Preset Query Selector
        preset_col, _ = st.columns([2, 1])
        with preset_col:
            selected_preset = st.selectbox("⚡ Preset Queries", list(PRESET_QUERIES.keys()))

        # Query Editor
        default_query = PRESET_QUERIES.get(selected_preset, "") or "SELECT * FROM transactions;"
        query = st.text_area(
            "✏️ SQL Query Editor",
            value=default_query,
            height=120,
            placeholder="Enter your SQL query here...",
            help="Supports SELECT, and read operations. Write ops (INSERT/UPDATE/DELETE) are applied to the in-memory DB only and reset on each run."
        )

        exec_col, clear_col, export_col = st.columns([1, 1, 1])

        with exec_col:
            run_query = st.button("▶️ Run Query", type="primary", use_container_width=True)
        with clear_col:
            if st.button("🗑️ Clear History", use_container_width=True):
                st.session_state.query_history = []
                st.rerun()

        # Execute Query
        if run_query and query.strip():
            conn = get_db_connection()
            try:
                start_time = time.time()
                result_df = pd.read_sql_query(query, conn)
                elapsed = round((time.time() - start_time) * 1000, 2)

                # Store in query history
                st.session_state.query_history.insert(0, {
                    "query": query.strip(),
                    "rows": len(result_df),
                    "cols": len(result_df.columns),
                    "time_ms": elapsed,
                    "success": True,
                    "result": result_df,
                    "error": None
                })

                log_event(f"SQL Query executed: {len(result_df)} rows returned", "success")

            except Exception as e:
                elapsed = round((time.time() - start_time) * 1000, 2)
                st.session_state.query_history.insert(0, {
                    "query": query.strip(),
                    "rows": 0,
                    "cols": 0,
                    "time_ms": elapsed,
                    "success": False,
                    "result": None,
                    "error": str(e)
                })
                log_event(f"SQL Error: {str(e)}", "error")
            finally:
                conn.close()

            st.rerun()

        # Display Most Recent Result
        if st.session_state.query_history:
            latest = st.session_state.query_history[0]
            st.divider()
            st.subheader("📊 Query Result")

            meta_col1, meta_col2, meta_col3, meta_col4 = st.columns(4)
            with meta_col1:
                st.metric("Status", "✅ Success" if latest["success"] else "❌ Error")
            with meta_col2:
                st.metric("Rows Returned", latest["rows"])
            with meta_col3:
                st.metric("Columns", latest["cols"])
            with meta_col4:
                st.metric("Execution Time", f"{latest['time_ms']} ms")

            if latest["success"] and latest["result"] is not None:
                result_df = latest["result"]
                st.dataframe(result_df, use_container_width=True, height=300)

                # Export options
                with export_col:
                    csv_data = result_df.to_csv(index=False).encode("utf-8")
                    st.download_button(
                        label="⬇️ Export CSV",
                        data=csv_data,
                        file_name=f"query_result_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                        mime="text/csv",
                        use_container_width=True
                    )

                # Quick chart if numeric columns exist
                numeric_cols = result_df.select_dtypes(include='number').columns.tolist()
                non_numeric_cols = result_df.select_dtypes(exclude='number').columns.tolist()

                if len(numeric_cols) >= 1 and len(result_df) > 1:
                    with st.expander("📈 Quick Visualization", expanded=False):
                        chart_type = st.radio("Chart type", ["Bar", "Line", "Area"], horizontal=True)
                        y_col = st.selectbox("Y-axis (numeric)", numeric_cols)
                        x_col = st.selectbox("X-axis (label)", non_numeric_cols if non_numeric_cols else numeric_cols)

                        chart_df = result_df[[x_col, y_col]].set_index(x_col)
                        if chart_type == "Bar":
                            st.bar_chart(chart_df)
                        elif chart_type == "Line":
                            st.line_chart(chart_df)
                        else:
                            st.area_chart(chart_df)

            elif not latest["success"]:
                st.error(f"**SQL Error:** {latest['error']}")
                st.markdown("**💡 Tips:**")
                st.markdown("- Check table names: `transactions`, `blocks`, `audit_log`")
                st.markdown("- Use `SELECT name FROM sqlite_master WHERE type='table';` to list all tables")
                st.markdown("- Use `PRAGMA table_info(table_name);` to inspect schema")

            # Query History
            if len(st.session_state.query_history) > 1:
                st.divider()
                st.subheader("🕐 Query History")
                for i, hist in enumerate(st.session_state.query_history[1:], 1):
                    status_icon = "✅" if hist["success"] else "❌"
                    with st.expander(f"{status_icon} [{hist['time_ms']}ms | {hist['rows']} rows] {hist['query'][:80]}{'...' if len(hist['query']) > 80 else ''}", expanded=False):
                        st.code(hist["query"], language="sql")
                        if hist["success"] and hist["result"] is not None:
                            st.dataframe(hist["result"], use_container_width=True)
                        elif hist["error"]:
                            st.error(hist["error"])

        else:
            # Empty state
            st.info("👆 Select a preset query or write your own SQL above, then click **Run Query** to see results.")
            st.markdown("""
            **Getting Started:**
            - Add transactions in the **Merkle Tree** tab first
            - Then query them here using SQL
            - Try: `SELECT * FROM transactions;`
            """)


if __name__ == "__main__":
    main()