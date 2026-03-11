// ===== DATA with RANDOM stock quantity (11 to 24) =====
const productsData = [
    {
        id: 1, name: "Apple iPhone 15 Pro", category: "Mobiles", price: 134900, img: "i15p.jpeg", discount: 8, rating: 4.8, reviews: "12,340 ratings", stock: Math.floor(Math.random() * 14) + 11,
        highlights: ["6.1-inch Super Retina XDR ProMotion display", "A17 Pro chip — industry-first 3nm processor", "48MP Main + 12MP Ultra Wide + 12MP 3x Telephoto", "Titanium design — lighter yet stronger than steel", "Action Button for instant one-press shortcuts"]
    },
    {
        id: 2, name: "Samsung Galaxy S24 Ultra", category: "Mobiles", price: 129999, img: "s24u.jpeg", discount: 10, rating: 4.7, reviews: "9,820 ratings", stock: Math.floor(Math.random() * 14) + 11,
        highlights: ["6.8-inch Dynamic AMOLED 2X, 120Hz adaptive", "200MP main camera with 10x Optical Zoom", "Snapdragon 8 Gen 3 — fastest Android chip", "Built-in S Pen with enhanced AI writing tools", "5000mAh + 45W wired / 15W wireless charging"]
    },
    {
        id: 3, name: "Google Pixel 8 Pro", category: "Mobiles", price: 106999, img: "gp8p.jpeg", discount: 12, rating: 4.6, reviews: "5,210 ratings", stock: Math.floor(Math.random() * 14) + 11,
        highlights: ["6.7-inch LTPO OLED, 1-120Hz variable refresh", "Google Tensor G3 chip with on-device AI", "50MP + 48MP + 48MP triple camera system", "7 years of Android OS & security updates", "Magic Eraser, Photo Unblur & Best Take AI features"]
    },
    {
        id: 4, name: "Apple MacBook Air M2", category: "Laptops", price: 94900, img: "Mac.jpeg", discount: 5, rating: 4.9, reviews: "18,540 ratings", stock: Math.floor(Math.random() * 14) + 11,
        highlights: ["Apple M2 chip — up to 18 hours battery life", "13.6-inch Liquid Retina display, 500 nits brightness", "8GB unified memory, 256GB SSD storage", "Fanless, completely silent operation", "MagSafe 3 + two Thunderbolt / USB 4 ports"]
    },
    {
        id: 5, name: "Dell XPS 13 Plus", category: "Laptops", price: 159990, img: "Dell.jpeg", discount: 7, rating: 4.5, reviews: "3,670 ratings", stock: Math.floor(Math.random() * 14) + 11,
        highlights: ["13.4-inch OLED 3.5K touch display, 60Hz", "13th Gen Intel Core i7-1360P processor", "16GB LPDDR5 RAM + 512GB NVMe PCIe SSD", "Capacitive function row with seamless touchpad", "Ultra-compact 1.26 kg chassis"]
    },
    {
        id: 6, name: "Sony WH-1000XM5", category: "Audio", price: 24990, img: "He.jpeg", discount: 15, rating: 4.8, reviews: "22,100 ratings", stock: Math.floor(Math.random() * 14) + 11,
        highlights: ["Industry-leading ANC with 8 microphones", "30-hour battery + 3-min quick charge for 3 hours", "Multipoint Bluetooth — connect 2 devices at once", "Speak-to-Chat pauses music when you talk", "Soft fit leather for all-day comfort"]
    },
    {
        id: 7, name: "JBL Flip 6", category: "Audio", price: 9999, img: "JBLF6.jpeg", discount: 20, rating: 4.6, reviews: "14,230 ratings", stock: Math.floor(Math.random() * 14) + 11,
        highlights: ["JBL Original Pro Sound with racetrack-shaped driver", "IP67 rated — waterproof, dustproof, mudproof", "12 hours of continuous playtime", "PartyBoost — sync 2 JBL speakers wirelessly", "USB-C fast charging"]
    },
    {
        id: 8, name: "Apple Watch Series 9", category: "Watch", price: 41900, img: "aws9.jpeg", discount: 6, rating: 4.8, reviews: "8,990 ratings", stock: Math.floor(Math.random() * 14) + 11,
        highlights: ["New S9 chip with Double Tap gesture control", "Always-On Retina display — 2000 nits brightness", "Blood Oxygen app + ECG + Crash Detection", "watchOS 10 with new Smart Stack widgets", "Up to 18-hour battery, 36hr Low Power Mode"]
    },
    {
        id: 9, name: "Samsung Galaxy Watch 6", category: "Watch", price: 29999, img: "sgw6.jpeg", discount: 12, rating: 4.5, reviews: "6,120 ratings", stock: Math.floor(Math.random() * 14) + 11,
        highlights: ["Advanced sleep coaching with sleep score", "BioActive Sensor — heart rate, ECG, body fat", "40mm Super AMOLED display, 2000 nits", "Sapphire Crystal glass for scratch resistance", "40 hours typical battery life"]
    },
    {
        id: 10, name: "Canon EOS R6 Mark II", category: "Cameras", price: 215995, img: "Canon.jpeg", discount: 4, rating: 4.9, reviews: "2,340 ratings", stock: Math.floor(Math.random() * 14) + 11,
        highlights: ["40fps continuous RAW burst shooting", "6K oversampled 4K 60p video, no crop", "Dual UHS-II SD card slots", "In-body 8-stop image stabilization (IBIS)", "Advanced animal, vehicle & eye-tracking AF"]
    },
    {
        id: 11, name: "Nike Air Jordan 1", category: "Fashion", price: 16995, img: "NAJ1.jpeg", discount: 10, rating: 4.7, reviews: "31,400 ratings", stock: Math.floor(Math.random() * 14) + 11,
        highlights: ["Premium full-grain leather upper", "Iconic Wings logo on the ankle collar", "Encapsulated Nike Air heel cushioning", "Rubber outsole with herringbone traction pattern", "OG colourway inspired by Michael Jordan's 1985 debut"]
    },
    {
        id: 12, name: "Ray-Ban Aviator", category: "Fashion", price: 8590, img: "RBA.jpeg", discount: 5, rating: 4.6, reviews: "19,880 ratings", stock: Math.floor(Math.random() * 14) + 11,
        highlights: ["Classic teardrop lens — 100% UV protection", "Lightweight gold-tone metal frame", "Iconic double bridge design since 1937", "Crystal lenses for superior optical clarity", "Adjustable nose pads for a custom fit"]
    },
    {
        id: 13, name: "Logitech MX Master 3S", category: "Accessories", price: 9995, img: "LMM3S.jpeg", discount: 18, rating: 4.8, reviews: "11,230 ratings", stock: Math.floor(Math.random() * 14) + 11,
        highlights: ["MagSpeed electromagnetic scrolling — whisper quiet", "8000 DPI high-precision sensor on any surface", "Silent clicks — 90% noise reduction vs standard", "Connect up to 3 devices, switch with one button", "USB-C quick charge: 1 min = 3 hours of use"]
    },
    {
        id: 14, name: "Keychron Q1 Pro", category: "Accessories", price: 18999, img: "Kq1P.jpeg", discount: 8, rating: 4.7, reviews: "3,410 ratings", stock: Math.floor(Math.random() * 14) + 11,
        highlights: ["QMK/VIA fully programmable with any key remap", "Bluetooth 5.1 wireless + USB-C wired dual mode", "Gasket-mount design for a soft, bouncy typing feel", "CNC machined full-aluminium body", "Hot-swappable PCB — swap switches without soldering"]
    },
    {
        id: 15, name: "Nespresso Coffee Machine", category: "Home", price: 18500, img: "NCM.jpeg", discount: 14, rating: 4.5, reviews: "7,600 ratings", stock: Math.floor(Math.random() * 14) + 11,
        highlights: ["19-bar high-pressure pump for rich espresso", "Rapid heat-up in just 25 seconds", "Compact design — fits any kitchen countertop", "Compatible with all Original Nespresso capsules", "Energy-saving auto off after 9 minutes"]
    },
    {
        id: 16, name: "Dyson V12 Detect Slim", category: "Home", price: 42900, img: "DV12DS.jpeg", discount: 9, rating: 4.7, reviews: "4,980 ratings", stock: Math.floor(Math.random() * 14) + 11,
        highlights: ["Laser Slim Fluffy head reveals microscopic dust", "HEPA filtration captures 99.97% of particles", "Up to 60 minutes run time on eco mode", "LCD screen shows real-time suction & motor data", "5 power modes for carpet, hard floor & crevices"]
    }
];

