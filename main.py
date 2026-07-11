from flask import Flask, render_template_string, request, jsonify
import os
import requests
import json

app = Flask(__name__)

# --- CONFIGURATION ---
TELEGRAM_BOT_TOKEN = "8991320152:AAFLJcXRpfQi3P-Wgap0bF8e5wIscG4XxY0"
TELEGRAM_CHAT_ID = "6632236983"
DOMAIN = "https://aapka-domain.onrender.com" 

# --- HELPER FUNCTIONS ---
def get_balance():
    if not os.path.exists("wallet.txt"): return "0"
    with open("wallet.txt", "r") as f: return f.read()

def update_wallet(amount):
    bal = int(get_balance())
    with open("wallet.txt", "w") as f: f.write(str(bal + int(amount)))

# --- TUMHARA ORIGINAL CONTENT ---
T1 = "😍 <b>80000+ zip file's Channel</b> 💔<br>━━━━━━━━━━━━━━━━━━━━<br><b>Benefits:</b><br>• 📁 All Dark Zip Files Available<br>• 🆕 New Files Added Daily<br>• 🔄 Forwarding Files is Allowed<br><br>🤔 <b>Want to Buy?</b><br>🚀 <i>Offers Are Live Now!</i><br><br>Price: <strike>Rs. 3,999.00</strike> <b>Rs. 99.00</b><br>🔥 <i>174 people bought this</i>"
T2 = "🎁 <b>PREMIUM COLLECTION</b> 🎁<br>━━━━━━━━━━━━━━━━━━━━<br>REAL PRICE - <strike>2499/-</strike><br>OFFER PRICE - <b>499/-</b> ✅"
T3 = "🥷 <b>VIP STUFF AVAILABLE</b> 🇨🇦<br>━━━━━━━━━━━━━━━━━━━━<br>Price: <strike>Rs. 299.00</strike> <b>Rs. 149.00</b><br>🔥 <i>94 people bought this</i>"

content = [
    {"text": T1, "media": "/static/1.jpg", "price": "₹99"},
    {"text": T2, "media": "/static/2.jpg", "price": "₹499"},
    {"text": T3, "media": "/static/3.jpg", "price": "₹149"}
]

HTML = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { background:#0b1626; color:#fff; font-family:sans-serif; margin:0; padding-top:70px; }
        .header { position:fixed; top:0; width:100%; background:#15253d; padding:15px; display:flex; justify-content:space-between; z-index:1000; border-bottom:1px solid #007bff; }
        .card { background:#15253d; border:1px solid #2c3e50; padding:15px; margin:15px auto; width:95%; max-width:400px; border-radius:15px; }
        img { width:100%; border-radius:10px; display:block; }
        .btn-demo { background:#ffc107; color:black; padding:8px; margin-bottom:10px; border-radius:5px; font-weight:bold; text-align:center; cursor:pointer; }
        .buy-btn { display:block; width:100%; background:#28a745; color:white; text-align:center; padding:12px; border-radius:8px; text-decoration:none; font-weight:bold; cursor:pointer; border:none; }
        .popup { display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.95); z-index:2000; justify-content:center; align-items:center; }
        .qr-box { background:white; padding:20px; border-radius:15px; color:black; text-align:center; width:85%; max-width:320px; }
        input { width:90%; padding:10px; margin:5px 0; border:1px solid #ccc; border-radius:5px; }
        .timer { color:red; font-size:20px; font-weight:bold; margin-bottom:10px; }
    </style>
</head>
<body>
    <div class="header">
        <div onclick="showPayment()" style="cursor:pointer; font-weight:bold;">➕ Add Payment</div>
        <div style="cursor:pointer;">💰 Wallet: ₹{{ balance }}</div>
    </div>
    {% for i in content %}
    <div class="card">
        <img src="{{ i.media }}">
        <p style="margin-top:15px; font-size:15px;">{{ i.text|safe }}</p>
        <p style="font-size:18px; color:#ffc107; font-weight:bold;">Price: {{ i.price }}</p>
        <div class="btn-demo" onclick="alert('Demo Loading...')">FREE DEMO</div>
        <button class="buy-btn" onclick="showPayment()">BUY NOW</button>
    </div>
    {% endfor %}

    <div id="paymentPopup" class="popup" onclick="this.style.display='none'">
        <div class="qr-box" onclick="event.stopPropagation()">
            <div id="timer" class="timer">04:00</div>
            <img src="/static/qr.jpg" style="width:100%; border:2px solid #ccc;">
            <p><b>UPI ID:</b> paytm.s20glin@pty</p>
            <input type="text" id="txId" placeholder="Transaction ID (UTR)">
            <input type="number" id="amount" placeholder="Amount Paid">
            <button class="buy-btn" onclick="verifyPayment()">VERIFY PAYMENT</button>
        </div>
    </div>

    <script>
        let timerInterval;
        function showPayment() { document.getElementById('paymentPopup').style.display = 'flex'; startTimer(240); }
        function startTimer(duration) {
            clearInterval(timerInterval);
            let timer = duration;
            timerInterval = setInterval(function () {
                let m = parseInt(timer / 60, 10);
                let s = parseInt(timer % 60, 10);
                document.getElementById('timer').textContent = (m<10?"0"+m:m) + ":" + (s<10?"0"+s:s);
                if (--timer < 0) { clearInterval(timerInterval); document.getElementById('paymentPopup').style.display = 'none'; }
            }, 1000);
        }
        function verifyPayment() {
            let tid = document.getElementById('txId').value;
            let amt = document.getElementById('amount').value;
            if(!tid || !amt) { alert("Pehle dono details sahi se fill karo!"); return; }
            fetch('/verify-payment', { 
                method:'POST', 
                headers:{'Content-Type':'application/json'}, 
                body:JSON.stringify({txId:tid, amount:amt}) 
            })
            .then(res=>res.json()).then(data=>{ 
                alert(data.message); 
                document.getElementById('paymentPopup').style.display = 'none'; 
            });
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home(): return render_template_string(HTML, content=content, balance=get_balance())

@app.route('/verify-payment', methods=['POST'])
def verify_payment():
    data = request.json
    tid, amt = data.get('txId'), data.get('amount')
    keyboard = {"inline_keyboard": [[{"text": "✅ VERIFY PAYMENT", "callback_data": f"ver_{amt}_{tid}"}]]}
    msg = f"🔔 *New Order*\n💰 Amt: ₹{amt}\n🆔 ID: `{tid}`"
    requests.post(f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage", 
                  json={"chat_id": TELEGRAM_CHAT_ID, "text": msg, "parse_mode": "Markdown", "reply_markup": keyboard})
    return jsonify({"message": "Request Admin ko bhej di gayi hai!"})

@app.route('/telegram-callback', methods=['POST'])
def telegram_callback():
    update = request.get_json()
    if 'callback_query' in update:
        query = update['callback_query']
        if query['data'].startswith("ver_"):
            _, amt, tid = query['data'].split("_")
            update_wallet(amt)
            requests.get(f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/answerCallbackQuery?callback_query_id={query['id']}&text=Verified! Balance Updated.")
    return "OK"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
