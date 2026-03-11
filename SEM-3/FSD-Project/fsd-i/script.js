/* =========================================
   1. MOCK DATA & STATE MANAGEMENT
   ========================================= */

// Mock Product Database
const products = [
    {
        id: 1,
        name: "Sony WH-1000XM5 Wireless Headphones",
        category: "Electronics",
        price: 24990,
        mrp: 29990,
        image: "https://images.unsplash.com/photo-1618366712010-f4ae9c647dcb?auto=format&fit=crop&w=500&q=80",
        rating: 4.8,
        reviews: 1240,
        stock: 15,
        highlights: ["Industry-leading noise canceling", "30-hour battery life", "Crystal clear hands-free calling"]
    },
    {
        id: 2,
        name: "Apple iPhone 15 (128GB) - Black",
        category: "Mobiles",
        price: 72999,
        mrp: 79900,
        image: "https://images.unsplash.com/photo-1510557880182-3d4d3cba35a5?auto=format&fit=crop&w=500&q=80",
        rating: 4.6,
        reviews: 850,
        stock: 5,
        highlights: ["Dynamic Island", "48MP Main Camera", "A16 Bionic chip"]
    },
    {
        id: 3,
        name: "Nike Air Jordan 1 Retro High",
        category: "Fashion",
        price: 13995,
        mrp: 16995,
        image: "https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=500&q=80",
        rating: 4.9,
        reviews: 2100,
        stock: 3, // Low stock
        highlights: ["Premium leather upper", "Air-Sole unit for cushioning", "Classic high-top support"]
    },
    {
        id: 4,
        name: "Samsung 4K Smart LED TV (55 Inch)",
        category: "Electronics",
        price: 45990,
        mrp: 65900,
        image: "https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?auto=format&fit=crop&w=500&q=80",
        rating: 4.5,
        reviews: 320,
        stock: 0, // Out of stock
        highlights: ["Crystal Processor 4K", "Tizen™ OS", "HDR 10+ Support"]
    },
    {
        id: 5,
        name: "Men's Cotton Casual Shirt",
        category: "Fashion",
        price: 899,
        mrp: 1999,
        image: "https://images.unsplash.com/photo-1596755094514-f87e34085b2c?auto=format&fit=crop&w=500&q=80",
        rating: 4.2,
        reviews: 540,
        stock: 50,
        highlights: ["100% Cotton", "Slim Fit", "Machine Washable"]
    },
    {
        id: 6,
        name: "Logitech MX Master 3S Mouse",
        category: "Electronics",
        price: 8995,
        mrp: 10995,
        image: "https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?auto=format&fit=crop&w=500&q=80",
        rating: 4.9,
        reviews: 4000,
        stock: 22,
        highlights: ["8K DPI sensor", "Quiet clicks", "Magspeed scrolling"]
    },
    {
        id: 7,
        name: "Instant Pot Duo 7-in-1 Pressure Cooker",
        category: "Home",
        price: 8499,
        mrp: 11999,
        image: "https://images.unsplash.com/photo-1556910103-1c02745a30bf?auto=format&fit=crop&w=500&q=80",
        rating: 4.7,
        reviews: 5000,
        stock: 12,
        highlights: ["7 Functions in 1", "Stainless Steel Inner Pot", "Safety Features"]
    },
    {
        id: 8,
        name: "OnePlus 11R 5G",
        category: "Mobiles",
        price: 39999,
        mrp: 44999,
        image: "https://images.unsplash.com/photo-1690312781476-06830575d563?auto=format&fit=crop&w=500&q=80",
        rating: 4.4,
        reviews: 670,
        stock: 8,
        highlights: ["Snapdragon 8+ Gen 1", "100W SUPERVOOC", "120Hz Super Fluid AMOLED"]
    }
];

// State
let cart = [];
let orders = [];
let currentUser = null; // { name: string, mobile: string }
let currentCategory = 'All';
let currentSearch = '';
let activeDiscount = 0; // % discount
let detailProductId = null;

/* =========================================
   2. INITIALIZATION & RENDERING
   ========================================= */

document.addEventListener('DOMContentLoaded', () => {
    renderCategories();
    renderProducts();
    updateCartUI();
});

