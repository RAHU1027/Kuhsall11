from flask import Flask, render_template_string, request, jsonify
import os
import requests

app = Flask(__name__)

# --- CONFIGURATION ---
TELEGRAM_BOT_TOKEN = "8991320152:AAFLJcXRpfQi3P-Wgap0bF8e5wIscG4XxY0"
TELEGRAM_CHAT_ID = "6632236983"
# YAHA APNA RENDER URL DALEIN (Jaise: https://myapp.onrender.com)
DOMAIN = "https://aapka-domain.onrender.com" 

# --- UPDATED CONTENT ---
content = [
    {
        "text": "😍 <b>80000+ zip file's Channel</b> 💔<br>━━━━━━━━━━━━━━━━━━━━<br><b>Benefits:</b><br>• 📁 All Dark Zip Files Available<br>• 🆕 New Files Added Daily<br>• 🔄 Forwarding Files is Allowed<br><br>🤔 <b>Want to Buy?</b><br>🚀 <i>Offers Are Live Now!</i><br><br>Price: <strike>Rs. 3,999.00</strike> <b>Rs. 99.00</b><br>🔥 <i>174 people bought this</i>",
        "media": "/static/1.jpg",
        "price": "₹99"
    },
    {
        "text": "🥷 <b>VIP STUFF AVAILABLE</b> 🇨🇦<br>━━━━━━━━━━━━━━━━━━━━<br>Price: <strike>Rs. 299.00</strike> <b>Rs. 149.00</b><br>🔥 <i>94 people bought this</i>",
        "media": "/static/2.jpg",
        "price": "₹149"
    },
    {
        "text": "🔞 <b>PREMIUM DESI MAAL</b> 🍑<br>━━━━━━━━━━━━━━━━━━━━<br>Price: <strike>Rs. 259.00</strike> <b>Rs. 69.00</b><br>🔥 <i>314 people bought this</i>",
        "media": "/static/3.jpg",
        "price": "₹69"
    }
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
        .buy-btn { display:block; width:100%; background:#28a745; color:white; text-align:center; padding:12px; border-radius:8px; text-decoration:none; font-weight:bold; cursor:pointer; }
        .popup { display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.95); z-index:2000; justify-content:center; align-items:center; }
        .qr-box { background:white; padding:20px; border-radius:15px; color:black; text-align:center; width:85%; max-width:320px; }
        input { width:90%; padding:10px; margin:5px 0; border:1px solid #ccc; border-radius:5px; }
        .timer { color:red; font-size:20px; font-weight:bold; margin-bottom:10px; }
    </style>
</head>
<body>
    <div class="header">
        <div onclick="showPayment()" style="cursor:pointer; font-weight:bold;">➕ Add Payment</div>
        <div onclick="alert('Wallet Balance: ₹0')" style="cursor:pointer;">💰 Wallet: ₹0</div>
    </div>
    {% for i in content %}
    <div class="card">
        <img src="{{ i.media }}">
        <p style="margin-top:15px; font-size:15px;">{{ i.text|safe }}</p>
        <div class="btn-demo" onclick="alert('Demo Loading...')">FREE DEMO</div>
        <div class="buy-btn" onclick="showPayment()">BUY NOW</div>
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
            let timer = duration, m, s;
            timerInterval = setInterval(function () {
                m = parseInt(timer / 60, 10); s = parseInt(timer % 60, 10);
                document.getElementById('timer').textContent = (m<10?"0"+m:m) + ":" + (s<10?"0"+s:s);
                if (--timer < 0) { clearInterval(timerInterval); document.getElementById('paymentPopup').style.display = 'none'; }
            }, 1000);
        }
        function verifyPayment() {
            let tid = document.getElementById('txId').value;
            let amt = document.getElementById('amount').value;
            fetch('/verify-payment', { method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify({txId:tid, amount:amt}) })
            .then(res=>res.json()).then(data=>{ alert(data.message); document.getElementById('paymentPopup').style.display = 'none'; });
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home(): return render_template_string(HTML, content=content)

@app.route('/verify-payment', methods=['POST'])
def verify_payment():
    data = request.json
    tid = data.get('txId')
    amt = data.get('amount')
    msg = f"🔔 *New Payment Request*\n💰 Amount: ₹{amt}\n🆔 Trans ID: {tid}\n\n[✅ CLICK TO VERIFY]({DOMAIN}/admin-verify/{tid})"
    requests.get(f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage?chat_id={TELEGRAM_CHAT_ID}&text={msg}&parse_mode=Markdown")
    return jsonify({"message": "Request sent to Admin!"})

@app.route('/admin-verify/<tid>')
def admin_verify(tid):
    with open("verified_ids.txt", "a") as f: f.write(tid + "\n")
    return "<h1>Payment Verified Successfully!</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
