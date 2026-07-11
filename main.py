from flask import Flask, render_template_string
import os, threading, requests, time

app = Flask(__name__)

# --- 24/7 UPTIME ROBOT ---
def keep_alive():
    while True:
        try:
            # Apni website ka URL yahan zaroor daalna
            requests.get("https://YOUR-APP-NAME.onrender.com")
        except: pass
        time.sleep(300)
threading.Thread(target=keep_alive, daemon=True).start()

# --- TUMHARA ORIGINAL DATA ---
T1 = "😍 <b>80000+ zip file's Channel</b> 💔<br>━━━━━━━━━━━━━━━━━━━━<br><b>Benefits:</b><br>• 📁 All Dark Zip Files Available<br>• 🆕 New Files Added Daily<br>• 🔄 Forwarding Files is Allowed<br>🤔 Want to Buy?<br>🚀 Offers Are Live Now!<br>Price: <strike>Rs. 3,999.00</strike> <b>Rs. 999.00</b><br>🔥 174 people bought this"
T2 = "📽️ <b>AVAILABLE VIDEOS COLLECTION</b> 🎁<br>━━━━━━━━━━━━━━━━━━━━<br>REAL PRICE - <strike>2499/-</strike><br>OFFER PRICE - <b>499/-</b> ✅<br>VALIDITY ~ 6 MONTH ⌛<br>PREMIUM QUALITY STUFF ✨<br>• INCEST ( D@RK )<br>• SLEEPING PILLS<br>• ONLY INDIAN<br>🔥 77 people bought this"
T3 = "🥷 <b>VIP STUFF AVAILABLE</b> 🇨🇦<br>━━━━━━━━━━━━━━━━━━━━<br>Price: <strike>Rs. 299.00</strike> <b>Rs. 149.00</b><br>🔥 94 people bought this"
T4 = "🎀 <b>PREMIUM CUTIES LEAK</b> 🎀<br>━━━━━━━━━━━━━━━━━━━━<br>🤡 HELLO USER<br>Direct P#rn Video Channel 🫧<br>D#si Maal Ke Deewan 🥀 Ke Liye ✨<br>51000+ rare D#si le#ks ever.... 😍<br>Just pay and get entry... 💸<br>Direct video - No Ads Sh#t 🚫<br>Validity :- lifetime ✅<br>Price: <strike>Rs. 249.00</strike> <b>Rs. 99.00</b><br>🔥 55 people bought this"
T5 = "🔞 <b>PREMIUM DESI MAAL</b> 🍑<br>━━━━━━━━━━━━━━━━━━━━<br>Price: <strike>Rs. 259.00</strike> <b>Rs. 69.00</b><br>🔥 314 people bought this"
T6 = "🎬 <b>PREMIUM ADULT COLLECTION UPDATED</b> ✅<br>━━━━━━━━━━━━━━━━━━━━<br>MAA-BETA 🖤<br>BAAP-BETI 🖤<br>BHAI-BEHEN 🖤<br>DESI CHOTI BACHIYA 💔<br>AUNTY AND BHABHI 💔<br>INSTAGRAM REELS STARS 💔<br>ONLYFANS FOREIGN 💔<br>HARDCORE AND FOREPLAY 💔<br>AND ALL CATEGORIES IN ONE PACKAGE ✊<br>VALIDITY - 6 MONTH 🤝<br>🔥🔥 100% MONEY BACK GUARANTEE IF NOT SATISFIED<br>Price: <strike>Rs. 799.00</strike> <b>Rs. 49.00</b><br>🔥 258 people bought this"

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
        .header { position:fixed; top:0; width:100%; background:#15253d; padding:15px; display:flex; justify-content:space-between; border-bottom:1px solid #007bff; z-index:1000; }
        .card { background:#15253d; border:1px solid #2c3e50; padding:15px; margin:15px auto; width:95%; max-width:400px; border-radius:15px; }
        .btn-pay { background:#28a745; color:white; padding:12px; text-align:center; border-radius:8px; font-weight:bold; cursor:pointer; margin-top:10px; }
        .popup { display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.9); z-index:9999; justify-content:center; align-items:center; }
        .box { background:#15253d; padding:20px; border-radius:15px; width:85%; max-width:350px; text-align:center; border:1px solid #333; }
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
            <img src="{{ i.media }}" style="width:100%; border-radius:10px;">
        {% endif %}
        <p style="margin-top:10px; font-size:14px;">{{ i.text|safe }}</p>
        <div class="btn-pay" onclick="showPayment()">PAYMENT (QR)</div>
    </div>
    {% endfor %}

    <div id="paymentPopup" class="popup" onclick="this.style.display='none'">
        <div class="box" onclick="event.stopPropagation()">
            <h3>Pay ₹119 and then add details ✍️</h3>
            <img src="/static/qr.jpg" style="width:100%; background:white; padding:5px; border-radius:10px;">
            <p>Download qr 📲 or Tap to copy UPI Id</p>
            <input type="text" placeholder="eg. @username" style="width:90%; padding:10px; margin:5px 0;">
            <input type="text" placeholder="eg. Transaction ID" style="width:90%; padding:10px; margin:5px 0;">
            <button class="btn-pay" style="width:100%; border:none;">Join telegram 👍</button>
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