function renderCategories() {
    const categories = ['All', ...new Set(products.map(p => p.category))];
    const container = document.getElementById('category-list');
    
    container.innerHTML = categories.map(cat => `
        <div class="filter-option ${cat === 'All' ? 'active' : ''}" 
             onclick="setCategory('${cat}', this)">
            ${cat}
            ${cat !== 'All' ? '›' : ''}
        </div>
    `).join('');
}

function setCategory(cat, element) {
    currentCategory = cat;
    // Update active UI
    document.querySelectorAll('.filter-option').forEach(el => el.classList.remove('active'));
    element.classList.add('active');
    renderProducts();
}

function handleSearch() {
    currentSearch = document.getElementById('search-input').value.toLowerCase();
    renderProducts();
}

function renderProducts() {
    const grid = document.getElementById('product-grid');
    const resultCount = document.getElementById('result-count');
    
    // Filter Logic
    const filtered = products.filter(p => {
        const matchCat = currentCategory === 'All' || p.category === currentCategory;
        const matchSearch = p.name.toLowerCase().includes(currentSearch) || 
                            p.category.toLowerCase().includes(currentSearch);
        return matchCat && matchSearch;
    });

    resultCount.innerText = filtered.length;

    if (filtered.length === 0) {
        grid.innerHTML = `<div style="grid-column:1/-1;text-align:center;padding:50px;color:#777;">
            <h3>No products found matching your criteria.</h3>
        </div>`;
        return;
    }

    grid.innerHTML = filtered.map(p => {
        const isOOS = p.stock === 0;
        const stockBadge = getStockBadge(p.stock);
        const discount = Math.round(((p.mrp - p.price) / p.mrp) * 100);

        return `
        <div class="product-card ${isOOS ? 'out-of-stock' : ''}" onclick="openDetail(${p.id})">
            ${stockBadge}
            <div class="card-img">
                <img src="${p.image}" alt="${p.name}">
            </div>
            <div class="p-cat">${p.category}</div>
            <div class="p-title">${p.name}</div>
            <div class="detail-rating" style="margin-bottom:5px;font-size:12px;">
                 <span class="stars">${'★'.repeat(Math.round(p.rating))}${'☆'.repeat(5-Math.round(p.rating))}</span> 
                 <span style="color:#007185;margin-left:4px;">${p.reviews}</span>
            </div>
            <div class="p-price">
                ₹${p.price.toLocaleString()} 
                <span style="font-size:12px;color:#777;text-decoration:line-through;font-weight:400">₹${p.mrp.toLocaleString()}</span>
                <span style="font-size:12px;color:#c62828;font-weight:400">(${discount}% off)</span>
            </div>
            <div class="btn-group">
                <button class="add-btn" onclick="event.stopPropagation(); addToCart(${p.id})" ${isOOS ? 'disabled' : ''}>
                    ${isOOS ? 'Out of Stock' : 'Add to Cart'}
                </button>
            </div>
        </div>
        `;
    }).join('');
}

function getStockBadge(stock) {
    if (stock === 0) return `<div class="stock-badge out-of-stock">Out of Stock</div>`;
    if (stock < 5) return `<div class="stock-badge low-stock">Only ${stock} left</div>`;
    return ''; // Don't show badge if stock is plentiful
}

/* =========================================
   3. PRODUCT DETAILS MODAL
   ========================================= */