// cart = { productId: quantity }  (map for easy qty management)
let cartMap = JSON.parse(localStorage.getItem('shopCartMap')) || {};
let registeredUsers = JSON.parse(localStorage.getItem('shopUsers')) || {};
let currentUser = localStorage.getItem('activeUser') || null;
let userOrders = JSON.parse(localStorage.getItem('shopOrders')) || {};
let activeCategory = 'All', searchQuery = '', pendingCheckout = false;
let generatedOTP = null, tempSignupData = {}, pendingReturnIndex = null;
let detailProductId = null, detailQty = 1;

// COUPON SYSTEM VARS
let currentCouponCode = null;
let currentDiscountRate = 0;
// 1. ADDED MORE COUPONS HERE
const VALID_COUPONS = {
    "WELCOME10": 0.10,
    "SALE20": 0.20,
    "FLASH30": 0.30,
    "NEWUSER50": 0.50,
    "FESTIVE15": 0.15
};

window.onload = () => { renderCategories(); renderProducts(); updateCartUI(); checkUser(); };

function formatPrice(p) { return "₹" + p.toLocaleString('en-IN'); }
function getMRP(price, disc) { return Math.round(price / (1 - disc / 100)); }
function genStars(r) {
    const full = Math.floor(r);
    return '★'.repeat(full) + (r % 1 >= 0.5 ? '⯨' : '') + '☆'.repeat(5 - full - (r % 1 >= 0.5 ? 1 : 0));
}

