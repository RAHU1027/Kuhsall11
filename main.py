from flask import Flask, render_template_string
import os

# --- WEB SERVICE ---
app = Flask(__name__)

# --- AAPKA ORIGINAL DATA ---
T1 = """😍 <b>80000+ zip file's Channel</b> 💔
<br>━━━━━━━━━━━━━━━━━━━━<br>
<b>Benefits:</b>
• 📁 All Dark Zip Files Available
• 🆕 New Files Added Daily
• 🔄 Forwarding Files is Allowed

🤔 Want to Buy?
🚀 Offers Are Live Now!

Price: <strike>Rs. 3,999.00</strike> <b>Rs. 999.00</b>
🔥 174 people bought this"""

T2 = """📽️ <b>AVAILABLE VIDEOS COLLECTION</b> 🎁
<br>━━━━━━━━━━━━━━━━━━━━<br>
REAL PRICE - <strike>2499/-</strike>
OFFER PRICE - <b>499/-</b> ✅

VALIDITY ~ 6 MONTH ⌛
PREMIUM QUALITY STUFF ✨

• INCEST ( D@RK )
• SLEEPING PILLS
• ONLY INDIAN

🔥 77 people bought this"""

T3 = """🥷 <b>VIP STUFF AVAILABLE</b> 🇨🇦
<br>━━━━━━━━━━━━━━━━━━━━<br>
Price: <strike>Rs. 299.00</strike> <b>Rs. 149.00</b>
🔥 94 people bought this"""

T4 = """🎀 <b>PREMIUM CUTIES LEAK</b> 🎀
<br>━━━━━━━━━━━━━━━━━━━━<br>
🤡 HELLO USER
Direct P#rn Video Channel 🫧
D#si Maal Ke Deewan 🥀 Ke Liye ✨
51000+ rare D#si le#ks ever.... 😍

Just pay and get entry... 💸
Direct video - No Ads Sh#t 🚫
Validity :- lifetime ✅

Price: <strike>Rs. 249.00</strike> <b>Rs. 99.00</b>
🔥 55 people bought this"""

T5 = """🔞 <b>PREMIUM DESI MAAL</b> 🍑
<br>━━━━━━━━━━━━━━━━━━━━<br>
Price: <strike>Rs. 259.00</strike> <b>Rs. 69.00</b>
🔥 314 people bought this"""

T6 = """🎬 <b>PREMIUM ADULT COLLECTION UPDATED</b> ✅
<br>━━━━━━━━━━━━━━━━━━━━<br>
MAA-BETA 🖤
BAAP-BETI 🖤
BHAI-BEHEN 🖤
DESI CHOTI BACHIYA 💔
AUNTY AND BHABHI 💔
INSTAGRAM REELS STARS 💔
ONLYFANS FOREIGN 💔
HARDCORE AND FOREPLAY 💔

AND ALL CATEGORIES IN ONE PACKAGE ✊

VALIDITY - 6 MONTH 🤝

🔥🔥 100% MONEY BACK GUARANTEE IF NOT SATISFIED

Price: <strike>Rs. 799.00</strike> <b>Rs. 49.00</b>
🔥 258 people bought this"""

data_list = [T1, T2, T3, T4, T5, T6]

# --- WEBSITE DESIGN (MOBILE OPTIMIZED) ---
HTML = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { background:#0b1626; color:#fff; font-family:sans-serif; text-align:center; padding:10px; margin:0; }
        .card { background:#15253d; border:2px solid #007bff; padding:15px; margin:15px auto; width:95%; max-width:400px; border-radius:15px; text-align:center; box-sizing:border-box; }
        .btn-group { display:flex; gap:10px; margin-top:15px; }
        .btn { flex:1; padding:12px; border:none; border-radius:8px; font-weight:bold; cursor:pointer; text-decoration:none; color:white; font-size:14px; }
    </style>
</head>
<body>
    {% for t in data %}
    <div class="card">
        <p style="text-align:left; font-size:15px;">{{ t|safe }}</p>
        <div class="btn-group">
            <button class="btn" style="background:#007bff;" onclick="document.getElementById('m{{loop.index}}').style.display='block'">PAYMENT (QR)</button>
            <a href="#" class="btn" style="background:#28a745;">DOWNLOAD</a>
        </div>
        <div id="m{{loop.index}}" style="display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.9); z-index:999;" onclick="this.style.display='none'">
            <img src="/static/qr.jpg" style="max-width:90%; margin-top:20%; border:5px solid white;">
        </div>
    </div>
    {% endfor %}
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML, data=data_list)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
