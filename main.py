import os
from flask import Flask

# --- CONFIG ---
PATH = "./" 

# --- WEB SERVICE FOR 24/7 ---
app = Flask(__name__)

# Ye function aapka pura content browser mein display karega
@app.route('/')
def home():
    # T1 se T6 tak ka content waisa hi hai jaisa aapka tha
    html_content = f"""
    <div style="font-family: sans-serif; line-height: 1.6; max-width: 600px; margin: auto;">
        <pre>{T1}</pre><hr>
        <pre>{T2}</pre><hr>
        <pre>{T3}</pre><hr>
        <pre>{T4}</pre><hr>
        <pre>{T5}</pre><hr>
        <pre>{T6}</pre>
    </div>
    """
    return html_content

@app.route('/ping')
def ping(): return "Site is active", 200

# --- EXACT VIDEO DATA (Aapka original text) ---
T1 = """😍 80000+ zip file's Channel 💔
━━━━━━━━━━━━━━━━━━━━
Benefits:
• 📁 All Dark Zip Files Available
• 🆕 New Files Added Daily
• 🔄 Forwarding Files is Allowed

🤔 Want to Buy?
🚀 Offers Are Live Now!

Price: Rs. 3,999.00 Rs. 999.00
🔥 174 people bought this"""

T2 = """📽️ AVAILABLE VIDEOS COLLECTION 🎁
━━━━━━━━━━━━━━━━━━━━
REAL PRICE - 2499/-
OFFER PRICE - 499/- ✅

VALIDITY ~ 6 MONTH ⌛
PREMIUM QUALITY STUFF ✨

• INCEST ( D@RK )
• SLEEPING PILLS
• ONLY INDIAN

🔥 77 people bought this"""

T3 = """🥷 VIP STUFF AVAILABLE 🇨🇦
━━━━━━━━━━━━━━━━━━━━
Price: Rs. 299.00 Rs. 149.00
🔥 94 people bought this"""

T4 = """🎀 PREMIUM CUTIES LEAK 🎀
━━━━━━━━━━━━━━━━━━━━
🤡 HELLO USER
Direct P#rn Video Channel 🫧
D#si Maal Ke Deewan 🥀 Ke Liye ✨
51000+ rare D#si le#ks ever.... 😍

Just pay and get entry... 💸
Direct video - No Ads Sh#t 🚫
Validity :- lifetime ✅

Price: Rs. 249.00 Rs. 99.00
🔥 55 people bought this"""

T5 = """🔞 PREMIUM DESI MAAL 🍑
━━━━━━━━━━━━━━━━━━━━
Price: Rs. 259.00 Rs. 69.00
🔥 314 people bought this"""

T6 = """🎬 PREMIUM ADULT COLLECTION UPDATED ✅
━━━━━━━━━━━━━━━━━━━━
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

Price: Rs. 799.00 Rs. 49.00
🔥 258 people bought this"""

# --- STARTING ---
if __name__ == "__main__":
    # Website server start
    print("🚀 WEBSITE IS LIVE!")
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
