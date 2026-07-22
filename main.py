from flask import Flask, render_template_string, request, redirect
import stripe, sqlite3

app = Flask(__name__)

# Stripe Secret Key configure ki gayi hai
stripe.api_key = "sk_test_51TvhWHDx1KUbUr9R50C0iRfzQh5HJ4tTbOM5cSoG0UjDWKHkfKKuJ05qexY9YTyureRbGNh7l10h53tiqvmzteiw00cFJ6FEsW"

def init_db():
    conn = sqlite3.connect('payments.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS transactions 
                 (tid TEXT PRIMARY KEY, amount INTEGER)''')
    conn.commit()
    conn.close()
init_db()

content = [
    {
        "title": "80000+ ZIP FILE'S CHANNEL",
        "text": "😍 <b>80000+ zip file's Channel</b> 💔<br>━━━━━━━━━━━━━━━━━━━━<br>Benefits:<br>• 📁 All Dark Zip Files Available<br>• 🆕 New Files Added Daily", 
        "media_type": "img",
        "media": "/static/1.jpg", 
        "price_val": 799,
        "price": "Rs. 799.00"
    },
    {
        "title": "50K+ MMS LEAK PACK",
        "text": "🔞 <b>50K+ MMS LEAK IN JUST ₹120/-</b> 💦<br>━━━━━━━━━━━━━━━━━━━━<br>🔥 ALL TYPE AVAILABLE", 
        "media_type": "video",
        "media": "/static/1.mp4", 
        "price_val": 120,
        "price": "Rs. 120.00"
    },
    {
        "title": "VIP STUFF AVAILABLE",
        "text": "🥷 <b>VIP STUFF AVAILABLE</b> 🇨🇦<br>━━━━━━━━━━━━━━━━━━━━", 
        "media_type": "img",
        "media": "/static/3.jpg", 
        "price_val": 69,
        "price": "Rs. 69.00"
    },
    {
        "title": "PREMIUM DESI MAAL",
        "text": "🔞 <b>PREMIUM DESI MAAL</b> 🍑<br>━━━━━━━━━━━━━━━━━━━━", 
        "media_type": "video",
        "media": "/static/2.mp4", 
        "price_val": 99,
        "price": "Rs. 99.00"
    }
]

HTML = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        @keyframes borderGlow {
            0% { border-color: rgba(255, 255, 255, 0.1); box-shadow: 0 0 10px rgba(0, 0, 0, 0.5); }
            50% { border-color: rgba(255, 235, 59, 0.5); box-shadow: 0 0 20px rgba(255, 235, 59, 0.2); }
            100% { border-color: rgba(255, 255, 255, 0.1); box-shadow: 0 0 10px rgba(0, 0, 0, 0.5); }
        }

        body { 
            background: #050505; 
            color: #fff; 
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
            margin: 0; 
            padding-top: 70px; 
            padding-bottom: 70px; 
            min-height: 100vh; 
            text-transform: uppercase; 
        }

        .header { 
            position: fixed; 
            top: 0; 
            width: 100%; 
            background: rgba(10, 10, 10, 0.95); 
            backdrop-filter: blur(10px); 
            padding: 10px; 
            display: flex; 
            justify-content: space-between; 
            align-items: center; 
            z-index: 1000; 
            box-sizing: border-box; 
            border-bottom: 1px solid rgba(255,255,255,0.08); 
        }

        .nav-btn { font-size: 11px; font-weight: 900; letter-spacing: 1px; color: #fff; padding: 6px 12px; border-radius: 8px; background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.15); white-space: nowrap; cursor: pointer; transition: all 0.3s ease; }
        .nav-btn:hover { background: rgba(255,235,59,0.15); color: #ffeb3b; border-color: #ffeb3b; }

        .card { 
            background: #111111; 
            padding: 15px; 
            margin: 15px auto; 
            width: 90%; 
            border-radius: 15px; 
            border: 1px solid rgba(255,255,255,0.08); 
            animation: borderGlow 4s infinite;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.8); 
        }

        .card p { font-size: 13px; font-weight: 800; letter-spacing: 0.5px; line-height: 1.5; color: #d0d0d0; }
        
        .btn-demo { background: #222; color: #ffeb3b; width: 100%; padding: 10px; margin-bottom: 10px; border: 1px solid rgba(255,235,59,0.3); border-radius: 8px; font-weight: 900; font-size: 12px; letter-spacing: 1px; cursor: pointer; transition: 0.2s; }
        .btn-demo:hover { background: #333; }

        .btn-buy { background: linear-gradient(45deg, #28a745, #20c997); color: white; width: 100%; padding: 10px; border: none; border-radius: 8px; font-weight: 900; font-size: 12px; letter-spacing: 1px; cursor: pointer; transition: 0.2s; }
        .btn-buy:hover { opacity: 0.9; transform: scale(1.01); }

        .menu { display: none; position: absolute; top: 45px; left: 10px; background: #141414; border-radius: 10px; padding: 10px; border: 1px solid rgba(255,255,255,0.15); width: 140px; z-index: 1001; box-shadow: 0 5px 20px rgba(0,0,0,0.9); font-size: 11px; font-weight: 800; color: white; }
        .menu div:hover { color: #ffeb3b; background: rgba(255,255,255,0.05); border-radius: 5px; }

        .bottom-nav { position: fixed; bottom: 0; left: 0; width: 100%; background: rgba(10, 10, 10, 0.95); backdrop-filter: blur(10px); display: flex; justify-content: space-around; padding: 10px 0; border-top: 1px solid rgba(255,255,255,0.08); z-index: 1000; box-sizing: border-box; }
        .nav-item { text-align: center; color: #777; cursor: pointer; font-size: 10px; font-weight: 900; letter-spacing: 1px; text-decoration: none; transition: 0.3s; }
        .nav-item.active { color: #ffeb3b; text-shadow: 0 0 10px rgba(255,235,59,0.4); }
        .nav-item div { font-size: 18px; margin-bottom: 2px; }

        .float-admin { position: fixed; bottom: 70px; right: 20px; background: #0088cc; color: white; padding: 10px 18px; border-radius: 25px; font-size: 11px; font-weight: 900; text-decoration: none; box-shadow: 0 4px 15px rgba(0,136,204,0.4); z-index: 999; display: flex; align-items: center; gap: 6px; border: 1px solid rgba(255,255,255,0.2); cursor: pointer; }
        
        .page-section { display: none; }
        .page-section.active { display: block; }

        .store-title { text-align: center; font-size: 20px; font-weight: 900; letter-spacing: 2px; margin: 20px 0; color: #ffeb3b; text-shadow: 0 0 10px rgba(255,235,59,0.2); }
        .review-card, .profile-card { background: #111; border: 1px solid rgba(255,255,255,0.08); width: 90%; margin: 15px auto; padding: 15px; border-radius: 15px; box-shadow: 0 5px 20px rgba(0,0,0,0.6); }
    </style>
</head>
<body>

    <div class="header">
        <div style="position:relative;">
            <div class="nav-btn" onclick="toggleMenu(event)">⚙️ SETTINGS</div>
            <div id="m" class="menu">
                <div style="padding:8px; cursor:pointer;" onclick="switchPage('profile', document.querySelectorAll('.nav-item')[2]); closeMenu();">👤 PROFILE</div>
                <div style="padding:8px; cursor:pointer;" onclick="startCheckout(100); closeMenu();">💳 ADD FUNDS</div>
                <div style="padding:8px; cursor:pointer;" onclick="window.open('https://t.me/Skjsbsh166', '_blank'); closeMenu();">🎧 SUPPORT</div>
            </div>
        </div>
        <div class="nav-btn" style="border-color:#ffeb3b; color:#ffeb3b;">💰 WALLET: ₹{{ total_wallet }}</div>
    </div>

    <a href="https://t.me/Skjsbsh166" target="_blank" class="float-admin">✈️ Contact Admin</a>

    <!-- HOME PAGE -->
    <div id="page-home" class="page-section active">
        <div class="store-title">✨ CP STORE</div>
        {% for i in content %}
        <div class="card">
            {% if i.media_type == 'video' %}
                <video width="100%" controls style="border-radius:10px;">
                    <source src="{{ i.media }}" type="video/mp4">
                </video>
            {% else %}
                <img src="{{ i.media }}" style="width:100%; border-radius:10px;">
            {% endif %}
            <p>{{ i.text|safe }}</p>
            <p style="color:#ffeb3b; font-weight:900; font-size:14px;">PRICE: {{ i.price }}</p>
            <button class="btn-demo" onclick="window.open('https://t.me/+JBVaDAvX-To1NzRl')">FREE DEMO</button>
            <button class="btn-buy" onclick="startCheckout('{{ i.price_val }}')">UNLOCK PREMIUM</button>
        </div>
        {% endfor %}
    </div>

    <!-- REVIEWS PAGE -->
    <div id="page-reviews" class="page-section">
        <div class="store-title">✨ REVIEWS</div>
        <div class="review-card">
            <div style="color:gold; font-size:14px;">★★★★★ <span style="float:right; color:#ffeb3b; font-size:11px;">Verified</span></div>
            <p style="font-size:13px; margin:10px 0;">"Files direct mil gayi, content bilkul real aur HD hai!"</p>
            <div style="font-size:10px; color:#ffeb3b;">📦 80000+ ZIP FILE'S CHANNEL</div>
        </div>
        <div class="review-card">
            <div style="color:gold; font-size:14px;">★★★★★ <span style="float:right; color:#ffeb3b; font-size:11px;">Verified</span></div>
            <p style="font-size:13px; margin:10px 0;">"Instant automatic access mil gaya payment hote hi. Best store!"</p>
            <div style="font-size:10px; color:#ffeb3b;">📦 50K+ MMS LEAK PACK</div>
        </div>
    </div>

    <!-- PROFILE PAGE -->
    <div id="page-profile" class="page-section">
        <div class="store-title">✨ MY PROFILE</div>
        <div class="profile-card" style="text-align:center;">
            <div style="font-size:45px; margin-bottom:10px;">👑</div>
            <div style="font-size:18px; font-weight:900; color:#ffeb3b;">VIP MEMBER</div>
            <div style="display:inline-block; background:rgba(255,235,59,0.1); padding:6px 15px; border-radius:20px; font-size:11px; margin-top:10px; border:1px solid rgba(255,235,59,0.3); color:#fff;">Status: Active</div>
        </div>
        <div class="profile-card" style="display:flex; justify-content:space-between; align-items:center;">
            <div>
                <div style="font-size:11px; color:#777;">WALLET BALANCE</div>
                <div style="font-size:18px; font-weight:900; color:#ffeb3b; margin-top:3px;">₹{{ total_wallet }}</div>
            </div>
            <button class="nav-btn" onclick="startCheckout(100)" style="background:#28a745; border:none;">ADD FUNDS</button>
        </div>
    </div>

    <!-- BOTTOM NAVIGATION -->
    <div class="bottom-nav">
        <div class="nav-item active" onclick="switchPage('home', this)"><div>🏠</div> Home</div>
        <div class="nav-item" onclick="switchPage('reviews', this)"><div>⭐</div> Reviews</div>
        <div class="nav-item" onclick="switchPage('profile', this)"><div>👤</div> Profile</div>
    </div>

    <script>
        function switchPage(pageId, element) {
            document.querySelectorAll('.page-section').forEach(el => el.classList.remove('active'));
            document.querySelectorAll('.nav-item').forEach(el => el.classList.remove('active'));
            document.getElementById('page-' + pageId).classList.add('active');
            if(element) element.classList.add('active');
            window.scrollTo(0, 0);
        }

        function toggleMenu(event) {
            event.stopPropagation();
            let m = document.getElementById('m');
            m.style.display = (m.style.display === 'block') ? 'none' : 'block';
        }

        function closeMenu() { document.getElementById('m').style.display = 'none'; }
        window.onclick = function() { closeMenu(); }

        function startCheckout(amount) {
            fetch('/create-checkout-session', {
                method: 'POST',
                headers: {'Content-Type': 'application/x-www-form-urlencoded'},
                body: 'amount=' + amount
            })
            .then(response => response.json())
            .then(data => {
                if(data.url) {
                    window.location.href = data.url;
                } else {
                    alert("Error creating payment session");
                }
            });
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    conn = sqlite3.connect('payments.db')
    c = conn.cursor()
    c.execute("SELECT SUM(amount) FROM transactions")
    res = c.fetchone()[0]
    total_wallet = res if res else 0
    conn.close()
    return render_template_string(HTML, content=content, total_wallet=total_wallet)

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        amount = int(request.form.get('amount', 100))
    except ValueError:
        amount = 100

    try:
        # Stripe automated checkout session create karega
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'inr',
                    'product_data': {'name': 'VIP Store Credit / Premium Access'},
                    'unit_amount': amount * 100, # Stripe takes amount in paisa
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.host_url + 'success?amount=' + str(amount),
            cancel_url=request.host_url + '',
        )
        return {"url": checkout_session.url}
    except Exception as e:
        return {"error": str(e)}, 400

@app.route('/success')
def success():
    amount = request.args.get('amount', '100')
    try:
        amt_val = int(amount)
    except:
        amt_val = 100

    # Payment successful hone par database mein automatically add ho jayega
    conn = sqlite3.connect('payments.db')
    c = conn.cursor()
    import uuid
    dummy_tid = "STRIPE_" + uuid.uuid4().hex[:8].upper()
    c.execute("INSERT OR IGNORE INTO transactions VALUES (?, ?)", (dummy_tid, amt_val))
    conn.commit()
    conn.close()

    return redirect('/')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