// --- Stock helpers ---
function availableStock(p) {
    return Math.max(0, p.stock - (cartMap[p.id] || 0));
}
function getStockInfo(p) {
    const avail = availableStock(p);
    if (p.stock === 0) return { label: 'Out of Stock', cls: 'out-of-stock', badgeCls: 'out-of-stock' };
    if (avail === 0) return { label: 'All in your cart!', cls: 'low-stock', badgeCls: 'low-stock' };
    if (p.stock <= 3) return { label: `Only ${p.stock} left!`, cls: 'low-stock', badgeCls: 'low-stock' };
    return { label: `In Stock (${p.stock})`, cls: 'in-stock', badgeCls: 'in-stock' };
}

// --- Cart quantity in cart (how many of this product are in cart) ---
function cartQtyForProduct(id) { return cartMap[id] || 0; }
function totalCartItems() { return Object.values(cartMap).reduce((a, b) => a + b, 0); }

function renderCategories() {
    const cats = ['All', ...new Set(productsData.map(p => p.category))];
    document.getElementById('category-list').innerHTML = cats.map(c =>
        `<div class="filter-option ${c === activeCategory ? 'active' : ''}" onclick="setCategory('${c}')">${c}</div>`
    ).join('');
}
function setCategory(c) { activeCategory = c; renderCategories(); renderProducts(); }
function handleSearch() { searchQuery = document.getElementById('search-input').value.toLowerCase(); renderProducts(); }

