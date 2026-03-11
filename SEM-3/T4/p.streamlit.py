import streamlit as st
import hashlib
import time
import random

# -------------------------------
# HASH FUNCTION
# -------------------------------
def sha256(data):
    return hashlib.sha256(data.encode()).hexdigest()

# -------------------------------
# TRANSACTION CLASS
# -------------------------------
class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.timestamp = time.time()
        self.hash = self.generate_hash()

    def generate_hash(self):
        return sha256(f"{self.sender}{self.receiver}{self.amount}{self.timestamp}")

# -------------------------------
# MERKLE TREE
# -------------------------------
class MerkleTree:
    def __init__(self, hashes):
        self.levels = []
        self.root = self.build_tree(hashes)

    def build_tree(self, hashes):
        self.levels.append(hashes)

        if len(hashes) == 1:
            return hashes[0]

        new_level = []
        for i in range(0, len(hashes), 2):
            left = hashes[i]
            right = hashes[i] if i+1 == len(hashes) else hashes[i+1]
            new_level.append(sha256(left + right))

        return self.build_tree(new_level)

# -------------------------------
# CONSENSUS TREE
# -------------------------------
def consensus_tree():

    validators = []
    approvals = 0

    st.subheader("Consensus Voting")

    for i in range(5):
        vote = random.choice([True, True, True, False])
        validators.append(vote)

        if vote:
            approvals += 1

        st.write(f"Validator {i+1} ➜ {vote}")

    if approvals > 2:
        st.success("Consensus Approved")
        return True
    else:
        st.error("Consensus Rejected")
        return False

# -------------------------------
# SESSION STORAGE
# -------------------------------
if "transactions" not in st.session_state:
    st.session_state.transactions = []

# -------------------------------
# STREAMLIT UI
# -------------------------------
st.title("🔗 Blockchain Validator (Merkle + Consensus + Tampering)")

menu = st.sidebar.selectbox(
    "Menu",
    ["Add Transaction", "View Blockchain", "Tampering Demo"]
)

# ===============================
# ADD TRANSACTION
# ===============================
if menu == "Add Transaction":

    sender = st.text_input("Sender")
    receiver = st.text_input("Receiver")
    amount = st.number_input("Amount", min_value=0.0)

    if st.button("Add"):

        tx = Transaction(sender, receiver, amount)
        st.session_state.transactions.append(tx)

        st.success("Transaction Added")

        # CONSENSUS
        if consensus_tree():

            hashes = [t.hash for t in st.session_state.transactions]
            tree = MerkleTree(hashes)

            st.subheader("Merkle Tree Levels")

            for i, level in enumerate(tree.levels):
                st.write(f"Level {i+1}")
                st.code(level)

            st.success(f"Merkle Root: {tree.root}")

# ===============================
# BLOCKCHAIN VIEW
# ===============================
elif menu == "View Blockchain":

    if len(st.session_state.transactions) == 0:
        st.warning("No Transactions")

    else:
        hashes = [t.hash for t in st.session_state.transactions]
        tree = MerkleTree(hashes)

        st.subheader("Blockchain Transactions")

        for t in st.session_state.transactions:
            st.write(vars(t))

        st.success(f"Current Merkle Root: {tree.root}")

# ===============================
# TAMPERING DEMO
# ===============================
elif menu == "Tampering Demo":

    if len(st.session_state.transactions) == 0:
        st.warning("No Transactions Available")

    else:

        hashes = [t.hash for t in st.session_state.transactions]
        original_tree = MerkleTree(hashes)

        st.info(f"Original Merkle Root: {original_tree.root}")

        index = st.number_input(
            "Select Transaction Index",
            min_value=0,
            max_value=len(st.session_state.transactions)-1
        )

        new_amount = st.number_input("Enter Tampered Amount")

        if st.button("Apply Tampering"):

            tx = st.session_state.transactions[index]
            tx.amount = new_amount
            tx.hash = tx.generate_hash()

            new_hashes = [t.hash for t in st.session_state.transactions]
            new_tree = MerkleTree(new_hashes)

            st.warning(f"New Merkle Root: {new_tree.root}")

            if new_tree.root != original_tree.root:
                st.error("🚨 Tampering Detected!")
            else:
                st.success("No Tampering Detected")
