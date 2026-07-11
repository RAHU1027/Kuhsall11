from flask import Flask, render_template_string
import os, threading, requests, time

app = Flask(__name__)

# --- 24/7 UPTIME ROBOT ---
def keep_alive():
    while True:
        try:
            requests.get("https://YOUR-APP-NAME.onrender.com") # Apna link yahan dalein
        except: pass
        time.sleep(300) 
threading.Thread(target=keep_alive, daemon=True).start()

# --- TUMHARA ORIGINAL DATA (Videos removed) ---
T1 = "😍 <b>80000+ zip file's Channel</b> 💔<br>━━━━━━━━━━━━━━━━━━━━<br>Price: <b>Rs. 999.00</b>"
T3 = "🥷 <b>VIP STUFF AVAILABLE</b> 🇨🇦<br>━━━━━━━━━━━━━━━━━━━━<br>Price: <b>Rs. 149.00</b>"
T4 = "🎀 <b>PREMIUM CUTIES LEAK</b> 🎀<br>━━━━━━━━━━━━━━━━━━━━<br>Price: <b>Rs. 99.00</b>"
T5 = "🔞 <b>PREMIUM DESI MAAL</b> 🍑<br>━━━━━━━━━━━━━━━━━━━━<br>Price: <b>Rs. 69.00</b>"
T6 = "🎬 <b>PREMIUM ADULT COLLECTION</b> ✅<br>━━━━━━━━━━━━━━━━━━━━<br>Price: <b>Rs. 49.00</b>"

content = [
    {"text": T1, "media": "/static/1.jpg", "price": "₹999"},
    {"text": T3, "media": "/static/3.jpg", "price": "₹149"},
    {"text": T4, "media": "/static/3.jpg", "price": "₹99"},
    {"text": T5, "media": "/static/2.jpg", "price": "₹69"},
    {"text": T6, "media": "/static/1.jpg", "price": "₹49"}
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
        .btn-pay { background:#28a745; color:white; padding:12px; text-align:center; border-radius:8px; font-weight:bold; cursor:pointer; margin-top:10px; width:100%; border:none; }
        .popup { display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.9); z-index:9999; justify-content:center; align-items:center; }
        .box { background:#15253d; padding:20px; border-radius:15px; width:85%; max-width:350px; text-align:center; border:1px solid #333; }
        .input-f { width:90%; padding:10px; margin:5px 0; border-radius:5px; border:none; }
    </style>
</head>
<body>
    <div class="header">
        <div>⚙️ Settings</div>
        <div>💰 Wallet: ₹0</div>
    </div>
    {% for i in content %}
    <div class="card">
        <img src="{{ i.media }}" style="width:100%; border-radius:10px;">
        <p style="margin-top:10px; font-size:14px;">{{ i.text|safe }}</p>
        <button class="btn-pay" onclick="showPayment()">BUY NOW</button>
    </div>
    {% endfor %}

    <div id="paymentPopup" class="popup" onclick="this.style.display='none'">
        <div class="box" onclick="event.stopPropagation()">
            <h3 style="color:#fff;">Pay and then add details ✍️</h3>
            <img src="/static/qr.jpg" style="width:100%; background:white; padding:5px; border-radius:10px;">
            <p style="font-size:12px; color:#aaa;">Download QR or scan to pay</p>
            <input type="text" placeholder="Telegram Username" class="input-f">
            <input type="text" placeholder="Transaction ID (UTR/URN)" class="input-f">
            <button class="btn-pay" onclick="alert('Details submitted! We will verify on Telegram.')">Join telegram 👍</button>
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
