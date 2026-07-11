from flask import Flask, render_template_string, request
import os, threading, requests, time

app = Flask(__name__)

# --- CONFIGURATION ---
BOT_TOKEN = "8991320152:AAFLJcXRpfQi3P-Wgap0bF8e5wIscG4XxY0"
ADMIN_ID = "6632236983"

# --- 24/7 UPTIME ROBOT ---
def keep_alive():
    while True:
        try: requests.get("https://YOUR-APP-NAME.onrender.com")
        except: pass
        time.sleep(300)
threading.Thread(target=keep_alive, daemon=True).start()

HTML = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { background:#0b1626; color:#fff; font-family:sans-serif; margin:0; padding-top:70px; }
        .header { position:fixed; top:0; width:100%; background:#15253d; padding:15px; display:flex; justify-content:space-between; border-bottom:2px solid #007bff; align-items:center; z-index:1000; }
        .nav-btn { cursor:pointer; font-weight:bold; color:#00d4ff; padding:5px 10px; border-radius:5px; background:rgba(0,123,255,0.1); }
        .card { background:#15253d; padding:15px; margin:15px auto; width:90%; border-radius:15px; border:1px solid #2c3e50; line-height:1.6; }
        .btn-buy { background:#28a745; color:white; width:100%; padding:10px; border:none; border-radius:5px; font-weight:bold; cursor:pointer; margin-top:10px; }
        .popup { display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.95); z-index:9999; justify-content:center; align-items:center; }
        .box { background:#15253d; padding:20px; border-radius:15px; width:85%; border:1px solid #333; text-align:center; }
    </style>
</head>
<body>
    <div class="header">
        <div class="nav-btn">⚙️ Menu</div>
        <div class="nav-btn">💰 Wallet: ₹0</div>
    </div>

    <!-- Product 1 -->
    <div class="card">
        <b>😍 80000+ zip file's Channel 💔</b><br>
        ━━━━━━━━━━━━━━━━━━━━<br>
        Benefits:<br>
        • 📁 All Dark Zip Files Available<br>
        • 🆕 New Files Added Daily<br>
        • 🔄 Forwarding Files is Allowed<br><br>
        🤔 Want to Buy?<br>
        🚀 Offers Are Live Now!<br>
        Price: <del>Rs. 3,999.00</del> <b>Rs. 999.00</b><br>
        🔥 174 people bought this<br>
        <button class="btn-buy" onclick="showPayment()">BUY NOW</button>
    </div>

    <!-- Product 2 -->
    <div class="card">
        <b>📽️ AVAILABLE VIDEOS COLLECTION 🎁</b><br>
        ━━━━━━━━━━━━━━━━━━━━<br>
        REAL PRICE - 2499/-<br>
        OFFER PRICE - 499/- ✅<br><br>
        VALIDITY ~ 6 MONTH ⌛<br>
        PREMIUM QUALITY STUFF ✨<br><br>
        • INCEST ( D@RK )<br>
        • SLEEPING PILLS<br>
        • ONLY INDIAN<br><br>
        🔥 77 people bought this<br>
        <button class="btn-buy" onclick="showPayment()">BUY NOW</button>
    </div>

    <!-- Product 3 -->
    <div class="card">
        <b>🥷 VIP STUFF AVAILABLE 🇨🇦</b><br>
        ━━━━━━━━━━━━━━━━━━━━<br>
        Price: <del>Rs. 299.00</del> <b>Rs. 149.00</b><br>
        🔥 94 people bought this<br>
        <button class="btn-buy" onclick="showPayment()">BUY NOW</button>
    </div>

    <!-- Product 4 -->
    <div class="card">
        <b>🔞 PREMIUM DESI MAAL 🍑</b><br>
        ━━━━━━━━━━━━━━━━━━━━<br>
        Price: <del>Rs. 259.00</del> <b>Rs. 69.00</b><br>
        🔥 314 people bought this<br>
        <button class="btn-buy" onclick="showPayment()">BUY NOW</button>
    </div>

    <div id="paymentPopup" class="popup">
        <div class="box" onclick="event.stopPropagation()">
            <h3>Pay & Add Details ✍️</h3>
            <div id="timer" style="color:red; font-size:22px; font-weight:bold;">04:00</div>
            <img src="/static/qr.jpg" style="width:100%; background:white; padding:5px; border-radius:5px;">
            <form action="/verify-payment" method="POST">
                <input name="username" placeholder="Telegram Username" required style="width:90%; margin:5px; padding:8px; border-radius:5px;">
                <input name="tid" placeholder="Transaction ID" required style="width:90%; margin:5px; padding:8px; border-radius:5px;">
                <button type="submit" class="btn-buy">Submit Details</button>
            </form>
        </div>
    </div>

    <script>
        function showPayment() {
            document.getElementById('paymentPopup').style.display = 'flex';
            let time = 240;
            let x = setInterval(function() {
                let m = Math.floor(time / 60);
                let s = time % 60;
                document.getElementById("timer").innerHTML = "0"+m+":"+(s<10?"0":"")+s;
                if (--time < 0) { clearInterval(x); alert("Time Expired!"); location.reload(); }
            }, 1000);
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML)

@app.route('/verify-payment', methods=['POST'])
def verify():
    username = request.form.get('username')
    tid = request.form.get('tid')
    msg = f"🔔 NEW PAYMENT\nUser: {username}\nTID: {tid}\n\n[Verify & Approve Access]"
    requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", json={"chat_id": ADMIN_ID, "text": msg})
    return "Details Submitted! Waiting for Admin verification."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
