from flask import Flask, render_template_string
import os

app = Flask(__name__)

# --- TUMHARA ORIGINAL DATA ---
T1 = "😍 <b>80000+ zip file's Channel</b> 💔<br>━━━━━━━━━━━━━━━━━━━━<br><b>Benefits:</b><br>• 📁 All Dark Zip Files Available<br>• 🆕 New Files Added Daily<br>• 🔄 Forwarding Files is Allowed<br>🤔 Want to Buy?<br>🚀 Offers Are Live Now!<br>Price: <strike>Rs. 3,999.00</strike> <b>Rs. 999.00</b><br>🔥 174 people bought this"
T2 = "📽️ <b>AVAILABLE VIDEOS COLLECTION</b> 🎁<br>━━━━━━━━━━━━━━━━━━━━<br>REAL PRICE - <strike>2499/-</strike><br>OFFER PRICE - <b>499/-</b> ✅<br>VALIDITY ~ 6 MONTH ⌛<br>PREMIUM QUALITY STUFF ✨<br>• INCEST ( D@RK )<br>• SLEEPING PILLS<br>• ONLY INDIAN<br>🔥 77 people bought this"
T3 = "🥷 <b>VIP STUFF AVAILABLE</b> 🇨🇦<br>━━━━━━━━━━━━━━━━━━━━<br>Price: <strike>Rs. 299.00</strike> <b>Rs. 149.00</b><br>🔥 94 people bought this"
T4 = "🎀 <b>PREMIUM CUTIES LEAK</b> 🎀<br>━━━━━━━━━━━━━━━━━━━━<br>🤡 HELLO USER<br>Direct P#rn Video Channel 🫧<br>D#si Maal Ke Deewan 🥀 Ke Liye ✨<br>51000+ rare D#si le#ks ever.... 😍<br>Just pay and get entry... 💸<br>Direct video - No Ads Sh#t 🚫<br>Validity :- lifetime ✅<br>Price: <strike>Rs. 249.00</strike> <b>Rs. 99.00</b><br>🔥 55 people bought this"
T5 = "🔞 <b>PREMIUM DESI MAAL</b> 🍑<br>━━━━━━━━━━━━━━━━━━━━<br>Price: <strike>Rs. 259.00</strike> <b>Rs. 69.00</b><br>🔥 314 people bought this"
T6 = "🎬 <b>PREMIUM ADULT COLLECTION UPDATED</b> ✅<br>━━━━━━━━━━━━━━━━━━━━<br>MAA-BETA 🖤<br>BAAP-BETI 🖤<br>BHAI-BEHEN 🖤<br>DESI CHOTI BACHIYA 💔<br>AUNTY AND BHABHI 💔<br>INSTAGRAM REELS STARS 💔<br>ONLYFANS FOREIGN 💔<br>HARDCORE AND FOREPLAY 💔<br>AND ALL CATEGORIES IN ONE PACKAGE ✊<br>VALIDITY - 6 MONTH 🤝<br>🔥🔥 100% MONEY BACK GUARANTEE IF NOT SATISFIED<br>Price: <strike>Rs. 799.00</strike> <b>Rs. 49.00</b><br>🔥 258 people bought this"

# Original Data ko sequence (Photo -> Video) mein set kiya
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
        .header { position:fixed; top:0; width:100%; background:#15253d; padding:15px; display:flex; justify-content:space-between; z-index:1000; border-bottom:1px solid #007bff; box-sizing:border-box; font-weight:bold; }
        .card { background:#15253d; border:1px solid #2c3e50; padding:15px; margin:15px auto; width:95%; max-width:400px; border-radius:15px; box-sizing:border-box; }
        video, img { width:100%; border-radius:10px; display:block; background:#000; }
    </style>
</head>
<body>
    <div class="header">
        <div onclick="alert('Settings Panel')">⚙️ Settings</div>
        <div onclick="alert('Wallet Balance: ₹0')">💰 Wallet: ₹0</div>
    </div>

    {% for i in content %}
    <div class="card">
        {% if i.type == 'vid' %}
            <video controls playsinline preload="metadata">
                <source src="{{ i.media }}" type="video/mp4">
            </video>
        {% else %}
            <img src="{{ i.media }}" loading="lazy">
        {% endif %}
        <p style="margin-top:15px; font-size:15px; text-align:left;">{{ i.text|safe }}</p>
    </div>
    {% endfor %}
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML, content=content)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
