import streamlit as st
import hashlib
import time
import random
import pandas as pd
from datetime import datetime

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
        return False, "Network Error/Malicious"

def log_event(message, type="info"):
    timestamp = datetime.now().strftime("%H:%M:%S")
    entry = {"time": timestamp, "message": message, "type": type}
    st.session_state.history.insert(0, entry)

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

    tab1, tab2 = st.tabs(["🌳 Merkle Tree & Tampering", "🤝 Consensus Protocol"])

    with tab1:
        st.header("Merkle Tree Integrity Check")
        col1, col2 = st.columns([1, 2])
        with col1:
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
                        st.rerun()
        with col2:
            if st.session_state.transactions:
                df = pd.DataFrame([t.to_dict() for t in st.session_state.transactions])
                st.dataframe(df[["Sender", "Receiver", "Amount", "Hash"]], use_container_width=True)

        if st.session_state.transactions and not st.session_state.block_finalized:
            if st.button("🔒 Finalize Block & Generate Merkle Root"):
                hashes = [tx.hash for tx in st.session_state.transactions]
                tree = MerkleTree(hashes)
                st.session_state.original_root = tree.root
                st.session_state.block_finalized = True
                log_event(f"Block Finalized. Root: {tree.root[:8]}...", "success")
                st.rerun()
        elif st.session_state.block_finalized:
            st.success(f"✅ Original Merkle Root: {st.session_state.original_root}")

    with tab2:
        st.header("Distributed Consensus")
        with st.form("consensus_form"):
            c_sender = st.text_input("Sender", "Alice")
            c_receiver = st.text_input("Receiver", "Bob")
            c_amount = st.number_input("Amount", value=50.0)
            validate_btn = st.form_submit_button("Broadcast to Network")
        if validate_btn:
            tx = Transaction(c_sender, c_receiver, c_amount)
            validators = [ValidatorNode(i) for i in range(1, 6)]
            approvals = 0
            cols = st.columns(5)
            for i, validator in enumerate(validators):
                is_valid, _ = validator.validate_transaction(tx)
                if is_valid:
                    approvals += 1
                with cols[i]:
                    st.markdown(f"**Node {validator.node_id}**")
                    if is_valid:
                        st.success("✅ APPROVED")
                    else:
                        st.error("❌ REJECTED")
            if approvals > len(validators) // 2:
                st.success(f"APPROVED ({approvals}/5)")
            else:
                st.error(f"REJECTED ({approvals}/5)")

if __name__ == "__main__":
    main()
