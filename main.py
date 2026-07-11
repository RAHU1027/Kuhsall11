from flask import Flask, render_template_string
import os
import threading
import requests
import time

app = Flask(__name__)

# --- 24/7 KEEP ALIVE SYSTEM ---
def keep_alive():
    while True:
        try:
            # Apni website ka link yahan dalna: https://your-app.onrender.com
            requests.get("https://YOUR-APP-LINK.onrender.com") 
        except: pass
        time.sleep(300) 

threading.Thread(target=keep_alive, daemon=True).start()

# --- DATA ---
T1 = "😍 <b>80000+ zip file's Channel</b> 💔<br>━━━━━━━━━━━━━━━━━━━━<br><b>Benefits:</b><br>• 📁 All Dark Zip Files Available<br>• 🆕 New Files Added Daily<br>• 🔄 Forwarding Files is Allowed<br>🤔 Want to Buy?<br>🚀 Offers Are Live Now!<br>Price: <strike>Rs. 3,999.00</strike> <b>Rs. 999.00</b>"
T2 = "📽️ <b>AVAILABLE VIDEOS COLLECTION</b> 🎁<br>━━━━━━━━━━━━━━━━━━━━<br>REAL PRICE - <strike>2499/-</strike><br>OFFER PRICE - <b>499/-</b> ✅<br>VALIDITY ~ 6 MONTH ⌛"
T3 = "🥷 <b>VIP STUFF AVAILABLE</b> 🇨🇦<br>━━━━━━━━━━━━━━━━━━━━<br>Price: <strike>Rs. 299.00</strike> <b>Rs. 149.00</b>"
T4 = "🎀 <b>PREMIUM CUTIES LEAK</b> 🎀<br>━━━━━━━━━━━━━━━━━━━━<br>🤡 HELLO USER<br>Direct video - No Ads Sh#t 🚫<br>Price: <strike>Rs. 249.00</strike> <b>Rs. 99.00</b>"
T5 = "🔞 <b>PREMIUM DESI MAAL</b> 🍑<br>━━━━━━━━━━━━━━━━━━━━<br>Price: <strike>Rs. 259.00</strike> <b>Rs. 69.00</b>"
T6 = "🎬 <b>PREMIUM ADULT COLLECTION</b> ✅<br>━━━━━━━━━━━━━━━━━━━━<br>100% MONEY BACK GUARANTEE<br>Price: <strike>Rs. 799.00</strike> <b>Rs. 49.00</b>"

content = [
    {"type": "img", "text": T1, "media": "/static/1.jpg"},
    {"type": "vid", "text": T2, "media": "/static/1.mp4"},
    {"type": "img", "text": T3, "media": "/static/3.jpg"},
    {"type": "vid", "text": T4, "media": "/static/3.mp4"},
    {"type": "img", "text": T5, "media": "/static/2.jpg"},
    {"type": "vid", "text": T6, "media": "/static/1.mp4"}
]

HTML = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { background:#0b1626; color:#fff; font-family:sans-serif; margin:0; padding-top:70px; }
        .header { position:fixed; top:0; width:100%; background:#15253d; padding:15px; display:flex; justify-content:space-between; z-index:1000; border-bottom:1px solid #007bff; font-weight:bold; }
        .card { background:#15253d; border:1px solid #2c3e50; padding:15px; margin:15px auto; width:95%; max-width:400px; border-radius:15px; }
        img, video { width:100%; border-radius:10px; display:block; background:#000; min-height:200px; }
        .btn-group { display:flex; gap:10px; margin-top:15px; }
        .btn { flex:1; padding:12px; text-align:center; border-radius:8px; font-weight:bold; cursor:pointer; text-decoration:none; color:white; }
        .pay-btn { background:#007bff; }
        .dl-btn { background:#28a745; }
        .popup { display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.95); z-index:9999; justify-content:center; align-items:center; }
        .qr-box { background:white; padding:20px; border-radius:15px; color:black; text-align:center; width:85%; max-width:320px; }
    </style>
</head>
<body>
    <div class="header">
        <div onclick="showPayment()">➕ Add Payment</div>
        <div>💰 Wallet: ₹0</div>
    </div>
    {% for i in content %}
    <div class="card">
        {% if i.type == 'vid' %}
            <video controls playsinline preload="metadata"><source src="{{ i.media }}" type="video/mp4"></video>
        {% else %}
            <img src="{{ i.media }}">
        {% endif %}
        <p style="margin-top:15px; font-size:15px;">{{ i.text|safe }}</p>
        <div class="btn-group">
            <div class="btn pay-btn" onclick="showPayment()">PAYMENT (QR)</div>
            <a href="#" class="btn dl-btn">DOWNLOAD</a>
        </div>
    </div>
    {% endfor %}

    <div id="paymentPopup" class="popup" onclick="this.style.display='none'">
        <div class="qr-box" onclick="event.stopPropagation()">
            <img src="/static/qr.jpg" style="width:100%; border:2px solid #ccc;">
            <p><b>UPI ID:</b> paytm.s20glin@pty</p>
            <p style="font-size:12px; color:red;">Screenshot le kar payment karein.</p>
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
    return render_template_string(HTML, content=content)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
