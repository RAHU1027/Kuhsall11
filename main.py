from flask import Flask, render_template_string
import os

app = Flask(__name__)

# --- AAPKA ORIGINAL DATA (NO CHANGES) ---
T1 = "😍 <b>80000+ zip file's Channel</b> 💔<br>━━━━━━━━━━━━━━━━━━━━<br><b>Benefits:</b><br>• 📁 All Dark Zip Files Available<br>• 🆕 New Files Added Daily<br>• 🔄 Forwarding Files is Allowed<br>🤔 Want to Buy?<br>🚀 Offers Are Live Now!<br>Price: <strike>Rs. 3,999.00</strike> <b>Rs. 999.00</b><br>🔥 174 people bought this"
T2 = "📽️ <b>AVAILABLE VIDEOS COLLECTION</b> 🎁<br>━━━━━━━━━━━━━━━━━━━━<br>REAL PRICE - <strike>2499/-</strike><br>OFFER PRICE - <b>499/-</b> ✅<br>VALIDITY ~ 6 MONTH ⌛<br>PREMIUM QUALITY STUFF ✨<br>• INCEST ( D@RK )<br>• SLEEPING PILLS<br>• ONLY INDIAN<br>🔥 77 people bought this"
T3 = "🥷 <b>VIP STUFF AVAILABLE</b> 🇨🇦<br>━━━━━━━━━━━━━━━━━━━━<br>Price: <strike>Rs. 299.00</strike> <b>Rs. 149.00</b><br>🔥 94 people bought this"
T4 = "🎀 <b>PREMIUM CUTIES LEAK</b> 🎀<br>━━━━━━━━━━━━━━━━━━━━<br>🤡 HELLO USER<br>Direct P#rn Video Channel 🫧<br>D#si Maal Ke Deewan 🥀 Ke Liye ✨<br>51000+ rare D#si le#ks ever.... 😍<br>Just pay and get entry... 💸<br>Direct video - No Ads Sh#t 🚫<br>Validity :- lifetime ✅<br>Price: <strike>Rs. 249.00</strike> <b>Rs. 99.00</b><br>🔥 55 people bought this"
T5 = "🔞 <b>PREMIUM DESI MAAL</b> 🍑<br>━━━━━━━━━━━━━━━━━━━━<br>Price: <strike>Rs. 259.00</strike> <b>Rs. 69.00</b><br>🔥 314 people bought this"
T6 = "🎬 <b>PREMIUM ADULT COLLECTION UPDATED</b> ✅<br>━━━━━━━━━━━━━━━━━━━━<br>MAA-BETA 🖤<br>BAAP-BETI 🖤<br>BHAI-BEHEN 🖤<br>DESI CHOTI BACHIYA 💔<br>AUNTY AND BHABHI 💔<br>INSTAGRAM REELS STARS 💔<br>ONLYFANS FOREIGN 💔<br>HARDCORE AND FOREPLAY 💔<br>AND ALL CATEGORIES IN ONE PACKAGE ✊<br>VALIDITY - 6 MONTH 🤝<br>🔥🔥 100% MONEY BACK GUARANTEE IF NOT SATISFIED<br>Price: <strike>Rs. 799.00</strike> <b>Rs. 49.00</b><br>🔥 258 people bought this"

data_list = [T1, T2, T3, T4, T5, T6]

# --- DESIGN ---
HTML = """
<!DOCTYPE html>
<html>
<body style="background:#0b1626; color:#fff; font-family:sans-serif; text-align:center; padding:20px;">
    {% for t in data %}
    <div style="background:#15253d; border:2px solid #007bff; padding:20px; margin:20px auto; max-width:400px; border-radius:15px; text-align:center;">
        <p style="text-align:left;">{{ t|safe }}</p>
        <div style="display:flex; gap:10px; margin-top:15px;">
            <button style="flex:1; background:#007bff; color:white; padding:12px; border:none; border-radius:8px; font-weight:bold; cursor:pointer;" onclick="document.getElementById('m{{loop.index}}').style.display='block'">PAYMENT (QR)</button>
            <a href="#" style="flex:1; background:#28a745; color:white; padding:12px; text-decoration:none; border-radius:8px; font-weight:bold;">DOWNLOAD</a>
        </div>
        <div id="m{{loop.index}}" style="display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.9); z-index:999;" onclick="this.style.display='none'">
            <img src="/static/qr.jpg" style="max-width:300px; margin-top:20%; border:5px solid white;">
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
