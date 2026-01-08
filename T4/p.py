import random
import time

class CongestionControl:
    def __init__(self):
        self.window_size = 1
        self.max_window = 10

    def send_packets(self):  # sourcery skip: use-named-expression
        print(f"\nSending {self.window_size} packets...")
        
        # Random congestion simulation
        congestion = random.choice([True, False, False])

        if congestion:
            print("⚠ Congestion detected!")
            self.window_size = max(1, self.window_size // 2)
        else:
            print("✅ No congestion")
            if self.window_size < self.max_window:
                self.window_size += 1

    def start(self):
        for _ in range(10):
            self.send_packets()
            time.sleep(1)

# Run simulator
cc = CongestionControl()
cc.start()



import hashlib
import time

class Block:
    def __init__(self, index, data, prev_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_data = f"{self.index}{self.timestamp}{self.data}{self.prev_hash}"
        return hashlib.sha256(block_data.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "Genesis Block", "0")

    def add_block(self, data):
        prev_block = self.chain[-1]
        new_block = Block(len(self.chain), data, prev_block.hash)
        self.chain.append(new_block)

    def validate_chain(self):
        for i in range(1, len(self.chain)):
            curr = self.chain[i]
            prev = self.chain[i - 1]

            if curr.hash != curr.calculate_hash():
                return False
            if curr.prev_hash != prev.hash:
                return False
        return True

# Run blockchain
bc = Blockchain()
bc.add_block("Transaction A → B ₹500")
bc.add_block("Transaction B → C ₹200")

print("Blockchain valid?", bc.validate_chain())

for block in bc.chain:
    print("\nBlock", block.index)
    print("Data:", block.data)
    print("Hash:", block.hash)
    print("Previous Hash:", block.prev_hash)

import hashlib
import time
import random

# -------------------------------
# Utility Hash Function
# -------------------------------
def sha256(data):
    return hashlib.sha256(data.encode()).hexdigest()

# -------------------------------
# Transaction Class
# -------------------------------
class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.timestamp = time.time()
        self.hash = self.generate_hash()

    def generate_hash(self):
        data = f"{self.sender}{self.receiver}{self.amount}{self.timestamp}"
        return sha256(data)

# -------------------------------
# Merkle Tree Class
# -------------------------------
class MerkleTree:
    def __init__(self, hashes):
        self.root = self.build_tree(hashes)

    def build_tree(self, hashes):
        if len(hashes) == 1:
            return hashes[0]

        new_level = []
        for i in range(0, len(hashes), 2):
            left = hashes[i]
            right = hashes[i] if i + 1 == len(hashes) else hashes[i + 1]
            new_level.append(sha256(left + right))

        return self.build_tree(new_level)

# -------------------------------
# Validator Node (Consensus)
# -------------------------------
class ValidatorNode:
    def __init__(self, node_id):
        self.node_id = node_id

    def validate_transaction(self, transaction):
        if transaction.amount <= 0:
            return False
        if transaction.sender == transaction.receiver:
            return False

        # Simulate unreliable network
        return random.choice([True, True, True, False])

# -------------------------------
# Consensus Validation
# -------------------------------
def consensus_validation(transaction):
    validators = [
        ValidatorNode(1),
        ValidatorNode(2),
        ValidatorNode(3),
        ValidatorNode(4),
        ValidatorNode(5),
    ]

    approvals = 0
    print("\nValidating transaction using consensus...\n")

    for validator in validators:
        result = validator.validate_transaction(transaction)
        print(f"Validator {validator.node_id} approval: {result}")
        if result:
            approvals += 1

    print(f"\nApprovals: {approvals}/{len(validators)}")

    if approvals > len(validators) // 2:
        print("\n✅ Transaction APPROVED by consensus.")
    else:
        print("\n❌ Transaction REJECTED by consensus.")

# -------------------------------
# Merkle Tree + Tampering Demo
# -------------------------------
def merkle_tree_with_tampering():
    n = int(input("\nEnter number of transactions: "))
    transactions = []

    for i in range(n):
        print(f"\nTransaction {i}")
        sender = input("Sender: ")
        receiver = input("Receiver: ")
        amount = float(input("Amount: "))
        transactions.append(Transaction(sender, receiver, amount))

    # Original Merkle Root
    original_hashes = [tx.hash for tx in transactions]
    original_root = MerkleTree(original_hashes).root

    print("\n✅ Original Merkle Root:")
    print(original_root)

    # Ask for tampering
    choice = input("\nDo you want to demonstrate tampering? (yes/no): ").lower()

    if choice != "yes":
        print("\nNo tampering performed. Data remains intact.")
        return

    # Select transaction index
    index = int(input(f"\nEnter transaction index to tamper (0 to {n-1}): "))

    if index < 0 or index >= n:
        print("❌ Invalid transaction index.")
        return

    old_amount = transactions[index].amount
    print(f"Old amount: {old_amount}")

    new_amount = float(input("Enter new amount: "))

    if new_amount == old_amount:
        print("\n⚠️ Amount not changed. Transaction remains same.")
    else:
        transactions[index].amount = new_amount
        transactions[index].hash = transactions[index].generate_hash()
        print("\n⚠️ Transaction has been modified.")

    # New Merkle Root
    new_hashes = [tx.hash for tx in transactions]
    new_root = MerkleTree(new_hashes).root

    print("\n🔁 New Merkle Root:")
    print(new_root)

    # Comparison
    print("\n🔍 Integrity Check Result:")
    if original_root != new_root:
        print("🚨 Data Tampering Detected! Merkle Roots do not match.")
    else:
        print("✅ No Tampering Detected. Merkle Roots match.")

# -------------------------------
# Main Program
# -------------------------------
def main():
    print("\n=== Blockchain Transaction Validator ===")
    print("1. Merkle Tree Validation (with Tampering)")
    print("2. Consensus Validation")

    choice = input("\nSelect validation type (1 or 2): ")

    if choice == "1":
        merkle_tree_with_tampering()

    elif choice == "2":
        sender = input("\nSender: ")
        receiver = input("Receiver: ")
        amount = float(input("Amount: "))
        tx = Transaction(sender, receiver, amount)
        consensus_validation(tx)

    else:
        print("\n❌ Invalid choice.")

# -------------------------------
# Run Program
# -------------------------------
if __name__ == "__main__":
    main()