function renderProducts() {
    const container = document.getElementById('product-grid');
    const filtered = productsData.filter(p =>
        (activeCategory === 'All' || p.category === activeCategory) && p.name.toLowerCase().includes(searchQuery)
    );
    document.getElementById('result-count').innerText = filtered.length;
    if (!filtered.length) { container.innerHTML = "<p>No products found.</p>"; return; }
    container.innerHTML = filtered.map(p => {
        const mrp = getMRP(p.price, p.discount);
        const si = getStockInfo(p);
        const oos = p.stock === 0;
        const avail = availableStock(p);
        const inCart = cartQtyForProduct(p.id);
        const canAdd = !oos && avail > 0;
        return `<div class="product-card ${oos ? 'out-of-stock' : ''}" onclick="openDetail(${p.id})">
            <div class="card-img">
                <img src="${p.img}" alt="${p.name}" referrerpolicy="no-referrer" onerror="this.onerror=null;this.src='https://placehold.co/400?text=Image+Unavailable';">
                ${oos ? '<div class="oos-overlay">OUT OF STOCK</div>' : ''}
            </div>
            <span class="stock-badge ${si.badgeCls}">${si.label}</span>
            <div class="p-cat">${p.category}</div>
            <div class="p-title" title="${p.name}">${p.name}</div>
            <div class="p-price">${formatPrice(p.price)} <span style="font-size:12px;color:#888;font-weight:400;text-decoration:line-through;">${formatPrice(mrp)}</span>
                <span style="font-size:11px;color:#007600;font-weight:600;margin-left:4px;">${p.discount}% off</span>
            </div>
            <div class="btn-group">
                ${inCart > 0 && !oos ? `
                <div class="card-qty-control" onclick="event.stopPropagation()">
                    <button onclick="event.stopPropagation();cardDecreaseQty(${p.id})">−</button>
                    <span class="qty-num">${inCart}</span>
                    <button onclick="event.stopPropagation();cardIncreaseQty(${p.id})" ${!canAdd ? 'disabled' : ''}>+</button>
                </div>` : ''}
                <div class="btn-row">
                    ${oos
                ? `<button class="add-btn" disabled>Out of Stock</button><button class="buy-btn" disabled>Unavailable</button>`
                : inCart > 0
                    ? `<button class="buy-btn" style="flex:1" onclick="event.stopPropagation();buyNow(${p.id})">Buy Now</button>`
                    : `<button class="add-btn" onclick="event.stopPropagation();addToCart(${p.id},1)">Add to Cart</button>
                    <button class="buy-btn" onclick="event.stopPropagation();buyNow(${p.id})">Buy Now</button>`
            }
                </div>
            </div>
        </div>`;
    }).join('');
}

// Card-level qty controls
function cardIncreaseQty(id) {
    const p = productsData.find(x => x.id === id);
    if (!p) return;
    const avail = availableStock(p);
    if (avail > 0) {
        cartMap[id] = (cartMap[id] || 0) + 1;
        saveCart(); updateCartUI(); renderProducts();
    }
}
function cardDecreaseQty(id) {
    const cur = cartQtyForProduct(id);
    if (cur <= 1) {
        delete cartMap[id];
    } else {
        cartMap[id] = cur - 1;
    }
    saveCart(); updateCartUI(); renderProducts();
}