function openDetail(id) {
    const p = products.find(x => x.id === id);
    if (!p) return;
    detailProductId = id;

    // Reset Quantity
    document.getElementById('d-qty-num').innerText = '1';

    // Populate Data
    document.getElementById('dtop-cat').innerText = p.category;
    document.getElementById('d-img').src = p.image;
    document.getElementById('d-cat').innerText = p.category;
    document.getElementById('d-name').innerText = p.name;
    document.getElementById('d-stars').innerText = '★'.repeat(Math.round(p.rating)) + '☆'.repeat(5-Math.round(p.rating));
    document.getElementById('d-rnum').innerText = p.rating;
    document.getElementById('d-rcnt').innerText = `(${p.reviews} ratings)`;
    
    document.getElementById('d-price').innerText = `₹${p.price.toLocaleString()}`;
    document.getElementById('d-mrp').innerText = `₹${p.mrp.toLocaleString()}`;
    const savings = p.mrp - p.price;
    const savePercent = Math.round((savings / p.mrp) * 100);
    document.getElementById('d-save').innerText = `Save ₹${savings.toLocaleString()} (${savePercent}%)`;

    // Stock Status
    const stockEl = document.getElementById('d-stock-status');
    const oosOverlay = document.getElementById('d-oos-overlay');
    const addBtn = document.getElementById('d-add');
    const buyBtn = document.getElementById('d-buy');

    if (p.stock === 0) {
        stockEl.className = 'detail-stock-status out';
        stockEl.innerText = 'Currently Unavailable';
        oosOverlay.style.display = 'flex';
        addBtn.disabled = true;
        buyBtn.disabled = true;
        document.getElementById('d-qty-wrapper').style.opacity = '0.5';
        document.getElementById('d-qty-wrapper').style.pointerEvents = 'none';
    } else if (p.stock < 5) {
        stockEl.className = 'detail-stock-status low';
        stockEl.innerText = `Only ${p.stock} left in stock`;
        oosOverlay.style.display = 'none';
        addBtn.disabled = false;
        buyBtn.disabled = false;
        document.getElementById('d-qty-wrapper').style.opacity = '1';
        document.getElementById('d-qty-wrapper').style.pointerEvents = 'auto';
    } else {
        stockEl.className = 'detail-stock-status in';
        stockEl.innerText = 'In Stock';
        oosOverlay.style.display = 'none';
        addBtn.disabled = false;
        buyBtn.disabled = false;
        document.getElementById('d-qty-wrapper').style.opacity = '1';
        document.getElementById('d-qty-wrapper').style.pointerEvents = 'auto';
    }

    // Highlights
    const ul = document.getElementById('d-highlights');
    ul.innerHTML = p.highlights.map(h => `<li>${h}</li>`).join('');

    // Set Button Actions
    addBtn.onclick = () => {
        const qty = parseInt(document.getElementById('d-qty-num').innerText);
        addToCart(p.id, qty);
        closeDetail();
    };
    
    buyBtn.onclick = () => {
        const qty = parseInt(document.getElementById('d-qty-num').innerText);
        addToCart(p.id, qty);
        closeDetail();
        toggleCart();
        setTimeout(initiateCheckout, 500); // Small delay for UX
    };

    document.getElementById('detail-modal').classList.add('open');
}

function closeDetail() {
    document.getElementById('detail-modal').classList.remove('open');
}

function handleDetailBgClick(e) {
    if (e.target.id === 'detail-modal') {
        closeDetail();
    }
}

function changeDetailQty(change) {
    const numEl = document.getElementById('d-qty-num');
    let current = parseInt(numEl.innerText);
    const p = products.find(x => x.id === detailProductId);
    
    let newVal = current + change;
    if (newVal < 1) newVal = 1;
    if (newVal > p.stock) newVal = p.stock;
    
    numEl.innerText = newVal;
}

/* =========================================
   4. CART MANAGEMENT
   ========================================= */

function addToCart(productId, qty = 1) {
    const product = products.find(p => p.id === productId);
    
    // Check Stock
    if (product.stock === 0) {
        alert("Sorry, this item is out of stock.");
        return;
    }

    const existingItem = cart.find(item => item.id === productId);

    if (existingItem) {
        if (existingItem.qty + qty > product.stock) {
            alert(`Cannot add more. We only have ${product.stock} in stock.`);
            return;
        }
        existingItem.qty += qty;
    } else {
        cart.push({ ...product, qty: qty });
    }

    // Animation visual cue
    const badge = document.getElementById('cart-badge');
    badge.style.transform = "scale(1.5)";
    setTimeout(() => badge.style.transform = "scale(1)", 200);

    updateCartUI();
    renderCart(); // Update panel if open
}

function removeFromCart(productId) {
    cart = cart.filter(item => item.id !== productId);
    updateCartUI();
    renderCart();
}

function updateCartQty(productId, change) {
    const item = cart.find(i => i.id === productId);
    const product = products.find(p => p.id === productId);

    if (item) {
        const newQty = item.qty + change;
        if (newQty > product.stock) {
            alert(`Max stock limit reached (${product.stock})`);
            return;
        }
        if (newQty <= 0) {
            removeFromCart(productId);
        } else {
            item.qty = newQty;
            updateCartUI();
            renderCart();
        }
    }
}

