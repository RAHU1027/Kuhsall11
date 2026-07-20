from flask import Flask, render_template_string, request
import sqlite3, re

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('payments.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS transactions 
                 (tid TEXT PRIMARY KEY, amount INTEGER)''')
    conn.commit()
    conn.close()
init_db()

# Aapka original data waisa ka waisa, sath mein 'price_val' add kiya hai wallet tracking ke liye
content = [
    {
        "text": "😍 <b>80000+ zip file's Channel</b> 💔<br>━━━━━━━━━━━━━━━━━━━━<br>Benefits:<br>• 📁 All Dark Zip Files Available<br>• 🆕 New Files Added Daily<br>• 🔄 Forwarding Files is Allowed<br><br>🤔 Want to Buy?<br>🚀 Offers Are Live Now!", 
        "media_type": "img",
        "media": "/static/1.jpg", 
        "price_val": 799,
        "price": "Rs. 799.00 <span style='text-decoration:line-through; color:gray; font-size:12px;'>Rs. 3,999.00</span><br><span style='color:red;'>🔥 174 people bought this</span>"
    },
    {
        "text": "🔞 <b>50K+ MMS LEAK IN JUST ₹120/-</b> 💦<br>━━━━━━━━━━━━━━━━━━━━<br>🔥 ALL TYPE AVAILABLE<br>✨ 90% OFF SALE<br>👇 CLICK SHOP NOW 👇", 
        "media_type": "video",
        "media": "/static/1.mp4", 
        "price_val": 120,
        "price": "Rs. 120.00 <span style='text-decoration:line-through; color:gray; font-size:12px;'>Rs. 249.00</span><br><span style='color:red;'>🔥 450+ people bought this</span>"
    },
    {
        "text": "🥷 <b>VIP STUFF AVAILABLE</b> 🇨🇦<br>━━━━━━━━━━━━━━━━━━━━", 
        "media_type": "img",
        "media": "/static/3.jpg", 
        "price_val": 69,
        "price": "Rs. 69.00 <span style='text-decoration:line-through; color:gray; font-size:12px;'>Rs. 199.00</span><br><span style='color:red;'>🔥 94 people bought this</span>"
    },
    {
        "text": "🔞 <b>PREMIUM DESI MAAL</b> 🍑<br>━━━━━━━━━━━━━━━━━━━━", 
        "media_type": "video",
        "media": "/static/2.mp4", 
        "price_val": 99,
        "price": "Rs. 99.00 <span style='text-decoration:line-through; color:gray; font-size:12px;'>Rs. 499.00</span><br><span style='color:red;'>🔥 314 people bought this</span>"
    },
    {
        "text": "🔞 <b>PREMIUM DESI MAAL 2</b> 🍑<br>━━━━━━━━━━━━━━━━━━━━", 
        "media_type": "img",
        "media": "/static/2.jpg", 
        "price_val": 99,
        "price": "Rs. 99.00 <span style='text-decoration:line-through; color:gray; font-size:12px;'>Rs. 399.00</span><br><span style='color:red;'>🔥 314 people bought this</span>"
    }
]

HTML = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        /* Modern dark gradient background & unique bold large capital letters */
        body { background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%); color:#fff; font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin:0; padding-top:70px; min-height: 100vh; text-transform: uppercase; }
        .header { position:fixed; top:0; width:100%; background:rgba(15, 23, 42, 0.95); backdrop-filter: blur(10px); padding:10px; display:flex; justify-content:space-between; align-items:center; z-index:1000; box-sizing:border-box; border-bottom:1px solid rgba(255,255,255,0.1); }
        .nav-btn { font-size:11px; font-weight:900; letter-spacing: 1px; color:#38bdf8; padding:6px 10px; border-radius:5px; background:rgba(56,189,248,0.1); border:1px solid rgba(56,189,248,0.3); white-space:nowrap; cursor:pointer; }
        .card { background:rgba(30, 41, 59, 0.7); backdrop-filter: blur(5px); padding:15px; margin:15px auto; width:90%; border-radius:15px; border:1px solid rgba(255,255,255,0.08); box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3); }
        
        /* Unique Bold Large Typography Styling */
        .card p { font-size: 13px; font-weight: 800; letter-spacing: 0.5px; line-height: 1.5; }
        .card b { font-size: 16px; letter-spacing: 1px; color: #f8fafc; }

        .btn-demo { background:#ffc107; color:black; width:100%; padding:10px; margin-bottom:10px; border:none; border-radius:5px; font-weight:900; font-size:12px; letter-spacing:1px; cursor:pointer; }
        .btn-buy { background:#28a745; color:white; width:100%; padding:10px; border:none; border-radius:5px; font-weight:900; font-size:12px; letter-spacing:1px; cursor:pointer; }
        .popup { display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.85); backdrop-filter: blur(8px); z-index:9999; justify-content:center; align-items:center; }
        .box { background:#1e293b; padding:20px; border-radius:15px; width:85%; border:1px solid rgba(255,255,255,0.1); text-align:center; position:relative; box-shadow: 0 10px 25px rgba(0,0,0,0.5); }
        .box h3 { font-size: 16px; font-weight: 900; letter-spacing: 1px; }
        .back-btn { position:absolute; top:10px; right:10px; color:#ff4d4d; cursor:pointer; font-weight:900; font-size:11px; letter-spacing: 1px; }
        .menu { display:none; position:absolute; top:45px; left:10px; background:#1e293b; border-radius:10px; padding:10px; border:1px solid rgba(255,255,255,0.1); width:120px; z-index:1001; box-shadow: 0 5px 15px rgba(0,0,0,0.3); font-size: 11px; font-weight: 800; }
        
        /* Welcome Overlay */
        #welcome-overlay { position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.9); z-index:10000; display:flex; justify-content:center; align-items:center; text-align:center; padding:20px; }
        #welcome-overlay h2 { font-size: 20px; font-weight: 900; letter-spacing: 1px; color: #fff; }
        #welcome-overlay p { font-size: 11px; font-weight: 700; color:#aaa; letter-spacing: 0.5px; }
        .ok-btn { background:#007bff; color:white; padding:12px 30px; border:none; border-radius:25px; font-weight:900; font-size:12px; letter-spacing:1px; cursor:pointer; margin-top:20px; }
    </style>
</head>
<body>
    <div id="welcome-overlay">
        <div>
            <h2>WELCOME TO PREMIUM ACCESS</h2>
            <p>CATEGORY WISE CONTENT NICHE DIYA GAYA HAI.<br>PAYMENT KE LIYE 'UNLOCK PREMIUM' PAR CLICK KAREIN.</p>
            <button class="ok-btn" onclick="document.getElementById('welcome-overlay').style.display='none'">OK, GOT IT</button>
        </div>
    </div>

    <div class="header">
        <div style="position:relative;">
            <div class="nav-btn" onclick="document.getElementById('m').style.display='block'">⚙️ SETTINGS</div>
            <div id="m" class="menu" onclick="this.style.display='none'">
                <div style="padding:5px; cursor:pointer;">👤 PROFILE</div>
                <div style="padding:5px; cursor:pointer;">💳 ADD FUNDS</div>
                <div style="padding:5px; cursor:pointer;">🎧 SUPPORT</div>
            </div>
        </div>
        <div class="nav-btn" style="border-color:#28a745; color:#28a745;" id="wallet-display">💰 WALLET: ₹{{ total_wallet }}</div>
    </div>

    {% for i in content %}
    <div class="card">
        {% if i.media_type == 'video' %}
            <video width="100%" controls style="border-radius:10px;">
                <source src="{{ i.media }}" type="video/mp4">
            </video>
        {% else %}
            <img src="{{ i.media }}" style="width:100%; border-radius:10px;">
        {% endif %}
        <p>{{ i.text|safe }}</p>
        <p style="color:#ffc107; font-weight:900; font-size:14px;">PRICE: {{ i.price|safe }}</p>
        <button class="btn-demo" onclick="window.open('https://t.me/+JBVaDAvX-To1NzRl')">FREE DEMO</button>
        <button class="btn-buy" onclick="showPopup('{{ i.price_val }}')">UNLOCK PREMIUM</button>
    </div>
    {% endfor %}

    <div id="p" class="popup">
        <div class="box" id="content-box">
            <div class="back-btn" onclick="closePopup()">BACK TO HOME</div>
            <h3>PAY & ADD DETAILS ✍️</h3>
            <div id="timer" style="color:yellow; font-weight:900; font-size:15px; margin-bottom:10px;">04:00</div>
            <img src="/static/qr.jpg" style="width:100%; background:white; padding:5px; border-radius:5px;">
            <input id="tid" placeholder="12 DIGIT TRANSACTION ID" style="width:90%; padding:10px; margin:5px; background:#0f172a; border:1px solid rgba(255,255,255,0.2); color:#fff; border-radius:5px; font-weight:bold; text-align:center; text-transform:uppercase;"><br>
            <button class="btn-buy" onclick="verify()">SUBMIT DETAILS</button>
        </div>
    </div>

    <script>
        let timerInterval;
        let currentPrice = 0;
        function showPopup(price) { 
            currentPrice = price;
            document.getElementById('p').style.display = 'flex'; 
            startTimer(240); 
        }
        function closePopup() { document.getElementById('p').style.display = 'none'; clearInterval(timerInterval); }
        function startTimer(duration) {
            clearInterval(timerInterval);
            let timer = duration, m, s;
            timerInterval = setInterval(function () {
                m = parseInt(timer / 60, 10); s = parseInt(timer % 60, 10);
                document.getElementById('timer').textContent = "0" + m + ":" + (s < 10 ? "0" + s : s);
                if (--timer < 0) { closePopup(); }
            }, 1000);
        }
        function verify() {
            let tid = document.getElementById('tid').value;
            fetch('/verify', {
                method: 'POST',
                headers: {'Content-Type': 'application/x-www-form-urlencoded'},
                body: 'tid=' + tid + '&amount=' + currentPrice
            }).then(r => r.json()).then(data => {
                if(data.success) {
                    clearInterval(timerInterval);
                    document.getElementById('content-box').innerHTML = data.html;
                    document.getElementById('wallet-display').textContent = "💰 WALLET: ₹" + data.new_wallet;
                } else {
                    alert(data.message);
                }
            });
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    conn = sqlite3.connect('payments.db')
    c = conn.cursor()
    c.execute("SELECT SUM(amount) FROM transactions")
    res = c.fetchone()[0]
    total_wallet = res if res else 0
    conn.close()
    return render_template_string(HTML, content=content, total_wallet=total_wallet)

@app.route('/verify', methods=['POST'])
def verify():
    tid = request.form.get('tid', '').strip()
    try:
        amount = int(request.form.get('amount', '0'))
    except ValueError:
        amount = 0

    if not re.match(r'^\d{12}$', tid):
        return {"success": False, "message": "❌ INVALID TID! MUST BE 12 DIGITS."}
    
    conn = sqlite3.connect('payments.db')
    c = conn.cursor()
    c.execute("SELECT * FROM transactions WHERE tid=?", (tid,))
    if c.fetchone():
        conn.close()
        return {"success": False, "message": "❌ TID ALREADY USED!"}
    
    c.execute("INSERT INTO transactions VALUES (?, ?)", (tid, amount))
    conn.commit()

    c.execute("SELECT SUM(amount) FROM transactions")
    res = c.fetchone()[0]
    total_wallet = res if res else 0
    conn.close()

    success_html = """
    <h3 style='color:green; font-size:16px; font-weight:900;'>✅ PAYMENT VERIFIED! ACCESS MIL GAYA!</h3>
    <p style='font-size:14px; font-weight:900;'>💋 WATCH VIDEO 💋</p>
    <a href='https://t.me/+DVwN8sdnvDQ1YWE9' style='color:#00d4ff; text-decoration:none; font-weight:900; font-size:14px;'>⚡️ JOIN CHANNEL</a>
    """
    return {"success": True, "html": success_html, "new_wallet": total_wallet}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