// ===== PRODUCT DETAIL =====
function openDetail(id) {
    const p = productsData.find(x => x.id === id);
    if (!p) return;
    detailProductId = id;
    detailQty = 1;
    const mrp = getMRP(p.price, p.discount);
    const oos = p.stock === 0;
    const avail = availableStock(p);

    document.getElementById('dtop-cat').innerText = p.category;
    document.getElementById('d-cat').innerText = p.category;
    document.getElementById('d-name').innerText = p.name;
    const img = document.getElementById('d-img');
    img.src = p.img; img.alt = p.name;
    img.onerror = function () { this.src = 'https://placehold.co/400?text=Image'; };
    document.getElementById('d-oos-overlay').style.display = (oos || avail === 0) ? 'flex' : 'none';
    if (!oos && avail === 0) {
        document.getElementById('d-oos-overlay').innerText = 'ALL STOCK IN CART';
        document.getElementById('d-oos-overlay').style.fontSize = '13px';
    } else {
        document.getElementById('d-oos-overlay').innerText = 'OUT OF STOCK';
        document.getElementById('d-oos-overlay').style.fontSize = '15px';
    }

    document.getElementById('d-stars').innerText = genStars(p.rating);
    document.getElementById('d-rnum').innerText = p.rating;
    document.getElementById('d-rcnt').innerText = '(' + p.reviews + ')';
    document.getElementById('d-price').innerText = formatPrice(p.price);
    document.getElementById('d-mrp').innerText = 'M.R.P: ' + formatPrice(mrp);
    document.getElementById('d-save').innerText = `Save ${formatPrice(mrp - p.price)} (${p.discount}% off)`;

    const stockEl = document.getElementById('d-stock-status');
    if (oos) {
        stockEl.className = 'detail-stock-status out';
        stockEl.innerText = 'Out of Stock';
    } else if (avail === 0) {
        stockEl.className = 'detail-stock-status low';
        stockEl.innerText = `All ${p.stock} units are in your cart`;
    } else if (p.stock <= 3) {
        stockEl.className = 'detail-stock-status low';
        stockEl.innerText = `Only ${avail} left available (${cartQtyForProduct(id)} in cart)`;
    } else {
        stockEl.className = 'detail-stock-status in';
        stockEl.innerText = `In Stock — ${avail} available`;
    }

    const qtyWrapper = document.getElementById('d-qty-wrapper');
    const canAdd = !oos && avail > 0;
    qtyWrapper.style.display = canAdd ? 'flex' : 'none';
    if (canAdd) {
        if (detailQty > avail) detailQty = avail;
        updateDetailQtyUI(p);
    }

    document.getElementById('d-highlights').innerHTML = p.highlights.map(h => `<li>${h}</li>`).join('');

    const addBtn = document.getElementById('d-add');
    const buyBtn = document.getElementById('d-buy');
    const effectiveOos = oos || avail === 0;
    addBtn.disabled = effectiveOos; buyBtn.disabled = oos;

    addBtn.onclick = (e) => { e.stopPropagation(); if (!effectiveOos) { addToCart(id, detailQty); closeDetail(); } };
    buyBtn.onclick = (e) => { e.stopPropagation(); if (!oos) { if (!effectiveOos) addToCart(id, detailQty); closeDetail(); initiateCheckout(); } };

    document.getElementById('detail-modal').classList.add('open');
    document.body.style.overflow = 'hidden';
}
function updateDetailQtyUI(p) {
    if (!p) p = productsData.find(x => x.id === detailProductId);
    const avail = availableStock(p);
    document.getElementById('d-qty-num').innerText = detailQty;
    document.getElementById('d-qty-minus').disabled = detailQty <= 1;
    document.getElementById('d-qty-plus').disabled = detailQty >= avail;
    const maxNote = avail <= 5 ? `Max ${avail} more available` : '';
    document.getElementById('d-qty-max').innerText = maxNote;
}
function changeDetailQty(delta) {
    const p = productsData.find(x => x.id === detailProductId);
    if (!p) return;
    const avail = availableStock(p);
    detailQty = Math.max(1, Math.min(avail, detailQty + delta));
    updateDetailQtyUI(p);
}
function closeDetail() {
    document.getElementById('detail-modal').classList.remove('open');
    document.body.style.overflow = '';
}
function handleDetailBgClick(e) { if (e.target === document.getElementById('detail-modal')) closeDetail(); }

// --- CART LOGIC ---
function addToCart(id, qty = 1) {
    const p = productsData.find(x => x.id === id);
    if (!p || p.stock === 0) return;
    const cur = cartQtyForProduct(id);
    const newQty = Math.min(p.stock, cur + qty);
    cartMap[id] = newQty;
    saveCart(); updateCartUI(); renderProducts();
}
function buyNow(id, qty = 1) { addToCart(id, qty); initiateCheckout(); }
function saveCart() { localStorage.setItem('shopCartMap', JSON.stringify(cartMap)); }

