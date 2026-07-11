from flask import Flask, render_template_string, request, jsonify
import os
import requests

app = Flask(__name__)

# --- CONFIGURATION ---
TELEGRAM_BOT_TOKEN = "8991320152:AAFLJcXRpfQi3P-Wgap0bF8e5wIscG4XxY0"
TELEGRAM_CHAT_ID = "6632236983"

# --- CONTENT ---
content = [
    {"text": "😍 <b>80000+ zip file's Channel</b> 💔<br>Price: <b>Rs. 99.00</b>", "media": "/static/1.jpg"},
    {"text": "🥷 <b>VIP STUFF AVAILABLE</b> 🇨🇦<br>Price: <b>Rs. 149.00</b>", "media": "/static/2.jpg"},
    {"text": "🔞 <b>PREMIUM DESI MAAL</b> 🍑<br>Price: <b>Rs. 69.00</b>", "media": "/static/3.jpg"}
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
        .buy-btn { width:100%; background:#28a745; color:white; padding:12px; border-radius:8px; font-weight:bold; cursor:pointer; border:none; margin-top:10px; }
        .popup { display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.9); z-index:2000; justify-content:center; align-items:center; }
        .qr-box { background:#15253d; padding:20px; border-radius:20px; color:#fff; width:90%; max-width:350px; text-align:center; border:1px solid #2c3e50; }
        input { width:90%; padding:12px; margin:8px 0; border-radius:8px; border:none; background:#0b1626; color:#fff; }
        .join-btn { width:90%; background:#28a745; color:white; padding:12px; border-radius:8px; font-weight:bold; cursor:pointer; border:none; margin-top:10px; }
    </style>
</head>
<body>
    <div class="header"><div>KUSHAL STORE</div><div>💰 Wallet: ₹0</div></div>
    {% for i in content %}
    <div class="card">
        <img src="{{ i.media }}">
        <p>{{ i.text|safe }}</p>
        <button class="buy-btn" onclick="showPayment()">BUY NOW</button>
    </div>
    {% endfor %}

    <div id="paymentPopup" class="popup" onclick="this.style.display='none'">
        <div class="qr-box" onclick="event.stopPropagation()">
            <h3 style="margin-top:0;">Pay and add details ✍️</h3>
            <img src="/static/qr.jpg" style="width:100%; border-radius:10px;">
            <p style="font-size:12px; color:#ffc107;">After payment you'll be added to VIP channel</p>
            <input type="text" id="tgUser" placeholder="Telegram username (eg. @rexy2313)">
            <input type="text" id="txId" placeholder="Transaction ID / URN no.">
            <button class="join-btn" onclick="sendDetails()">Join telegram 👍</button>
        </div>
    </div>

    <script>
        function showPayment() { document.getElementById('paymentPopup').style.display = 'flex'; }
        function sendDetails() {
            let tg = document.getElementById('tgUser').value;
            let tid = document.getElementById('txId').value;
            if(!tg || !tid) { alert("Dono details bharein!"); return; }
            fetch('/send-order', { 
                method:'POST', headers:{'Content-Type':'application/json'}, 
                body:JSON.stringify({tg:tg, tid:tid}) 
            }).then(r=>r.json()).then(d=>{ alert(d.message); document.getElementById('paymentPopup').style.display='none'; });
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home(): return render_template_string(HTML, content=content)

@app.route('/send-order', methods=['POST'])
def send_order():
    data = request.json
    msg = f"🔔 *New Join Request*\n👤 TG: {data['tg']}\n🆔 ID: `{data['tid']}`"
    requests.post(f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage", 
                  json={"chat_id": TELEGRAM_CHAT_ID, "text": msg, "parse_mode": "Markdown"})
    return jsonify({"message": "Details bhej di gayi hai, wait karein!"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
