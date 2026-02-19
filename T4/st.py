import streamlit as st
import hashlib
import time
import random
import mysql.connector
import pandas as pd
import graphviz

# ==========================================
# 1. ADVANCED CONFIGURATION & STYLING
# ==========================================
st.set_page_config(
    page_title="Nexus Blockchain | Advanced Validator",
    page_icon="🔗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for a modern look
st.markdown("""
<style>
    .stMetric {
        background-color: #f0f2f6;
        padding: 10px;
        border-radius: 10px;
    }
    .status-approved { color: #00cc00; font-weight: bold; }
    .status-rejected { color: #ff3333; font-weight: bold; }
    div[data-testid="stExpander"] {
        border: 1px solid #ddd;
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. DATABASE LAYER
# ==========================================
class db_manager:
    def get_connection(self):
        return mysql.connector.connect(
            host="localhost", user="root", password="", database="advanced_blockchain"
        )

    def init_genesis_block(self):
        """Ensures a Genesis block exists if DB is empty"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM blocks")
        if cursor.fetchone()[0] == 0:
            genesis_hash = hashlib.sha256("GENESIS".encode()).hexdigest()
            cursor.execute(
                "INSERT INTO blocks (block_index, timestamp, previous_hash, merkle_root, block_hash, nonce) VALUES (%s, %s, %s, %s, %s, %s)",
                (0, time.time(), "0", genesis_hash, genesis_hash, 0)
            )
            conn.commit()
        conn.close()

    def save_block(self, block):
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            # 1. Save Block
            cursor.execute(
                "INSERT INTO blocks (block_index, timestamp, previous_hash, merkle_root, block_hash, nonce) VALUES (%s, %s, %s, %s, %s, %s)",
                (block.index, block.timestamp, block.previous_hash, block.merkle_root, block.hash, block.nonce)
            )
            # 2. Save Transactions
            for tx in block.transactions:
                cursor.execute(
                    "INSERT INTO transactions (block_index, sender, receiver, amount, tx_hash) VALUES (%s, %s, %s, %s, %s)",
                    (block.index, tx.sender, tx.receiver, tx.amount, tx.hash)
                )
            conn.commit()
            return True
        except Exception as e:
            st.error(f"DB Error: {e}")
            return False
        finally:
            conn.close()

    def fetch_chain(self):
        conn = self.get_connection()
        cursor = conn.cursor(dictionary=True)
        
        # Get Blocks
        cursor.execute("SELECT * FROM blocks ORDER BY block_index ASC")
        block_rows = cursor.fetchall()
        
        chain = []
        for row in block_rows:
            # Get Transactions for this block
            cursor.execute("SELECT * FROM transactions WHERE block_index = %s", (row['block_index'],))
            tx_rows = cursor.fetchall()
            
            tx_objs = [Transaction(t['sender'], t['receiver'], t['amount'], row['timestamp'], t['tx_hash']) for t in tx_rows]
            
            block = Block(row['block_index'], tx_objs, row['previous_hash'])
            block.timestamp = row['timestamp']
            block.hash = row['block_hash']
            block.merkle_root = row['merkle_root']
            block.nonce = row['nonce']
            chain.append(block)
            
        conn.close()
        return chain
    
    def get_connection(self):
        return mysql.connector.connect(
            host="127.0.0.1",  # CHANGED FROM "localhost"
            user="root",
            password="",
            database="advanced_blockchain",
            autocommit=True  # Added for stability
        )

DB = db_manager()

# ==========================================
# 3. CORE LOGIC CLASSES
# ==========================================
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
        return sha256(f"{self.sender}{self.receiver}{self.amount}{self.timestamp}")

class Block:
    def __init__(self, index, transactions, previous_hash):
        self.index = index
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.timestamp = time.time()
        self.nonce = 0
        self.merkle_root = self.calculate_merkle_root()
        self.hash = self.calculate_block_hash()

    def calculate_merkle_root(self):
        hashes = [tx.hash for tx in self.transactions]
        if not hashes: return sha256("")
        return MerkleTree(hashes).root

    def calculate_block_hash(self):
        data = f"{self.index}{self.timestamp}{self.previous_hash}{self.merkle_root}{self.nonce}"
        return sha256(data)

    def mine_block(self, difficulty=2):
        # Simple Proof of Work
        target = "0" * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_block_hash()

class MerkleTree:
    def __init__(self, hashes):
        self.leaves = hashes
        self.root = self.build_tree(hashes)

    def build_tree(self, hashes):
        if len(hashes) == 1: return hashes[0]
        new_level = []
        for i in range(0, len(hashes), 2):
            left = hashes[i]
            right = hashes[i] if i + 1 == len(hashes) else hashes[i]
            new_level.append(sha256(left + right))
        return self.build_tree(new_level)

    def visualize(self):
        """Generates a Graphviz Digraph for the tree"""
        dot = graphviz.Digraph(comment='Merkle Tree')
        dot.attr(rankdir='BT', bgcolor='transparent')
        dot.attr('node', shape='box', style='filled', fillcolor='lightblue', fontname='Courier')
        
        levels = [self.leaves]
        current = self.leaves
        while len(current) > 1:
            next_level = []
            for i in range(0, len(current), 2):
                left = current[i]
                right = current[i] if i + 1 == len(current) else current[i]
                parent = sha256(left + right)
                next_level.append(parent)
                
                # Add edges for visualization
                dot.edge(left[:8]+"...", parent[:8]+"...")
                dot.edge(right[:8]+"...", parent[:8]+"...")
            
            current = next_level
            levels.append(current)
            
        dot.node(self.root[:8]+"...", style='filled', fillcolor='gold', label=f"ROOT\n{self.root[:8]}...")
        return dot

class ValidatorNode:
    def __init__(self, id, name, reliability):
        self.id = id
        self.name = name
        self.reliability = reliability # 0.0 to 1.0

    def validate(self, block):
        # Logic: If reliability is 0.9, it has 10% chance of failing/rejecting randomly
        # Also checks basic validity
        if len(block.transactions) == 0: return False
        
        is_honest = random.random() < self.reliability
        return is_honest

# ==========================================
# 4. APP INTERFACE
# ==========================================

# Initialize DB
try:
    DB.init_genesis_block()
except:
    st.error("Please start XAMPP MySQL and create the database first.")
    st.stop()

# Sidebar Navigation
menu = st.sidebar.selectbox("Navigation", 
    ["1. New Block & Consensus", "2. Blockchain Explorer", "3. Advanced Tampering"])

# ------------------------------------------------------------------
# MODULE 1: NEW BLOCK & CONSENSUS
# ------------------------------------------------------------------
if menu == "1. New Block & Consensus":
    st.title("⛏️ Mining & Consensus Console")
    
    # Initialize Session State for Pending Transactions
    if 'pending_tx' not in st.session_state:
        st.session_state.pending_tx = []

    # Section A: Add Transactions
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("1. Add Transaction")
        with st.form("add_tx"):
            s = st.text_input("Sender")
            r = st.text_input("Receiver")
            a = st.number_input("Amount", min_value=0.1)
            add_btn = st.form_submit_button("Add to Pool")
            
            if add_btn and s and r:
                tx = Transaction(s, r, a)
                st.session_state.pending_tx.append(tx)
                st.success("Added to pool!")

    with col2:
        st.subheader("2. Mempool (Pending)")
        if st.session_state.pending_tx:
            df = pd.DataFrame([{'Sender': t.sender, 'Receiver': t.receiver, 'Amount': t.amount} 
                               for t in st.session_state.pending_tx])
            st.dataframe(df, use_container_width=True)
            
            # Action Button
            if st.button("🚀 Initiating Consensus & Mine Block"):
                # Get latest block index
                chain = DB.fetch_chain()
                last_block = chain[-1]
                
                # Create New Block
                new_block = Block(last_block.index + 1, st.session_state.pending_tx, last_block.hash)
                
                # --- CONSENSUS SIMULATION ---
                st.write("---")
                st.subheader("3. Consensus Protocol (PoA)")
                
                validators = [
                    ValidatorNode(1, "Alpha Node", 0.99),
                    ValidatorNode(2, "Beta Node", 0.95),
                    ValidatorNode(3, "Gamma Node", 0.90),
                    ValidatorNode(4, "Delta Node", 0.85),
                    ValidatorNode(5, "Epsilon Node", 0.50) # Malicious/Buggy node
                ]
                
                votes = 0
                cols = st.columns(5)
                
                for i, v in enumerate(validators):
                    with cols[i]:
                        with st.status(f"{v.name}", expanded=True) as status:
                            time.sleep(random.uniform(0.1, 0.5)) # Simulate network delay
                            if v.validate(new_block):
                                status.update(label="APPROVED", state="complete", expanded=False)
                                votes += 1
                            else:
                                status.update(label="REJECTED", state="error", expanded=False)

                st.progress(votes / 5)
                
                if votes > 2:
                    st.success(f"✅ Consensus Reached ({votes}/5). Mining Block...")
                    with st.spinner("Solving Proof of Work..."):
                        new_block.mine_block()
                        time.sleep(1)
                    
                    if DB.save_block(new_block):
                        st.balloons()
                        st.success(f"Block #{new_block.index} added to chain!")
                        st.session_state.pending_tx = [] # Clear pool
                else:
                    st.error("❌ Consensus Failed. Block discarded.")
        else:
            st.info("Add transactions to start mining.")

# ------------------------------------------------------------------
# MODULE 2: BLOCKCHAIN EXPLORER (VISUALIZATION)
# ------------------------------------------------------------------
elif menu == "2. Blockchain Explorer":
    st.title("🔗 Blockchain Ledger & Merkle Tree")
    
    chain = DB.fetch_chain()
    
    # Sidebar Block Selector
    block_id = st.sidebar.selectbox("Select Block to Inspect", [b.index for b in chain])
    selected_block = next((b for b in chain if b.index == block_id), None)
    
    if selected_block:
        # Top Metrics
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Block Index", f"#{selected_block.index}")
        c2.metric("Transactions", len(selected_block.transactions))
        c3.metric("Nonce", selected_block.nonce)
        c4.metric("Timestamp", time.strftime('%H:%M:%S', time.localtime(selected_block.timestamp)))
        
        st.divider()
        
        col_left, col_right = st.columns([1, 1])
        
        with col_left:
            st.subheader("📜 Block Header")
            st.code(f"""
Hash:         {selected_block.hash}
Prev Hash:    {selected_block.previous_hash}
Merkle Root:  {selected_block.merkle_root}
            """, language="yaml")
            
            st.subheader("📝 Transactions")
            for tx in selected_block.transactions:
                st.text(f"{tx.sender} -> {tx.receiver}: ${tx.amount}")

        with col_right:
            st.subheader("🌳 Merkle Tree Visualization")
            if len(selected_block.transactions) > 0:
                tx_hashes = [tx.hash for tx in selected_block.transactions]
                tree = MerkleTree(tx_hashes)
                
                
                st.graphviz_chart(tree.visualize())
            else:
                st.info("Genesis block or empty block has no tree.")

# ------------------------------------------------------------------
# MODULE 3: ADVANCED TAMPERING
# ------------------------------------------------------------------
elif menu == "3. Advanced Tampering":
    st.title("🕵️ Forensic Tamper Analysis")
    st.markdown("Modify a transaction in the history and watch the cryptographic breakdown.")
    
    chain = DB.fetch_chain()
    block_options = [b for b in chain if len(b.transactions) > 0]
    
    if not block_options:
        st.warning("No blocks with transactions available to tamper.")
    else:
        # Select Block
        b_sel = st.selectbox("Select Target Block", [b.index for b in block_options])
        target_block = next(b for b in block_options if b.index == b_sel)
        
        # Select Transaction
        t_sel_idx = st.selectbox("Select Transaction Index", range(len(target_block.transactions)))
        target_tx = target_block.transactions[t_sel_idx]
        
        st.write("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.info("Original Data")
            st.write(f"Amount: **{target_tx.amount}**")
            st.write(f"TX Hash: `{target_tx.hash[:15]}...`")
            st.write(f"Merkle Root: `{target_block.merkle_root[:15]}...`")
            
        with col2:
            st.error("Tampered Data")
            fake_amount = st.number_input("Inject Fake Amount", value=target_tx.amount)
            
            if st.button("⚔️ EXECUTE ATTACK"):
                if fake_amount != target_tx.amount:
                    # 1. Recalculate TX Hash
                    fake_tx_hash = sha256(f"{target_tx.sender}{target_tx.receiver}{fake_amount}{target_tx.timestamp}")
                    
                    # 2. Rebuild Tree
                    hashes = [t.hash for t in target_block.transactions]
                    hashes[t_sel_idx] = fake_tx_hash # Swap with fake hash
                    fake_tree = MerkleTree(hashes)
                    
                    # 3. Recalculate Block Hash
                    fake_block_hash = sha256(f"{target_block.index}{target_block.timestamp}{target_block.previous_hash}{fake_tree.root}{target_block.nonce}")
                    
                    st.markdown("### 💥 Attack Results")
                    st.write(f"**New TX Hash:** `{fake_tx_hash[:15]}...` (CHANGED)")
                    st.write(f"**New Merkle Root:** `{fake_tree.root[:15]}...` (CHANGED)")
                    
                    st.markdown("#### Chain Integrity Check:")
                    if fake_tree.root != target_block.merkle_root:
                         st.error("🚨 **MERKLE ROOT MISMATCH DETECTED**")
                         st.write("The block header no longer matches the data. The chain is broken.")
                        
                         # Visual Chain Reaction
                         st.graphviz_chart(f"""
                            digraph G {{
                                rankdir=LR;
                                node [shape=box];
                                Block{target_block.index} [style=filled, fillcolor=red, label="Block #{target_block.index}\\n(INVALID)"];
                                Block{target_block.index+1} [style=filled, fillcolor=orange, label="Block #{target_block.index+1}\\n(Orphaned)"];
                                Block{target_block.index} -> Block{target_block.index+1} [color=red, style=dashed];
                            }}
                        """)