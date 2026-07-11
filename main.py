from flask import Flask, render_template_string, request
import os

app = Flask(__name__)

# --- TUMHARA ORIGINAL DATA ---
T1 = "😍 <b>80000+ zip file's Channel</b> 💔<br>━━━━━━━━━━━━━━━━━━━━<br><b>Benefits:</b><br>• 📁 All Dark Zip Files Available<br>• 🆕 New Files Added Daily<br>• 🔄 Forwarding Files is Allowed<br>🤔 Want to Buy?<br>🚀 Offers Are Live Now!"
T2 = "📽️ <b>AVAILABLE VIDEOS COLLECTION</b> 🎁<br>━━━━━━━━━━━━━━━━━━━━<br>REAL PRICE - <strike>2499/-</strike><br>OFFER PRICE - <b>499/-</b> ✅<br>VALIDITY ~ 6 MONTH ⌛"
T3 = "🥷 <b>VIP STUFF AVAILABLE</b> 🇨🇦<br>━━━━━━━━━━━━━━━━━━━━<br>Price: <strike>Rs. 299.00</strike> <b>Rs. 149.00</b>"
T4 = "🎀 <b>PREMIUM CUTIES LEAK</b> 🎀<br>━━━━━━━━━━━━━━━━━━━━<br>🤡 HELLO USER<br>Direct video - No Ads Sh#t 🚫<br>Price: <strike>Rs. 249.00</strike> <b>Rs. 99.00</b>"
T5 = "🔞 <b>PREMIUM DESI MAAL</b> 🍑<br>━━━━━━━━━━━━━━━━━━━━<br>Price: <strike>Rs. 259.00</strike> <b>Rs. 69.00</b>"
T6 = "🎬 <b>PREMIUM ADULT COLLECTION</b> ✅<br>━━━━━━━━━━━━━━━━━━━━<br>100% MONEY BACK GUARANTEE<br>Price: <strike>Rs. 799.00</strike> <b>Rs. 49.00</b>"

content = [
    {"type": "img", "text": T1, "media": "/static/1.jpg", "price": "₹999"},
    {"type": "vid", "text": T2, "media": "/static/1.mp4", "price": "₹499"},
    {"type": "img", "text": T3, "media": "/static/3.jpg", "price": "₹149"},
    {"type": "vid", "text": T4, "media": "/static/3.mp4", "price": "₹99"},
    {"type": "img", "text": T5, "media": "/static/2.jpg", "price": "₹69"},
    {"type": "vid", "text": T6, "media": "/static/1.mp4", "price": "₹49"}
]

HTML = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { background:#0b1626; color:#fff; font-family:sans-serif; margin:0; padding-top:70px; }
        .header { position:fixed; top:0; width:100%; background:#15253d; padding:15px; display:flex; justify-content:space-between; z-index:1000; border-bottom:1px solid #007bff; }
        .back-btn { cursor:pointer; color:#007bff; font-weight:bold; }
        .card { background:#15253d; border:1px solid #2c3e50; padding:15px; margin:15px auto; width:95%; max-width:400px; border-radius:15px; }
        img, video { width:100%; border-radius:10px; display:block; background:#000; min-height:200px; }
        .buy-btn { display:block; width:100%; background:#28a745; color:white; text-align:center; padding:12px; margin-top:10px; border-radius:8px; text-decoration:none; font-weight:bold; cursor:pointer; }
        .popup { display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.95); z-index:2000; justify-content:center; align-items:center; overflow-y:auto; }
        .qr-box { background:white; padding:20px; border-radius:15px; color:black; width:85%; max-width:320px; text-align:center; }
        input { width:90%; padding:10px; margin:8px 0; border:1px solid #ccc; border-radius:5px; }
        .verify-btn { background:#007bff; color:white; padding:12px; width:100%; border:none; border-radius:5px; cursor:pointer; font-weight:bold; }
    </style>
</head>
<body>
    <div class="header">
        <div class="back-btn" onclick="history.back()">⬅ Back</div>
        <div onclick="showPayment()">💰 Wallet: ₹0</div>
    </div>

    {% for i in content %}
    <div class="card">
        {% if i.type == 'vid' %}
            <video controls playsinline preload="metadata"><source src="{{ i.media }}" type="video/mp4"></video>
        {% else %}
            <img src="{{ i.media }}">
        {% endif %}
        <p style="margin-top:15px; font-size:15px; text-align:left;">{{ i.text|safe }}</p>
        <p style="font-size:18px; color:#ffc107; font-weight:bold;">Price: {{ i.price }}</p>
        <div class="buy-btn" onclick="showPayment()">BUY NOW</div>
    </div>
    {% endfor %}

    <div id="paymentPopup" class="popup" onclick="this.style.display='none'">
        <div class="qr-box" onclick="event.stopPropagation()">
            <img src="/static/qr.jpg" style="width:100%; border:2px solid #ccc;">
            <p><b>UPI ID:</b> paytm.s20glin@pty</p>
            <input type="text" id="txId" placeholder="Transaction ID (UTR)">
            <input type="number" id="amount" placeholder="Amount Paid">
            <button class="verify-btn" onclick="verify()">VERIFY PAYMENT</button>
            <p style="font-size:12px; color:red; margin-top:10px;">Screenshot le kar payment karein.</p>
        </div>
    </div>

    <script>
        function showPayment() { document.getElementById('paymentPopup').style.display = 'flex'; }
        function verify() {
            let tid = document.getElementById('txId').value;
            let amt = document.getElementById('amount').value;
            if(!tid || !amt) { alert("Dono details bharein!"); return; }
            alert("Verification request sent for ID: " + tid);
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML, content=content)

# Uptime Robot ke liye route
@app.route('/ping')
def ping():
    return "Alive", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
