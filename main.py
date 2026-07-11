from flask import Flask, render_template_string
import os

# --- WEB SERVICE ---
app = Flask(__name__)

# --- ORIGINAL DATA ---
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

# --- WEBSITE DESIGN ---
HTML = """
<!DOCTYPE html>
<html>
<body style="background:#000; color:#fff; font-family:sans-serif; text-align:center;">
    {% for t in data %}
    <div style="border:1px solid #333; padding:20px; margin:20px auto; max-width:400px; border-radius:10px;">
        <p>{{ t|safe }}</p>
        
        <div style="display:flex; gap:10px; margin-top:15px;">
            <button style="flex:1; background:#007bff; color:white; padding:10px; border:none; border-radius:5px; cursor:pointer;" onclick="document.getElementById('m{{loop.index}}').style.display='block'">PAYMENT (QR)</button>
            <a href="#" style="flex:1; background:#28a745; color:white; padding:10px; text-decoration:none; border-radius:5px;">DOWNLOAD</a>
        </div>
        
        <div id="m{{loop.index}}" style="display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.9); z-index:999;" onclick="this.style.display='none'">
            <img src="/static/qr.png" style="max-width:300px; margin-top:20%;">
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