function updateCartUI() {
    const totalItems = totalCartItems();
    document.getElementById('cart-badge').innerText = totalItems;
    const container = document.getElementById('cart-items');
    let total = 0;
    const ids = Object.keys(cartMap).map(Number);

    if (!ids.length) {
        container.innerHTML = '<p style="text-align:center;color:#888;padding:30px 0;">Your cart is empty</p>';
        document.getElementById('cart-item-count').innerText = '';
        document.getElementById('cart-total').innerText = '₹0';
        return;
    }

    container.innerHTML = ids.map(id => {
        const p = productsData.find(x => x.id === id);
        if (!p) return '';
        const qty = cartMap[id];
        const lineTotal = p.price * qty;
        total += lineTotal;
        return `<div class="cart-item">
            <img class="cart-item-img" src="${p.img}" referrerpolicy="no-referrer" onerror="this.src='https://placehold.co/54'">
            <div class="cart-item-info">
                <div class="cart-item-name">${p.name}</div>
                <div class="cart-item-price">${formatPrice(p.price)} each</div>
                <div style="display:flex;align-items:center;gap:12px;">
                    <div class="cart-qty-control">
                        <button onclick="cartChangeQty(${id},-1)" ${qty <= 1 ? '' : ''}>−</button>
                        <span class="cqty-num">${qty}</span>
                        <button onclick="cartChangeQty(${id},1)" ${qty >= p.stock ? 'disabled' : ''}>+</button>
                    </div>
                    <span style="font-size:12px;color:#555;">= <strong>${formatPrice(lineTotal)}</strong></span>
                </div>
                ${p.stock <= 3 ? `<div style="font-size:11px;color:#e65100;margin-top:4px;">⚠ Only ${p.stock} in stock</div>` : ''}
            </div>
            <span style="color:red;cursor:pointer;font-size:22px;line-height:1;padding:2px 4px;" onclick="removeCartItem(${id})">&times;</span>
        </div>`;
    }).join('');

    document.getElementById('cart-item-count').innerText = `${totalItems} item${totalItems !== 1 ? 's' : ''} in cart`;
    document.getElementById('cart-total').innerText = formatPrice(total);
}

function cartChangeQty(id, delta) {
    const p = productsData.find(x => x.id === id);
    if (!p) return;
    const cur = cartMap[id] || 0;
    const newQty = cur + delta;
    if (newQty <= 0) { delete cartMap[id]; }
    else if (newQty <= p.stock) { cartMap[id] = newQty; }
    saveCart(); updateCartUI(); renderProducts();
}
function removeCartItem(id) { delete cartMap[id]; saveCart(); updateCartUI(); renderProducts(); }
function toggleCart() { const el = document.getElementById('cart-modal'); el.style.display = el.style.display === 'block' ? 'none' : 'block'; }

// --- AUTH ---
function handleAuthClick() {
    if (currentUser) { if (confirm("Logout from ShopSphere?")) { localStorage.removeItem('activeUser'); currentUser = null; checkUser(); alert("Logged out."); } }
    else { document.getElementById('auth-modal').style.display = 'block'; toggleAuthView('login'); }
}
function closeAuthModal() { document.getElementById('auth-modal').style.display = 'none'; }
function toggleAuthView(v) {
    document.getElementById('login-view').style.display = v === 'login' ? 'block' : 'none';
    document.getElementById('signup-view').style.display = v === 'signup' ? 'block' : 'none';
    ['login-step-1', 'signup-step-1'].forEach(id => document.getElementById(id).style.display = 'block');
    ['login-step-2', 'signup-step-2'].forEach(id => document.getElementById(id).style.display = 'none');
}
function generateOTP() { generatedOTP = Math.floor(1000 + Math.random() * 9000); setTimeout(() => alert(`Your OTP is: ${generatedOTP}`), 500); }
function getLoginOTP() {
    const m = document.getElementById('login-mobile').value;
    if (!m || m.length !== 10) return alert("Enter valid 10-digit mobile number");
    if (!registeredUsers[m]) return alert("Account not found. Please Sign Up first.");
    generateOTP(); document.getElementById('login-step-1').style.display = 'none'; document.getElementById('login-step-2').style.display = 'block';
}
function verifyLoginOTP() {
    if (document.getElementById('login-otp').value == generatedOTP) {
        currentUser = document.getElementById('login-mobile').value; localStorage.setItem('activeUser', currentUser);
        checkUser(); closeAuthModal(); if (pendingCheckout) { pendingCheckout = false; openPaymentModal(); }
    } else alert("Invalid OTP");
}
function getSignupOTP() {
    const n = document.getElementById('signup-name').value, m = document.getElementById('signup-mobile').value;
    if (!n || !m || m.length !== 10) return alert("Enter valid details");
    if (registeredUsers[m]) return alert("Account already exists!");
    tempSignupData = { name: n, mobile: m }; generateOTP(); document.getElementById('signup-step-1').style.display = 'none'; document.getElementById('signup-step-2').style.display = 'block';
}
function verifySignupOTP() {
    if (document.getElementById('signup-otp').value == generatedOTP) {
        registeredUsers[tempSignupData.mobile] = tempSignupData.name; localStorage.setItem('shopUsers', JSON.stringify(registeredUsers));
        currentUser = tempSignupData.mobile; localStorage.setItem('activeUser', currentUser);
        checkUser(); closeAuthModal(); alert("Account Created!"); if (pendingCheckout) { pendingCheckout = false; openPaymentModal(); }
    } else alert("Invalid OTP");
}
function resendOTP() { generateOTP(); }
function checkUser() { document.getElementById('user-greeting').innerText = currentUser ? "Hello, " + registeredUsers[currentUser] : "Hello, Sign in"; }

