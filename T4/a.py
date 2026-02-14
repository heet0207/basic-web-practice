import streamlit as st
import hashlib
import time
import random
import pandas as pd
from datetime import datetime

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

        # Simulate Network/Validator Reliability (80% honest)
        is_honest = random.choices([True, False], weights=[0.8, 0.2])[0]
        if is_honest:
            return True, "Valid"
        else:
            return False, "Network Error/Malicious"

# -------------------------------
# Logging Helper
# -------------------------------
def log_event(message, type="info"):
    """
    Adds an event to the session state history.
    Types: info, success, warning, error
    """
    timestamp = datetime.now().strftime("%H:%M:%S")
    entry = {
        "time": timestamp,
        "message": message,
        "type": type
    }
    st.session_state.history.insert(0, entry)

# -------------------------------
# Streamlit App Logic
# -------------------------------
def main():
    st.set_page_config(page_title="Blockchain Validator", layout="wide")
    st.title("⛓️ Blockchain Transaction Validator")

    # Initialize Session State
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

    # ---------------------------
    # SIDEBAR: ACTIONS & LOGS
    # ---------------------------
    with st.sidebar:
        st.header("⚙️ Network Actions")
        
        # --- NEW: Quick Tamper Button ---
        if st.session_state.block_finalized:
            if st.button("😈 Simulate Cyber Attack (Tamper)", type="primary"):
                if st.session_state.transactions:
                    # Pick random transaction
                    idx = random.randint(0, len(st.session_state.transactions) - 1)
                    tx = st.session_state.transactions[idx]
                    
                    # Tamper with amount
                    old_amt = tx.amount
                    tx.amount = round(random.uniform(1000, 9999), 2)
                    tx.hash = tx.generate_hash() # Hash changes!
                    
                    # Recalculate Root immediately
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

        # History Display
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
    tab1, tab2 = st.tabs(["🌳 Merkle Tree & Tampering", "🤝 Consensus Protocol"])

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
                        st.session_state.tampered_root = None # Reset tamper state
                        
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

        # Merkle Root Generation
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

        # Tampering Detection Logic
        if st.session_state.block_finalized and st.session_state.transactions:
            st.divider()
            
            # Recalculate current root to see if it matches original
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
                
                # Check if we need to log this detection (avoid spamming)
                if not st.session_state.tampered_root: 
                     st.session_state.tampered_root = current_root
                     log_event("🚨 TAMPERING DETECTED! Root Mismatch.", "error")
            
            else:
                st.info("✅ Data is intact. No tampering detected.")

            # Manual Tampering (Optional)
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

if __name__ == "__main__":
    main()