function updateCartUI() {
    const totalQty = cart.reduce((sum, item) => sum + item.qty, 0);
    const badge = document.getElementById('cart-badge');
    badge.innerText = totalQty;
    badge.style.display = totalQty > 0 ? 'flex' : 'none';
}

function toggleCart() {
    const modal = document.getElementById('cart-modal');
    if (modal.style.display === 'block') {
        modal.style.display = 'none';
    } else {
        renderCart();
        modal.style.display = 'block';
    }
}

function renderCart() {
    const container = document.getElementById('cart-items');
    const countEl = document.getElementById('cart-item-count');
    const totalEl = document.getElementById('cart-total');

    if (cart.length === 0) {
        container.innerHTML = `<div style="text-align:center;padding:40px;color:#888;">
            <p style="font-size:50px;margin-bottom:10px;">🛒</p>
            Your cart is empty
        </div>`;
        countEl.innerText = "";
        totalEl.innerText = "₹0";
        return;
    }

    let total = 0;
    container.innerHTML = cart.map(item => {
        total += item.price * item.qty;
        return `
        <div class="cart-item">
            <img src="${item.image}" class="cart-item-img">
            <div class="cart-item-info">
                <div class="cart-item-name">${item.name}</div>
                <div class="cart-item-price">₹${item.price.toLocaleString()}</div>
                <div class="cart-qty-control">
                    <button onclick="updateCartQty(${item.id}, -1)">−</button>
                    <div class="cqty-num">${item.qty}</div>
                    <button onclick="updateCartQty(${item.id}, 1)">+</button>
                </div>
            </div>
            <span style="color:#999;cursor:pointer;font-size:18px;" onclick="removeFromCart(${item.id})">&times;</span>
        </div>
        `;
    }).join('');

    countEl.innerText = `Subtotal (${cart.reduce((a,b)=>a+b.qty,0)} items):`;
    totalEl.innerText = `₹${total.toLocaleString()}`;
}

/* =========================================
   5. AUTHENTICATION (MOBILE VALIDATION)
   ========================================= */

function handleAuthClick() {
    if (currentUser) {
        // If logged in, maybe show profile or logout logic (simplified here to alert)
        const logout = confirm(`Logged in as ${currentUser.name}. Do you want to logout?`);
        if (logout) {
            currentUser = null;
            document.getElementById('user-greeting').innerText = "Hello, Sign in";
            // Clear orders/cart if desired (optional)
            alert("Logged out successfully.");
        }
    } else {
        toggleAuthView('login');
        document.getElementById('auth-modal').style.display = 'block';
    }
}

function closeAuthModal() {
    document.getElementById('auth-modal').style.display = 'none';
}

function toggleAuthView(view) {
    if (view === 'signup') {
        document.getElementById('login-view').style.display = 'none';
        document.getElementById('signup-view').style.display = 'block';
    } else {
        document.getElementById('signup-view').style.display = 'none';
        document.getElementById('login-view').style.display = 'block';
    }
}

/* --- Validation Logic --- */
function validateIndianMobile(mobile) {
    // Regex: Starts with 6, 7, 8, or 9, followed by exactly 9 digits
    const regex = /^[6-9]\d{9}$/;
    return regex.test(mobile);
}

// LOGIN FLOW
let tempMobile = '';
function getLoginOTP() {
    const mobile = document.getElementById('login-mobile').value;
    
    if (!validateIndianMobile(mobile)) {
        alert("Invalid Mobile Number. It must be 10 digits and start with 6, 7, 8, or 9.");
        return;
    }
    
    tempMobile = mobile;
    // Simulate API call
    document.getElementById('login-step-1').style.display = 'none';
    document.getElementById('login-step-2').style.display = 'block';
    alert(`OTP sent to ${mobile}: 1234`);
}

function verifyLoginOTP() {
    const otp = document.getElementById('login-otp').value;
    if (otp === '1234') {
        // Successful login
        currentUser = { name: "User", mobile: tempMobile };
        document.getElementById('user-greeting').innerText = `Hello, ${currentUser.name}`;
        closeAuthModal();
        alert("Login Successful!");
    } else {
        alert("Incorrect OTP");
    }
}