// --- CHECKOUT & COUPONS ---
function initiateCheckout() {
    if (!totalCartItems()) return alert("Cart is empty");
    if (!currentUser) { pendingCheckout = true; document.getElementById('cart-modal').style.display = 'none'; handleAuthClick(); }
    else openPaymentModal();
}

function getCartTotalValue() {
    const ids = Object.keys(cartMap).map(Number);
    let total = 0;
    ids.forEach(id => {
        const p = productsData.find(x => x.id === id);
        if (p) total += p.price * cartMap[id];
    });
    return total;
}

function openPaymentModal() {
    document.getElementById('cart-modal').style.display = 'none';

    // Reset Coupon
    currentCouponCode = null;
    currentDiscountRate = 0;
    document.getElementById('coupon-input').value = "";
    document.getElementById('coupon-msg').innerHTML = "";
    document.getElementById('coupon-msg').style.color = "#555";

    updatePaymentModalTotals();
    document.getElementById('payment-modal').style.display = 'block';
}

function applyCoupon() {
    const input = document.getElementById('coupon-input').value.trim().toUpperCase();
    const msg = document.getElementById('coupon-msg');

    if (!input) {
        msg.innerHTML = "Please enter a code.";
        msg.style.color = "red";
        return;
    }

    // 2. CHECK IF USER LOGGED IN
    if (!currentUser) {
        msg.innerHTML = "Please login to use coupons.";
        msg.style.color = "red";
        return;
    }

    // 3. CHECK HISTORY (One-Time Use)
    const usedCoupons = JSON.parse(localStorage.getItem('shopUsedCoupons')) || {};
    const userHistory = usedCoupons[currentUser] || [];

    if (userHistory.includes(input)) {
        currentCouponCode = null;
        currentDiscountRate = 0;
        msg.innerHTML = `This coupon has already been used by you.`;
        msg.style.color = "red";
        updatePaymentModalTotals();
        return;
    }

    if (VALID_COUPONS[input]) {
        currentCouponCode = input;
        currentDiscountRate = VALID_COUPONS[input];
        msg.innerHTML = `Success! Coupon <strong>${input}</strong> applied.`;
        msg.style.color = "green";
        updatePaymentModalTotals();
    } else {
        currentCouponCode = null;
        currentDiscountRate = 0;
        msg.innerHTML = `Invalid coupon code.`;
        msg.style.color = "red";
        updatePaymentModalTotals();
    }
}

function updatePaymentModalTotals() {
    const subtotal = getCartTotalValue();
    const discountAmount = Math.round(subtotal * currentDiscountRate);
    const total = subtotal - discountAmount;

    document.getElementById('pay-subtotal').innerText = formatPrice(subtotal);
    document.getElementById('pay-discount').innerText = "- " + formatPrice(discountAmount);
    document.getElementById('pay-total').innerText = formatPrice(total);
}

function closePaymentModal() { document.getElementById('payment-modal').style.display = 'none'; }
function selectPayment(m, el) {
    document.querySelectorAll('.payment-details').forEach(e => e.style.display = 'none');
    document.querySelectorAll('.payment-option').forEach(e => e.classList.remove('selected'));
    document.querySelectorAll('input[name="payment"]').forEach(e => e.checked = false);
    el.classList.add('selected'); el.querySelector('input').checked = true;
    if (m === 'upi') document.getElementById('upi-fields').style.display = 'block';
    if (m === 'card') document.getElementById('card-fields').style.display = 'block';
}

