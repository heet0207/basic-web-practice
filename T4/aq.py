import streamlit as st
import hashlib
import time
import random
import pandas as pd
from datetime import datetime
import mysql.connector

# -------------------------------
# DATABASE CONNECTION UTILITIES
# -------------------------------
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",      # Default XAMPP user
        password="",      # Default XAMPP password
        database="blockchain_db"
    )

def save_transaction_to_db(tx):
    conn = get_db_connection()
    cursor = conn.cursor()
    # Explicitly matching the table columns: sender, receiver, amount, timestamp, tx_hash
    query = "INSERT INTO transactions (sender, receiver, amount, timestamp, tx_hash) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (tx.sender, tx.receiver, tx.amount, tx.timestamp, tx.hash))
    conn.commit()
    cursor.close()
    conn.close()

def save_block_to_db(root):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "INSERT INTO blocks (merkle_root) VALUES (%s)"
    cursor.execute(query, (root,))
    conn.commit()
    cursor.close()
    conn.close()

def save_consensus_to_db(tx, approvals, total_nodes, status):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "INSERT INTO consensus_logs (sender, receiver, amount, approvals, total_nodes, status) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (tx.sender, tx.receiver, tx.amount, approvals, total_nodes, status))
    conn.commit()
    cursor.close()
    conn.close()

# -------------------------------
# BLOCKCHAIN LOGIC CLASSES
# -------------------------------
def sha256(data):
    return hashlib.sha256(data.encode()).hexdigest()
class Transaction:
    def __init__(self, sender, receiver, amount, timestamp=None, tx_hash=None):
        self.sender = sender
        self.receiver = receiver
        self.amount = float(amount)
        self.timestamp = timestamp if timestamp else time.time()
        self.hash = tx_hash if tx_hash else self.generate_hash()

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
        if not hashes: return None
        if len(hashes) == 1: return hashes[0]
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
        if transaction.amount <= 0: return False, "Invalid Amount"
        # 80% chance of being an honest node
        is_honest = random.choices([True, False], weights=[0.8, 0.2])[0]
        return (True, "Valid") if is_honest else (False, "Network Failure")

def log_event(message, type="info"):
    timestamp = datetime.now().strftime("%H:%M:%S")
    if 'history' not in st.session_state: st.session_state.history = []
    st.session_state.history.insert(0, {"time": timestamp, "message": message, "type": type})

# -------------------------------
# MAIN STREAMLIT INTERFACE
# -------------------------------
def main():
    st.set_page_config(page_title="Blockchain DBMS", layout="wide")
    st.title("⛓️ Full-Stack Blockchain & DBMS Integrator")

    # Session State Init
    if 'transactions' not in st.session_state: st.session_state.transactions = []
    if 'original_root' not in st.session_state: st.session_state.original_root = None
    if 'block_finalized' not in st.session_state: st.session_state.block_finalized = False
    if 'history' not in st.session_state: st.session_state.history = []

    # Sidebar
    with st.sidebar:
        st.header("⚙️ Network Controls")
        if st.session_state.block_finalized:
            if st.button("😈 Simulate Cyber Attack", type="primary"):
                if st.session_state.transactions:
                    idx = random.randint(0, len(st.session_state.transactions)-1)
                    st.session_state.transactions[idx].amount += 5000.0
                    st.session_state.transactions[idx].hash = st.session_state.transactions[idx].generate_hash()
                    log_event(f"TAMPERED: Tx {idx} modified!", "error")
                    st.rerun()
        
        st.divider()
        st.subheader("Audit Log")
        for item in st.session_state.history[:5]:
            st.caption(f"[{item['time']}] {item['message']}")

    tab1, tab2, tab3 = st.tabs(["🌳 Merkle & DB Storage", "🤝 Consensus Hub", "📊 phpMyAdmin View"])

    # TAB 1: DATA STORAGE
    with tab1:
        col1, col2 = st.columns([1, 2])
        with col1:
            st.subheader("Add to Blockchain")
            with st.form("tx_form", clear_on_submit=True):
                s = st.text_input("Sender")
                r = st.text_input("Receiver")
                a = st.number_input("Amount", min_value=1.0)
                if st.form_submit_button("Record Transaction"):
                    if s and r:
                        new_tx = Transaction(s, r, a)
                        st.session_state.transactions.append(new_tx)
                        save_transaction_to_db(new_tx) # Saves to MySQL
                        st.session_state.block_finalized = False
                        log_event(f"Tx recorded in DB", "success")
                        st.rerun()

        with col2:
            st.subheader("Current Block Metadata")
            if st.session_state.transactions:
                df = pd.DataFrame([t.to_dict() for t in st.session_state.transactions])
                st.dataframe(df, use_container_width=True)
                
                if not st.session_state.block_finalized:
                    if st.button("🔒 Finalize Block & Save Merkle Root"):
                        hashes = [t.hash for t in st.session_state.transactions]
                        root = MerkleTree(hashes).root
                        st.session_state.original_root = root
                        st.session_state.block_finalized = True
                        save_block_to_db(root) # Saves to MySQL
                        log_event("Merkle Root committed to DB", "success")
                        st.rerun()
                else:
                    curr_root = MerkleTree([t.hash for t in st.session_state.transactions]).root
                    if curr_root == st.session_state.original_root:
                        st.success(f"✅ Integrity Verified. Merkle Root: {curr_root}")
                    else:
                        st.error(f"🚨 ALERT: Root Mismatch! Original: {st.session_state.original_root}")

    # TAB 2: CONSENSUS
    with tab2:
        st.header("Distributed Consensus Simulation")
        
        with st.form("consensus_node_form"):
            c_s = st.text_input("Sender Account", "Alice")
            c_r = st.text_input("Receiver Account", "Bob")
            c_a = st.number_input("Transfer Value", value=100.0)
            if st.form_submit_button("Broadcast to Validators"):
                temp_tx = Transaction(c_s, c_r, c_a)
                nodes = [ValidatorNode(i) for i in range(1, 6)]
                
                cols = st.columns(5)
                approvals = 0
                for i, node in enumerate(nodes):
                    valid, msg = node.validate_transaction(temp_tx)
                    if valid: approvals += 1
                    with cols[i]:
                        st.metric(f"Node {node.node_id}", "PASS" if valid else "FAIL")
                
                status = "APPROVED" if approvals > 2 else "REJECTED"
                save_consensus_to_db(temp_tx, approvals, 5, status) # Saves to MySQL
                
                if status == "APPROVED":
                    st.success(f"Network Consensus Reached: {approvals}/5 Nodes Approved.")
                else:
                    st.error(f"Consensus Failed: Only {approvals}/5 Nodes Approved.")

    # TAB 3: LIVE DB VIEW
    with tab3:
        st.header("Live MySQL Database Tables")
        try:
            conn = get_db_connection()
            st.subheader("📋 Transactions Table (`transactions`)")
            st.dataframe(pd.read_sql("SELECT * FROM transactions", conn), use_container_width=True)
            
            st.subheader("🛡️ Consensus Logs (`consensus_logs`)")
            st.dataframe(pd.read_sql("SELECT * FROM consensus_logs", conn), use_container_width=True)
            
            st.subheader("📦 Finalized Blocks (`blocks`)")
            st.dataframe(pd.read_sql("SELECT * FROM blocks", conn), use_container_width=True)
            conn.close()
        except Exception as e:
            st.error(f"Connection Error: {e}")

if __name__ == "__main__":
    main()