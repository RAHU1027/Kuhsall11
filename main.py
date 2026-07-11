from flask import Flask, render_template_string
import os

# --- WEB SERVICE ---
app = Flask(__name__)

# --- AAPKA ORIGINAL DATA (NO CHANGES) ---
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

# --- DESIGN (Screenshot style) ---
HTML = """
<!DOCTYPE html>
<html>
<head><meta name="viewport" content="width=device-width, initial-scale=1.0"></head>
<body style="background:#0b1626; color:#fff; font-family:sans-serif; text-align:center; padding:20px;">
    
    <h1 style="color:#f39c12; margin-bottom:20px;">peter adult store</h1>
    <a href="#" style="background:#0056b3; color:white; padding:15px 50px; border-radius:8px; text-decoration:none; display:inline-block; font-weight:bold; margin-bottom:30px;">DEMO VIDEOS</a>

    {% for t in data %}
    <div style="background:#15253d; border:2px solid #007bff; padding:20px; margin:15px auto; max-width:400px; border-radius:15px; text-align:left;">
        <p style="margin-bottom:20px;">{{ t|safe }}</p>
        <button style="background:#8e6a00; color:white; border:none; padding:15px; width:100%; border-radius:10px; font-size:18px; font-weight:bold; cursor:pointer;">BUY NOW</button>
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