function confirmOrder() {
    const btn = document.getElementById('pay-btn'); btn.innerText = "Processing..."; btn.disabled = true;
    setTimeout(() => {
        // Build items
        const items = Object.keys(cartMap).map(id => {
            const p = productsData.find(x => x.id == id);
            return { ...p, qty: cartMap[id] };
        }).filter(Boolean);

        // Calculate Final Paid Amount
        const finalTotalStr = document.getElementById('pay-total').innerText;

        const o = {
            id: 'ORD-' + Math.floor(100000 + Math.random() * 900000),
            date: new Date().toLocaleDateString('en-IN', { day: 'numeric', month: 'short', year: 'numeric' }),
            total: finalTotalStr,
            items,
            status: 'Delivered',
            returnable: true
        };

        if (!userOrders[currentUser]) userOrders[currentUser] = [];
        userOrders[currentUser].unshift(o);
        localStorage.setItem('shopOrders', JSON.stringify(userOrders));

        // 4. SAVE USED COUPON TO HISTORY
        if (currentCouponCode) {
            const usedCoupons = JSON.parse(localStorage.getItem('shopUsedCoupons')) || {};
            if (!usedCoupons[currentUser]) usedCoupons[currentUser] = [];
            usedCoupons[currentUser].push(currentCouponCode);
            localStorage.setItem('shopUsedCoupons', JSON.stringify(usedCoupons));
        }

        // ✅ DEDUCT STOCK
        Object.keys(cartMap).forEach(id => {
            const p = productsData.find(x => x.id == id);
            if (p) p.stock = Math.max(0, p.stock - cartMap[id]);
        });

        alert("Order Placed Successfully! 🎉");
        cartMap = {}; saveCart(); updateCartUI(); renderProducts(); closePaymentModal();
        btn.innerText = "Place Order"; btn.disabled = false; toggleOrders();
    }, 2000);
}

// --- ORDERS ---
function toggleOrders() {
    if (!currentUser) return alert("Please login");
    const el = document.getElementById('orders-modal'); el.style.display = el.style.display === 'block' ? 'none' : 'block';
    if (el.style.display === 'block') renderOrders();
}
function renderOrders() {
    const list = document.getElementById('orders-list'); const orders = userOrders[currentUser] || [];
    if (!orders.length) { list.innerHTML = "<p style='text-align:center;'>No orders yet.</p>"; return; }
    list.innerHTML = orders.map((o, i) => `<div class="order-card">
        <div class="order-header">
            <div><span>ORDER PLACED</span><br><strong>${o.date}</strong></div>
            <div><span>TOTAL</span><br><strong>${o.total}</strong></div>
            <div><span>ORDER # ${o.id}</span></div>
        </div>
        <div class="order-body">
            <div style="flex-grow:1;">
                <div class="order-status" style="color:${o.status === 'Returned' ? '#B12704' : '#007600'}">${o.status === 'Returned' ? 'Refund Processed' : 'Delivered'}</div>
                <div style="font-size:13px;margin-bottom:10px;">${o.items.map(x => x.name + (x.qty > 1 ? ' ×' + x.qty : '')).join(', ')}</div>
                <div style="display:flex;gap:5px;">${o.items.map(x => `<img src="${x.img}" style="width:40px;height:40px;border:1px solid #eee;object-fit:contain;" referrerpolicy="no-referrer" onerror="this.src='https://placehold.co/50'">`).join('')}</div>
            </div>
            <div>${o.status !== 'Returned' ? `<button class="return-btn" onclick="initiateReturn(${i})">Return Item</button>` : ''}</div>
        </div>
    </div>`).join('');
}
function initiateReturn(i) { pendingReturnIndex = i; generateOTP(); document.getElementById('return-modal').style.display = 'block'; }
function closeReturnModal() { document.getElementById('return-modal').style.display = 'none'; }
function verifyReturnOTP() {
    if (document.getElementById('return-otp-input').value == generatedOTP) {
        userOrders[currentUser][pendingReturnIndex].status = "Returned";
        userOrders[currentUser][pendingReturnIndex].returnable = false;
        localStorage.setItem('shopOrders', JSON.stringify(userOrders));
        closeReturnModal(); renderOrders();
        setTimeout(() => alert("Return initiated.\n\nPickup & Refund will take 3–7 days."), 200);
    } else alert("Invalid OTP. Please try again.");
}