// SIGNUP FLOW
function getSignupOTP() {
    const name = document.getElementById('signup-name').value;
    const mobile = document.getElementById('signup-mobile').value;
    
    if (name.length < 2) {
        alert("Please enter a valid name.");
        return;
    }
    if (!validateIndianMobile(mobile)) {
        alert("Invalid Mobile Number. It must be 10 digits and start with 6, 7, 8, or 9.");
        return;
    }
    
    tempMobile = mobile;
    // Simulate API call
    document.getElementById('signup-step-1').style.display = 'none';
    document.getElementById('signup-step-2').style.display = 'block';
    alert(`OTP sent to ${mobile}: 1234`);
}

function verifySignupOTP() {
    const otp = document.getElementById('signup-otp').value;
    const name = document.getElementById('signup-name').value;
    
    if (otp === '1234') {
        currentUser = { name: name, mobile: tempMobile };
        document.getElementById('user-greeting').innerText = `Hello, ${currentUser.name}`;
        closeAuthModal();
        alert("Account created successfully!");
    } else {
        alert("Incorrect OTP");
    }
}

function resendOTP() {
    alert(`OTP resent to ${tempMobile}: 1234`);
}

/* =========================================
   6. CHECKOUT & PAYMENT
   ========================================= */

function initiateCheckout() {
    if (cart.length === 0) {
        alert("Your cart is empty!");
        return;
    }
    
    if (!currentUser) {
        alert("Please login to proceed.");
        handleAuthClick();
        return;
    }

    // Close Cart
    document.getElementById('cart-modal').style.display = 'none';

    // Calculate Totals
    const subtotal = cart.reduce((sum, item) => sum + (item.price * item.qty), 0);
    document.getElementById('pay-subtotal').innerText = `₹${subtotal.toLocaleString()}`;
    
    // Reset Coupon
    activeDiscount = 0;
    document.getElementById('coupon-msg').innerText = '';
    document.getElementById('coupon-msg').style.color = '#333';
    document.getElementById('coupon-input').value = '';
    updatePaymentTotal(subtotal);

    // Open Modal
    document.getElementById('payment-modal').style.display = 'block';
}

function closePaymentModal() {
    document.getElementById('payment-modal').style.display = 'none';
}

function applyCoupon() {
    const code = document.getElementById('coupon-input').value.toUpperCase();
    const subtotal = cart.reduce((sum, item) => sum + (item.price * item.qty), 0);
    const msg = document.getElementById('coupon-msg');
    
    // Coupon Logic
    const coupons = {
        'NEWUSER50': 50,
        'FLASH30': 30,
        'SALE20': 20,
        'WELCOME10': 10
    };

    if (coupons[code]) {
        activeDiscount = coupons[code];
        msg.innerText = `Success! ${activeDiscount}% discount applied.`;
        msg.style.color = 'green';
    } else {
        activeDiscount = 0;
        msg.innerText = 'Invalid Coupon Code';
        msg.style.color = 'red';
    }
    updatePaymentTotal(subtotal);
}

function updatePaymentTotal(subtotal) {
    const discountAmount = Math.round(subtotal * (activeDiscount / 100));
    const finalTotal = subtotal - discountAmount;
    
    document.getElementById('pay-discount').innerText = `-₹${discountAmount.toLocaleString()}`;
    document.getElementById('pay-total').innerText = `₹${finalTotal.toLocaleString()}`;
}

function selectPayment(method, element) {
    // Styling
    document.querySelectorAll('.payment-option').forEach(el => {
        el.classList.remove('selected');
        el.querySelector('input').checked = false;
    });
    element.classList.add('selected');
    element.querySelector('input').checked = true;

    // Show Details
    document.querySelectorAll('.payment-details').forEach(el => el.style.display = 'none');
    if (method === 'upi') document.getElementById('upi-fields').style.display = 'block';
    if (method === 'card') document.getElementById('card-fields').style.display = 'block';
}

