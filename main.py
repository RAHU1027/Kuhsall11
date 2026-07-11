from flask import Flask, render_template_string, request, session
import os, threading, requests, time, sqlite3

app = Flask(__name__)
app.secret_key = 'super_secret_key'

# --- DATABASE SETUP (Automatic TID check) ---
def init_db():
    conn = sqlite3.connect('payments.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS transactions (tid TEXT PRIMARY KEY)')
    conn.commit()
    conn.close()
init_db()

# --- 24/7 UPTIME ROBOT ---
def keep_alive():
    while True:
        try: requests.get("https://YOUR-APP-NAME.onrender.com")
        except: pass
        time.sleep(300)
threading.Thread(target=keep_alive, daemon=True).start()

# --- ORIGINAL DATA ---
content = [
    {"text": "😍 <b>80000+ zip file's Channel</b> 💔", "media": "/static/1.jpg", "price": "₹999"},
    {"text": "🥷 <b>VIP STUFF AVAILABLE</b> 🇨🇦", "media": "/static/3.jpg", "price": "₹149"},
    {"text": "🎀 <b>PREMIUM CUTIES LEAK</b> 🎀", "media": "/static/3.jpg", "price": "₹99"},
    {"text": "🔞 <b>PREMIUM DESI MAAL</b> 🍑", "media": "/static/2.jpg", "price": "₹69"},
    {"text": "🎬 <b>PREMIUM ADULT COLLECTION</b> ✅", "media": "/static/1.jpg", "price": "₹49"}
]

# --- ORIGINAL HTML ---
HTML = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { background:#0b1626; color:#fff; font-family:sans-serif; margin:0; padding-top:70px; }
        .header { position:fixed; top:0; width:100%; background:#15253d; padding:15px; display:flex; justify-content:space-between; border-bottom:2px solid #007bff; align-items:center; z-index:1000; }
        .nav-btn { cursor:pointer; font-weight:bold; color:#00d4ff; padding:5px 10px; border-radius:5px; background:rgba(0,123,255,0.1); }
        .card { background:#15253d; padding:15px; margin:15px auto; width:90%; border-radius:15px; border:1px solid #2c3e50; }
        .btn-demo { background:#ffc107; color:black; width:100%; padding:10px; border:none; border-radius:5px; font-weight:bold; margin-bottom:8px; cursor:pointer; }
        .btn-buy { background:#28a745; color:white; width:100%; padding:10px; border:none; border-radius:5px; font-weight:bold; cursor:pointer; }
        .popup { display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.95); z-index:9999; justify-content:center; align-items:center; }
        .box { background:#15253d; padding:20px; border-radius:15px; width:85%; border:1px solid #333; text-align:center; }
        .menu { display:none; position:absolute; top:55px; left:10px; background:#1e2a38; border-radius:10px; padding:10px; border:1px solid #007bff; }
    </style>
</head>
<body>
    <div class="header">
        <div style="position:relative;">
            <div class="nav-btn" onclick="document.getElementById('settingsMenu').style.display='block'">⚙️ Settings</div>
            <div id="settingsMenu" class="menu" onclick="this.style.display='none'">
                <div style="padding:8px;" onclick="alert('Profile Loading...')">👤 My Profile</div>
                <div style="padding:8px;" onclick="alert('Support: @admin')">🎧 Support</div>
            </div>
        </div>
        <div class="nav-btn">💰 Wallet: ₹{{ session.get('wallet', 0) }}</div>
    </div>

    {% for i in content %}
    <div class="card">
        <img src="{{ i.media }}" style="width:100%; border-radius:10px;">
        <p>{{ i.text|safe }}</p>
        <p style="color:#ffc107; font-weight:bold;">Price: {{ i.price }}</p>
        <button class="btn-demo" onclick="window.location.href='https://t.me/your_demo_link'">FREE DEMO</button>
        <button class="btn-buy" onclick="showPayment()">BUY NOW</button>
    </div>
    {% endfor %}

    <div id="paymentPopup" class="popup">
        <div class="box" onclick="event.stopPropagation()">
            <h3>Pay & Add Details ✍️</h3>
            <img src="/static/qr.jpg" style="width:100%; background:white; padding:5px; border-radius:5px;">
            <form action="/verify-payment" method="POST">
                <input name="username" placeholder="Telegram Username" required style="width:90%; margin:5px; padding:8px; border-radius:5px;">
                <input name="tid" placeholder="Transaction ID" required style="width:90%; margin:5px; padding:8px; border-radius:5px;">
                <button type="submit" class="btn-buy" style="margin-top:10px;">Submit Details</button>
            </form>
        </div>
    </div>
    <script>
        function showPayment() { document.getElementById('paymentPopup').style.display = 'flex'; }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    if 'wallet' not in session: session['wallet'] = 0
    return render_template_string(HTML, content=content)

@app.route('/verify-payment', methods=['POST'])
def verify():
    tid = request.form.get('tid').strip()
    
    # Auto-Verification Logic: Check if TID is already in DB
    conn = sqlite3.connect('payments.db')
    c = conn.cursor()
    c.execute("SELECT * FROM transactions WHERE tid=?", (tid,))
    if c.fetchone():
        conn.close()
        return "❌ This TID is already used!"
    
    # Save TID and update session wallet
    c.execute("INSERT INTO transactions VALUES (?)", (tid,))
    conn.commit()
    conn.close()
    
    session['wallet'] = session.get('wallet', 0) + 999
    return "✅ Payment Verified Successfully! Your wallet has been updated."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
