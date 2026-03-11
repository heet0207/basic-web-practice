import streamlit as st
import hashlib
import time
import random
import pandas as pd
from datetime import datetime
import sqlite3


import mysql.connector

# Step 1: Connect WITHOUT specifying a database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)
cursor = conn.cursor()

# Step 2: Create the database if it doesn't exist
cursor.execute("CREATE DATABASE IF NOT EXISTS blockchain_db")
cursor.execute("USE blockchain_db")

# Step 3: Create all tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sender VARCHAR(100) NOT NULL,
    receiver VARCHAR(100) NOT NULL,
    amount DECIMAL(18,4) NOT NULL,
    tx_hash VARCHAR(64) NOT NULL,
    status ENUM('pending','finalized','tampered') DEFAULT 'pending',
    block_id INT DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS blocks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    merkle_root VARCHAR(64),
    tx_count INT DEFAULT 0,
    finalized_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS consensus_rounds (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tx_hash VARCHAR(64),
    sender VARCHAR(100),
    receiver VARCHAR(100),
    amount DECIMAL(18,4),
    total_nodes INT DEFAULT 5,
    approvals INT DEFAULT 0,
    rejections INT DEFAULT 0,
    threshold INT DEFAULT 2,
    final_verdict ENUM('APPROVED','REJECTED') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS consensus_votes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    round_id INT NOT NULL,
    node_id INT NOT NULL,
    vote ENUM('APPROVED','REJECTED') NOT NULL,
    reason VARCHAR(100) DEFAULT 'Valid',
    voted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (round_id) REFERENCES consensus_rounds(id) ON DELETE CASCADE
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS audit_log (
    id INT AUTO_INCREMENT PRIMARY KEY,
    event_type ENUM('info','success','warning','error') DEFAULT 'info',
    message TEXT,
    logged_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()
cursor.close()
conn.close()
print("✅ Database and tables created successfully!")
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
        self.levels = []
        self.root = self.build_tree(hashes)

    def build_tree(self, hashes):
        if not hashes:
            return None
        self.levels.append(list(hashes))
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
# DBMS Helper
# -------------------------------
def get_db_connection():
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

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
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS blocks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            merkle_root TEXT,
            finalized_at REAL,
            tx_count INTEGER
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS audit_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            event_time TEXT,
            event_type TEXT,
            message TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS consensus_votes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tx_hash TEXT,
            sender TEXT,
            receiver TEXT,
            amount REAL,
            node_id INTEGER,
            vote TEXT,
            reason TEXT,
            voted_at REAL,
            round_id INTEGER
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS consensus_rounds (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tx_hash TEXT,
            sender TEXT,
            receiver TEXT,
            amount REAL,
            total_nodes INTEGER,
            approvals INTEGER,
            rejections INTEGER,
            final_verdict TEXT,
            threshold INTEGER,
            created_at REAL
        )
    """)

    for tx in st.session_state.transactions:
        cursor.execute("""
            INSERT INTO transactions (sender, receiver, amount, timestamp, hash, status)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (tx.sender, tx.receiver, tx.amount, tx.timestamp, tx.hash,
              'finalized' if st.session_state.block_finalized else 'pending'))

    if st.session_state.block_finalized and st.session_state.original_root:
        cursor.execute("""
            INSERT INTO blocks (merkle_root, finalized_at, tx_count)
            VALUES (?, ?, ?)
        """, (st.session_state.original_root, time.time(), len(st.session_state.transactions)))

    for item in reversed(st.session_state.history):
        cursor.execute("""
            INSERT INTO audit_log (event_time, event_type, message)
            VALUES (?, ?, ?)
        """, (item['time'], item['type'], item['message']))

    for round_data in st.session_state.consensus_rounds:
        cursor.execute("""
            INSERT INTO consensus_rounds (tx_hash, sender, receiver, amount, total_nodes, approvals, rejections, final_verdict, threshold, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (round_data['tx_hash'], round_data['sender'], round_data['receiver'],
              round_data['amount'], round_data['total_nodes'], round_data['approvals'],
              round_data['rejections'], round_data['final_verdict'], round_data['threshold'],
              round_data['created_at']))
        round_id = cursor.lastrowid
        for vote in round_data['votes']:
            cursor.execute("""
                INSERT INTO consensus_votes (tx_hash, sender, receiver, amount, node_id, vote, reason, voted_at, round_id)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (round_data['tx_hash'], round_data['sender'], round_data['receiver'],
                  round_data['amount'], vote['node_id'], vote['vote'], vote['reason'],
                  round_data['created_at'], round_id))

    conn.commit()
    return conn

# -------------------------------
# Preset Queries
# -------------------------------
PRESET_QUERIES = {
    "-- Select a preset query --": "",
    # Transactions
    "All Transactions": "SELECT * FROM transactions;",
    "Transactions by Amount (DESC)": "SELECT sender, receiver, amount, status FROM transactions ORDER BY amount DESC;",
    "Pending Transactions": "SELECT * FROM transactions WHERE status = 'pending';",
    "Finalized Transactions": "SELECT * FROM transactions WHERE status = 'finalized';",
    "Top Senders by Volume": "SELECT sender, COUNT(*) AS tx_count, SUM(amount) AS total_sent FROM transactions GROUP BY sender ORDER BY total_sent DESC;",
    "Top Receivers by Volume": "SELECT receiver, COUNT(*) AS tx_count, SUM(amount) AS total_received FROM transactions GROUP BY receiver ORDER BY total_received DESC;",
    "Transaction Summary Stats": "SELECT COUNT(*) AS total_tx, SUM(amount) AS total_volume, AVG(amount) AS avg_amount, MIN(amount) AS min_amount, MAX(amount) AS max_amount FROM transactions;",
    "Unique Wallets": "SELECT DISTINCT sender AS wallet FROM transactions UNION SELECT DISTINCT receiver FROM transactions ORDER BY wallet;",
    "Transactions Above Avg Amount": "SELECT * FROM transactions WHERE amount > (SELECT AVG(amount) FROM transactions);",
    # Consensus
    "All Consensus Rounds": "SELECT id, sender, receiver, amount, approvals, rejections, final_verdict FROM consensus_rounds ORDER BY id DESC;",
    "All Consensus Votes": "SELECT round_id, node_id, vote, reason, sender, receiver, amount FROM consensus_votes ORDER BY round_id DESC, node_id;",
    "Approval Rate per Round": "SELECT id AS round_id, sender, receiver, amount, approvals, total_nodes, ROUND(CAST(approvals AS FLOAT)/total_nodes*100, 1) AS approval_pct, final_verdict FROM consensus_rounds;",
    "Node Approval Stats": "SELECT node_id, COUNT(*) AS total_votes, SUM(CASE WHEN vote='APPROVED' THEN 1 ELSE 0 END) AS approvals, SUM(CASE WHEN vote='REJECTED' THEN 1 ELSE 0 END) AS rejections FROM consensus_votes GROUP BY node_id ORDER BY node_id;",
    "Rejected Consensus Rounds": "SELECT * FROM consensus_rounds WHERE final_verdict = 'REJECTED';",
    "Approved Consensus Rounds": "SELECT * FROM consensus_rounds WHERE final_verdict = 'APPROVED';",
    "Votes for Round 1": "SELECT * FROM consensus_votes WHERE round_id = 1;",
    "Consensus + Transaction JOIN": """SELECT cr.id AS round_id, cr.sender, cr.receiver, cr.amount,
  cr.approvals, cr.rejections, cr.final_verdict,
  t.status AS block_status, t.hash
FROM consensus_rounds cr
LEFT JOIN transactions t
  ON cr.sender = t.sender AND cr.receiver = t.receiver AND cr.amount = t.amount
ORDER BY cr.id DESC;""",
    "Malicious Node Activity": "SELECT node_id, COUNT(*) AS rejections FROM consensus_votes WHERE vote='REJECTED' GROUP BY node_id ORDER BY rejections DESC;",
    # Blocks & Logs
    "Block Info": "SELECT * FROM blocks;",
    "Full Audit Log": "SELECT * FROM audit_log ORDER BY id DESC;",
    "Error Events in Log": "SELECT * FROM audit_log WHERE event_type IN ('error', 'warning') ORDER BY id DESC;",
    # Schema
    "Schema: transactions": "PRAGMA table_info(transactions);",
    "Schema: consensus_rounds": "PRAGMA table_info(consensus_rounds);",
    "Schema: consensus_votes": "PRAGMA table_info(consensus_votes);",
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
# Consensus Tree Renderer
# -------------------------------
def render_consensus_tree(round_data):
    votes = round_data['votes']
    approvals = round_data['approvals']
    rejections = round_data['rejections']
    verdict = round_data['final_verdict']
    verdict_color = "#22c55e" if verdict == "APPROVED" else "#ef4444"
    verdict_icon = "✅" if verdict == "APPROVED" else "❌"
    tx_short = round_data['tx_hash'][:12] + "..."

    node_html = ""
    for v in votes:
        color = "#22c55e" if v['vote'] == "APPROVED" else "#ef4444"
        icon = "✅" if v['vote'] == "APPROVED" else "❌"
        node_html += f"""
        <div style="display:flex; flex-direction:column; align-items:center; margin: 0 6px;">
            <div style="width:2px; height:30px; background:#555;"></div>
            <div style="background:{color}22; border:2px solid {color}; border-radius:10px;
                        padding:8px 10px; text-align:center; min-width:90px; font-size:12px;">
                <div style="font-weight:700; color:{color};">{icon} Node {v['node_id']}</div>
                <div style="color:#aaa; font-size:10px; margin-top:2px;">{v['vote']}</div>
                <div style="color:#888; font-size:10px;">{v['reason']}</div>
            </div>
        </div>"""

    width = max(len(votes) * 110, 120)

    return f"""
    <div style="background:#0f1117; border:1px solid #2d2d2d; border-radius:14px;
                padding:20px 16px; margin-bottom:12px; font-family: 'Courier New', monospace;">
        <div style="display:flex; justify-content:center; margin-bottom:6px;">
            <div style="background:#1e3a5f; border:2px solid #3b82f6; border-radius:12px;
                        padding:10px 20px; text-align:center;">
                <div style="color:#60a5fa; font-weight:700; font-size:13px;">📦 Transaction</div>
                <div style="color:#94a3b8; font-size:11px; margin-top:3px;">
                    {round_data['sender']} → {round_data['receiver']}
                </div>
                <div style="color:#f59e0b; font-size:12px; font-weight:600;">${round_data['amount']:.2f}</div>
                <div style="color:#475569; font-size:10px; margin-top:2px;">hash: {tx_short}</div>
            </div>
        </div>
        <div style="display:flex; justify-content:center;">
            <div style="width:2px; height:20px; background:#3b82f6;"></div>
        </div>
        <div style="display:flex; justify-content:center; margin-bottom:6px;">
            <div style="background:#1a1a2e; border:2px solid #7c3aed; border-radius:10px;
                        padding:7px 18px; text-align:center;">
                <div style="color:#a78bfa; font-weight:600; font-size:12px;">📡 Broadcast to Network</div>
                <div style="color:#6b7280; font-size:10px;">{len(votes)} Validator Nodes</div>
            </div>
        </div>
        <div style="display:flex; justify-content:center;">
            <div style="width:{width}px; height:2px; background:#555;"></div>
        </div>
        <div style="display:flex; justify-content:center; align-items:flex-start; margin-bottom:6px;">
            {node_html}
        </div>
        <div style="display:flex; justify-content:center;">
            <div style="width:{width}px; height:2px; background:#555;"></div>
        </div>
        <div style="display:flex; justify-content:center;">
            <div style="width:2px; height:20px; background:{verdict_color};"></div>
        </div>
        <div style="display:flex; justify-content:center;">
            <div style="background:{verdict_color}22; border:2px solid {verdict_color}; border-radius:12px;
                        padding:10px 24px; text-align:center;">
                <div style="color:{verdict_color}; font-weight:700; font-size:14px;">
                    {verdict_icon} Final Verdict: {verdict}
                </div>
                <div style="color:#94a3b8; font-size:11px; margin-top:3px;">
                    {approvals} Approved / {rejections} Rejected &nbsp;|&nbsp;
                    Threshold: &gt;{round_data['threshold']}/{round_data['total_nodes']}
                </div>
            </div>
        </div>
    </div>
    """

# -------------------------------
# Main App
# -------------------------------
def main():
    st.set_page_config(page_title="Blockchain Validator", layout="wide")
    st.title("⛓️ Blockchain Transaction Validator")

    defaults = {
        'transactions': [],
        'original_root': None,
        'tampered_root': None,
        'block_finalized': False,
        'history': [],
        'query_history': [],
        'consensus_rounds': [],
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

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

    tab1, tab2, tab3, tab4 = st.tabs([
        "🌳 Merkle Tree & Tampering",
        "🤝 Consensus Protocol",
        "🔗 Consensus Tree & Transactions",
        "🗄️ DBMS Query"
    ])

    # ---------------------------
    # TAB 1: Merkle Tree
    # ---------------------------
    with tab1:
        st.header("Merkle Tree Integrity Check")
        st.info("Step 1: Add transactions. Step 2: Finalize Block. Step 3: Use the Sidebar 'Simulate Attack' or tamper below.")

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
                tx_options = {f"Tx {i}": i for i in range(len(st.session_state.transactions))}
                sel_idx = st.selectbox("Select Tx", list(tx_options.keys()))
                sel_val = tx_options[sel_idx]
                new_val = st.number_input("New Amount", value=st.session_state.transactions[sel_val].amount)
                if st.button("Apply Manual Change"):
                    st.session_state.transactions[sel_val].amount = new_val
                    st.session_state.transactions[sel_val].hash = st.session_state.transactions[sel_val].generate_hash()
                    log_event(f"Manual Edit on Tx {sel_val}", "warning")
                    st.rerun()

    # ---------------------------
    # TAB 2: Consensus Protocol
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
            log_event(f"Broadcast: {c_sender}->{c_receiver} ${c_amount}", "info")
            st.write("📡 Broadcasting to validators...")
            time.sleep(1)

            validators = [ValidatorNode(i) for i in range(1, 6)]
            approvals = 0
            vote_records = []

            cols = st.columns(5)
            for i, validator in enumerate(validators):
                is_valid, reason = validator.validate_transaction(tx)
                if is_valid:
                    approvals += 1
                vote_records.append({
                    "node_id": validator.node_id,
                    "vote": "APPROVED" if is_valid else "REJECTED",
                    "reason": reason
                })
                with cols[i]:
                    st.markdown(f"**Node {validator.node_id}**")
                    if is_valid:
                        st.success("✅ APPROVED")
                    else:
                        st.error("❌ REJECTED")

            threshold = len(validators) // 2
            verdict = "APPROVED" if approvals > threshold else "REJECTED"

            if approvals > threshold:
                st.success(f"✅ **APPROVED ({approvals}/5)**")
            else:
                st.error(f"❌ **REJECTED ({approvals}/5)**")

            round_data = {
                "tx_hash": tx.hash,
                "sender": c_sender,
                "receiver": c_receiver,
                "amount": c_amount,
                "total_nodes": len(validators),
                "approvals": approvals,
                "rejections": len(validators) - approvals,
                "final_verdict": verdict,
                "threshold": threshold,
                "created_at": time.time(),
                "votes": vote_records
            }
            st.session_state.consensus_rounds.insert(0, round_data)
            log_event(
                f"Consensus {verdict}: {c_sender}->{c_receiver} ${c_amount} ({approvals}/{len(validators)})",
                "success" if verdict == "APPROVED" else "warning"
            )
            st.info("✅ Round saved! View the decision tree in the **Consensus Tree & Transactions** tab.")

    # ---------------------------
    # TAB 3: Consensus Tree & Transactions
    # ---------------------------
    with tab3:
        st.header("🔗 Consensus Tree & Transaction View")

        if not st.session_state.consensus_rounds:
            st.info("No consensus rounds yet. Go to **Consensus Protocol**, broadcast a transaction, then return here.")
        else:
            total_rounds = len(st.session_state.consensus_rounds)
            approved_count = sum(1 for r in st.session_state.consensus_rounds if r['final_verdict'] == 'APPROVED')
            rejected_count = total_rounds - approved_count
            total_volume = sum(r['amount'] for r in st.session_state.consensus_rounds if r['final_verdict'] == 'APPROVED')

            m1, m2, m3, m4 = st.columns(4)
            m1.metric("Total Rounds", total_rounds)
            m2.metric("✅ Approved", approved_count)
            m3.metric("❌ Rejected", rejected_count)
            m4.metric("💰 Approved Volume", f"${total_volume:,.2f}")

            st.divider()

            fc1, fc2 = st.columns(2)
            with fc1:
                verdict_filter = st.selectbox("Filter by Verdict", ["All", "APPROVED", "REJECTED"])
            with fc2:
                sort_order = st.selectbox("Sort by", ["Newest First", "Oldest First", "Amount (High→Low)", "Amount (Low→High)"])

            rounds = list(st.session_state.consensus_rounds)
            if verdict_filter != "All":
                rounds = [r for r in rounds if r['final_verdict'] == verdict_filter]
            if sort_order == "Oldest First":
                rounds = list(reversed(rounds))
            elif sort_order == "Amount (High→Low)":
                rounds = sorted(rounds, key=lambda r: r['amount'], reverse=True)
            elif sort_order == "Amount (Low→High)":
                rounds = sorted(rounds, key=lambda r: r['amount'])

            # Transaction Records Table
            st.subheader(f"📊 Transaction Records ({len(rounds)} shown)")
            if rounds:
                tx_df = pd.DataFrame([{
                    "Round #": i + 1,
                    "Sender": r['sender'],
                    "Receiver": r['receiver'],
                    "Amount ($)": r['amount'],
                    "Approvals": r['approvals'],
                    "Rejections": r['rejections'],
                    "Verdict": r['final_verdict'],
                    "TX Hash": r['tx_hash'][:16] + "...",
                } for i, r in enumerate(rounds)])
                st.dataframe(tx_df, use_container_width=True, hide_index=True)

            st.divider()

            # Consensus Trees
            st.subheader("🌲 Consensus Decision Trees")
            st.caption("Visual flow from transaction broadcast → validator votes → final consensus verdict.")

            if rounds:
                round_labels = [
                    f"Round {i+1}: {r['sender']}→{r['receiver']} ${r['amount']:.2f} [{r['final_verdict']}]"
                    for i, r in enumerate(rounds)
                ]

                view_mode = st.radio("View Mode", ["Selected Round", "All Rounds"], horizontal=True)

                if view_mode == "Selected Round":
                    selected_label = st.selectbox("Select Round", round_labels)
                    selected_idx = round_labels.index(selected_label)
                    st.markdown(render_consensus_tree(rounds[selected_idx]), unsafe_allow_html=True)

                    st.markdown("**🗳️ Vote Breakdown**")
                    votes_df = pd.DataFrame(rounds[selected_idx]['votes'])
                    votes_df.columns = ["Node ID", "Vote", "Reason"]
                    votes_df["Node ID"] = votes_df["Node ID"].apply(lambda x: f"Node {x}")
                    st.dataframe(votes_df, use_container_width=True, hide_index=True)

                else:
                    for i, r in enumerate(rounds):
                        label = f"Round {i+1}: {r['sender']} → {r['receiver']} | ${r['amount']:.2f} | {r['final_verdict']}"
                        with st.expander(label, expanded=(i == 0)):
                            st.markdown(render_consensus_tree(r), unsafe_allow_html=True)
                            votes_df = pd.DataFrame(r['votes'])
                            votes_df.columns = ["Node ID", "Vote", "Reason"]
                            votes_df["Node ID"] = votes_df["Node ID"].apply(lambda x: f"Node {x}")
                            st.dataframe(votes_df, use_container_width=True, hide_index=True)

            # Node Performance
            st.divider()
            st.subheader("🤖 Validator Node Performance")
            if rounds:
                node_stats = {}
                for r in rounds:
                    for v in r['votes']:
                        nid = f"Node {v['node_id']}"
                        node_stats.setdefault(nid, {"Approved": 0, "Rejected": 0})
                        if v['vote'] == "APPROVED":
                            node_stats[nid]["Approved"] += 1
                        else:
                            node_stats[nid]["Rejected"] += 1

                node_df = pd.DataFrame([
                    {
                        "Node": n,
                        "Approved": s["Approved"],
                        "Rejected": s["Rejected"],
                        "Total": s["Approved"] + s["Rejected"],
                        "Approval Rate": f"{s['Approved']/(s['Approved']+s['Rejected'])*100:.1f}%"
                    }
                    for n, s in node_stats.items()
                ])
                st.dataframe(node_df, use_container_width=True, hide_index=True)
                st.bar_chart(node_df.set_index("Node")[["Approved", "Rejected"]])

    # ---------------------------
    # TAB 4: DBMS Query
    # ---------------------------
    with tab4:
        st.header("🗄️ DBMS Query Interface")
        st.markdown("Query blockchain and consensus data using **SQL** (in-memory SQLite, seeded from session).")

        with st.expander("📋 Database Schema Reference", expanded=False):
            sc1, sc2, sc3, sc4, sc5 = st.columns(5)
            with sc1:
                st.markdown("""**`transactions`**
| Column | Type |
|---|---|
| id | INT PK |
| sender | TEXT |
| receiver | TEXT |
| amount | REAL |
| timestamp | REAL |
| hash | TEXT |
| status | TEXT |
| block_id | INT |""")
            with sc2:
                st.markdown("""**`blocks`**
| Column | Type |
|---|---|
| id | INT PK |
| merkle_root | TEXT |
| finalized_at | REAL |
| tx_count | INT |""")
            with sc3:
                st.markdown("""**`consensus_rounds`**
| Column | Type |
|---|---|
| id | INT PK |
| tx_hash | TEXT |
| sender | TEXT |
| receiver | TEXT |
| amount | REAL |
| total_nodes | INT |
| approvals | INT |
| rejections | INT |
| final_verdict | TEXT |
| threshold | INT |
| created_at | REAL |""")
            with sc4:
                st.markdown("""**`consensus_votes`**
| Column | Type |
|---|---|
| id | INT PK |
| tx_hash | TEXT |
| sender | TEXT |
| receiver | TEXT |
| amount | REAL |
| node_id | INT |
| vote | TEXT |
| reason | TEXT |
| voted_at | REAL |
| round_id | INT |""")
            with sc5:
                st.markdown("""**`audit_log`**
| Column | Type |
|---|---|
| id | INT PK |
| event_time | TEXT |
| event_type | TEXT |
| message | TEXT |""")

        st.divider()

        preset_col, _ = st.columns([2, 1])
        with preset_col:
            selected_preset = st.selectbox("⚡ Preset Queries", list(PRESET_QUERIES.keys()))

        default_query = PRESET_QUERIES.get(selected_preset, "") or "SELECT * FROM transactions;"
        query = st.text_area("✏️ SQL Query Editor", value=default_query, height=130,
                             placeholder="Enter your SQL query here...")

        exec_col, clear_col, export_col = st.columns([1, 1, 1])
        with exec_col:
            run_query = st.button("▶️ Run Query", type="primary", use_container_width=True)
        with clear_col:
            if st.button("🗑️ Clear History", use_container_width=True):
                st.session_state.query_history = []
                st.rerun()

        if run_query and query.strip():
            conn = get_db_connection()
            start_time = time.time()
            try:
                result_df = pd.read_sql_query(query, conn)
                elapsed = round((time.time() - start_time) * 1000, 2)
                st.session_state.query_history.insert(0, {
                    "query": query.strip(), "rows": len(result_df),
                    "cols": len(result_df.columns), "time_ms": elapsed,
                    "success": True, "result": result_df, "error": None
                })
                log_event(f"SQL Query: {len(result_df)} rows returned", "success")
            except Exception as e:
                elapsed = round((time.time() - start_time) * 1000, 2)
                st.session_state.query_history.insert(0, {
                    "query": query.strip(), "rows": 0, "cols": 0, "time_ms": elapsed,
                    "success": False, "result": None, "error": str(e)
                })
                log_event(f"SQL Error: {str(e)}", "error")
            finally:
                conn.close()
            st.rerun()

        if st.session_state.query_history:
            latest = st.session_state.query_history[0]
            st.divider()
            st.subheader("📊 Query Result")

            mc1, mc2, mc3, mc4 = st.columns(4)
            mc1.metric("Status", "✅ Success" if latest["success"] else "❌ Error")
            mc2.metric("Rows", latest["rows"])
            mc3.metric("Columns", latest["cols"])
            mc4.metric("Time", f"{latest['time_ms']} ms")

            if latest["success"] and latest["result"] is not None:
                result_df = latest["result"]
                st.dataframe(result_df, use_container_width=True, height=300)

                with export_col:
                    csv_data = result_df.to_csv(index=False).encode("utf-8")
                    st.download_button("⬇️ Export CSV", data=csv_data,
                                       file_name=f"query_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                                       mime="text/csv", use_container_width=True)

                numeric_cols = result_df.select_dtypes(include='number').columns.tolist()
                non_numeric_cols = result_df.select_dtypes(exclude='number').columns.tolist()
                if len(numeric_cols) >= 1 and len(result_df) > 1:
                    with st.expander("📈 Quick Visualization", expanded=False):
                        chart_type = st.radio("Chart type", ["Bar", "Line", "Area"], horizontal=True)
                        y_col = st.selectbox("Y-axis (numeric)", numeric_cols)
                        x_col = st.selectbox("X-axis", non_numeric_cols if non_numeric_cols else numeric_cols)
                        chart_df = result_df[[x_col, y_col]].set_index(x_col)
                        if chart_type == "Bar":
                            st.bar_chart(chart_df)
                        elif chart_type == "Line":
                            st.line_chart(chart_df)
                        else:
                            st.area_chart(chart_df)

            elif not latest["success"]:
                st.error(f"**SQL Error:** {latest['error']}")
                st.info("💡 Tables: `transactions`, `blocks`, `consensus_rounds`, `consensus_votes`, `audit_log`")

            if len(st.session_state.query_history) > 1:
                st.divider()
                st.subheader("🕐 Query History")
                for hist in st.session_state.query_history[1:]:
                    icon = "✅" if hist["success"] else "❌"
                    label = f"{icon} [{hist['time_ms']}ms | {hist['rows']} rows] {hist['query'][:80]}{'...' if len(hist['query']) > 80 else ''}"
                    with st.expander(label, expanded=False):
                        st.code(hist["query"], language="sql")
                        if hist["success"] and hist["result"] is not None:
                            st.dataframe(hist["result"], use_container_width=True)
                        elif hist["error"]:
                            st.error(hist["error"])
        else:
            st.info("👆 Select a preset or write your own SQL, then click **Run Query**.")
            st.markdown("Tables available: `transactions`, `blocks`, `consensus_rounds`, `consensus_votes`, `audit_log`")


if __name__ == "__main__":
    main()
    
    
def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="blockchain_db"   # ← make sure this matches exactly, no typo
    )
    return conn