function confirmOrder() {
    const paymentMethod = document.querySelector('input[name="payment"]:checked');
    if (!paymentMethod) {
        alert("Please select a payment method.");
        return;
    }

    // Processing Simulation
    const btn = document.getElementById('pay-btn');
    const originalText = btn.innerText;
    btn.innerText = "Processing...";
    btn.disabled = true;

    setTimeout(() => {
        const orderId = 'ORD-' + Date.now().toString().slice(-6);
        const subtotal = cart.reduce((sum, item) => sum + (item.price * item.qty), 0);
        const discountAmount = Math.round(subtotal * (activeDiscount / 100));
        
        // Move Cart to Orders
        const newOrder = {
            id: orderId,
            date: new Date().toLocaleDateString(),
            items: [...cart],
            total: subtotal - discountAmount,
            status: 'Arriving by ' + new Date(Date.now() + 2*86400000).toLocaleDateString('en-IN', {weekday:'short', day:'numeric', month:'short'})
        };

        orders.unshift(newOrder); // Add to top
        cart = []; // Clear Cart
        updateCartUI();

        // Stock Update (Simulation in local mock data only)
        newOrder.items.forEach(orderItem => {
            const product = products.find(p => p.id === orderItem.id);
            if(product) product.stock -= orderItem.qty;
        });
        
        // Re-render product grid to show updated stock
        renderProducts();

        btn.innerText = originalText;
        btn.disabled = false;
        closePaymentModal();
        alert(`Order Placed Successfully! Order ID: ${orderId}`);
        toggleOrders(); // Show orders
    }, 2000);
}

/* =========================================
   7. ORDERS & RETURNS
   ========================================= */

function toggleOrders() {
    if (!currentUser) {
        alert("Please login to view orders.");
        handleAuthClick();
        return;
    }
    const modal = document.getElementById('orders-modal');
    if (modal.style.display === 'block') {
        modal.style.display = 'none';
    } else {
        renderOrders();
        modal.style.display = 'block';
    }
}

function renderOrders() {
    const container = document.getElementById('orders-list');
    
    if (orders.length === 0) {
        container.innerHTML = `<div style="text-align:center;padding:30px;color:#777;">No past orders.</div>`;
        return;
    }

    container.innerHTML = orders.map(order => `
        <div class="order-card">
            <div class="order-header">
                <div>
                    <span>ORDER PLACED</span><br>
                    <strong>${order.date}</strong>
                </div>
                <div>
                    <span>TOTAL</span><br>
                    <strong>₹${order.total.toLocaleString()}</strong>
                </div>
                <div>
                    <span>ORDER # ${order.id}</span>
                </div>
            </div>
            <div class="order-body">
                <div style="flex:1;">
                    <div class="order-status">${order.status}</div>
                    ${order.items.map(i => `
                        <div style="display:flex;gap:10px;margin-bottom:10px;">
                            <img src="${i.image}" style="width:40px;height:40px;object-fit:contain;">
                            <div style="font-size:13px;">
                                <a href="#" style="color:#007185;font-weight:600;">${i.name}</a>
                                <div style="color:#555;">Qty: ${i.qty}</div>
                            </div>
                        </div>
                    `).join('')}
                </div>
                <div style="width:120px;text-align:right;">
                     ${order.status.includes('Returned') ? 
                        '<span style="color:#c62828;font-size:12px;font-weight:bold;">Returned</span>' : 
                        `<button class="return-btn" onclick="initiateReturn('${order.id}')">Return Items</button>`
                     }
                </div>
            </div>
        </div>
    `).join('');
}

// Return Logic
let returnOrderId = null;
function initiateReturn(oid) {
    returnOrderId = oid;
    document.getElementById('return-modal').style.display = 'block';
    // Simulate OTP sent
    alert(`Return OTP sent to ${currentUser.mobile}: 9999`);
}

function closeReturnModal() {
    document.getElementById('return-modal').style.display = 'none';
    returnOrderId = null;
}

function verifyReturnOTP() {
    const otp = document.getElementById('return-otp-input').value;
    if (otp === '9999') {
        const order = orders.find(o => o.id === returnOrderId);
        if (order) {
            order.status = 'Returned - Refund Processing';
            renderOrders();
            closeReturnModal();
            alert("Return initiated successfully. Pickup scheduled.");
        }
    } else {
        alert("Invalid OTP");
    }
}