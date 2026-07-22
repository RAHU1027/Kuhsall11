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
        /* Modern red solid background & unique bold large capital letters */
        body { background: #dc2626; color:#fff; font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin:0; padding-top:70px; padding-bottom:70px; min-height: 100vh; text-transform: uppercase; }
        .header { position:fixed; top:0; width:100%; background:rgba(153, 0, 0, 0.95); backdrop-filter: blur(10px); padding:10px; display:flex; justify-content:space-between; align-items:center; z-index:1000; box-sizing:border-box; border-bottom:1px solid rgba(255,255,255,0.2); }
        .nav-btn { font-size:11px; font-weight:900; letter-spacing: 1px; color:#fff; padding:6px 10px; border-radius:5px; background:rgba(255,255,255,0.1); border:1px solid rgba(255,255,255,0.3); white-space:nowrap; cursor:pointer; }
        .card { background:rgba(0, 0, 0, 0.5); backdrop-filter: blur(5px); padding:15px; margin:15px auto; width:90%; border-radius:15px; border:1px solid rgba(255,255,255,0.1); box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3); }
        
        /* Unique Bold Large Typography Styling */
        .card p { font-size: 13px; font-weight: 800; letter-spacing: 0.5px; line-height: 1.5; color: #e0e0e0; }
        .card b { font-size: 16px; letter-spacing: 1px; color: #fff; }

        .btn-demo { background:#ffeb3b; color:black; width:100%; padding:10px; margin-bottom:10px; border:none; border-radius:5px; font-weight:900; font-size:12px; letter-spacing:1px; cursor:pointer; }
        .btn-buy { background:#28a745; color:white; width:100%; padding:10px; border:none; border-radius:5px; font-weight:900; font-size:12px; letter-spacing:1px; cursor:pointer; }
        .popup { display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.9); backdrop-filter: blur(8px); z-index:9999; justify-content:center; align-items:center; }
        .box { background:#4a0000; padding:20px; border-radius:15px; width:85%; border:1px solid rgba(255,255,255,0.2); text-align:center; position:relative; box-shadow: 0 10px 25px rgba(0,0,0,0.5); }
        .box h3 { font-size: 16px; font-weight: 900; letter-spacing: 1px; color: #fff; }
        .back-btn { position:absolute; top:10px; right:10px; color:#ffcccc; cursor:pointer; font-weight:900; font-size:11px; letter-spacing: 1px; }
        .menu { display:none; position:absolute; top:45px; left:10px; background:#990000; border-radius:10px; padding:10px; border:1px solid rgba(255,255,255,0.2); width:120px; z-index:1001; box-shadow: 0 5px 15px rgba(0,0,0,0.3); font-size: 11px; font-weight: 800; color: white; }
        
        /* Welcome Overlay */
        #welcome-overlay { position:fixed; top:0; left:0; width:100%; height:100%; background:#cc0000; z-index:10000; display:flex; justify-content:center; align-items:center; text-align:center; padding:20px; }
        #welcome-overlay h2 { font-size: 20px; font-weight: 900; letter-spacing: 1px; color: #fff; }
        #welcome-overlay p { font-size: 11px; font-weight: 700; color:#ffcccc; letter-spacing: 0.5px; }
        .ok-btn { background:#fff; color:#cc0000; padding:12px 30px; border:none; border-radius:25px; font-weight:900; font-size:12px; letter-spacing:1px; cursor:pointer; margin-top:20px; }

        /* Bottom Navigation Bar & Admin Button Styles */
        .bottom-nav { position: fixed; bottom: 0; left: 0; width: 100%; background: rgba(153, 0, 0, 0.95); backdrop-filter: blur(10px); display: flex; justify-content: space-around; padding: 10px 0; border-top: 1px solid rgba(255,255,255,0.2); z-index: 1000; box-sizing: border-box; }
        .nav-item { text-align: center; color: #aaa; cursor: pointer; font-size: 10px; font-weight: 900; letter-spacing: 1px; text-decoration: none; }
        .nav-item.active { color: #ffeb3b; }
        .nav-item div { font-size: 18px; margin-bottom: 2px; }
        .float-admin { position: fixed; bottom: 70px; right: 20px; background: #0088cc; color: white; padding: 10px 18px; border-radius: 25px; font-size: 11px; font-weight: 900; text-decoration: none; box-shadow: 0 4px 15px rgba(0,0,0,0.4); z-index: 999; display: flex; align-items: center; gap: 6px; border: 1px solid rgba(255,255,255,0.3); cursor: pointer; }
        .page-section { display: none; }
        .page-section.active { display: block; }
        .store-title { text-align: center; font-size: 20px; font-weight: 900; letter-spacing: 2px; margin: 20px 0; color: #ffeb3b; }
        .review-card, .profile-card { background: rgba(0, 0, 0, 0.6); border: 1px solid rgba(255,255,255,0.1); width: 90%; margin: 15px auto; padding: 15px; border-radius: 15px; box-shadow: 0 5px 20px rgba(0,0,0,0.3); }
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
                <div style="padding:5px; cursor:pointer;" onclick="switchPage('profile', document.querySelectorAll('.nav-item')[2])">👤 PROFILE</div>
                <div style="padding:5px; cursor:pointer;" onclick="window.open('https://t.me/Skjsbsh166')">💳 ADD FUNDS</div>
                <div style="padding:5px; cursor:pointer;" onclick="window.open('https://t.me/Skjsbsh166')">🎧 SUPPORT</div>
            </div>
        </div>
        <div class="nav-btn" style="border-color:#fff; color:#fff;" id="wallet-display">💰 WALLET: ₹{{ total_wallet }}</div>
    </div>

    <!-- Working Contact Admin Button -->
    <a href="https://t.me/Skjsbsh166" target="_blank" class="float-admin">
        ✈️ Contact Admin
    </a>

    <!-- HOME PAGE -->
    <div id="page-home" class="page-section active">
        <div class="store-title">✨ CP STORE</div>
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
            <p style="color:#ffeb3b; font-weight:900; font-size:14px;">PRICE: {{ i.price|safe }}</p>
            <button class="btn-demo" onclick="window.open('https://t.me/+JBVaDAvX-To1NzRl')">FREE DEMO</button>
            <button class="btn-buy" onclick="showPopup('{{ i.price_val }}')">UNLOCK PREMIUM</button>
        </div>
        {% endfor %}
    </div>

    <!-- REVIEWS PAGE -->
    <div id="page-reviews" class="page-section">
        <div class="store-title">✨ CP STORE</div>
        <div style="text-align:center; font-size:12px; font-weight:700; color:#ffcccc; margin-bottom:15px;">⭐ Customer Reviews<br><span style="font-size:10px; color:#aaa;">Sirf verified purchasers feedback de sakte hain</span></div>
        
        <div class="review-card">
            <div style="color:gold; font-size:14px;">★★★★★ <span style="float:right; color:#aaa; font-size:11px;">Anonymous</span></div>
            <p style="font-size:13px; margin:10px 0;">"49 rs best ha bro"</p>
            <div style="font-size:10px; color:#ffeb3b;">📦 DESI MALAYALAM AUNTY</div>
        </div>
        
        <div class="review-card">
            <div style="color:gold; font-size:14px;">★★★★★ <span style="float:right; color:#aaa; font-size:11px;">Anonymous</span></div>
            <p style="font-size:13px; margin:10px 0;">"Best"</p>
            <div style="font-size:10px; color:#ffeb3b;">📦 10 INDIAN CP FILE</div>
        </div>

        <div class="review-card">
            <div style="color:gold; font-size:14px;">★★★★★ <span style="float:right; color:#aaa; font-size:11px;">Anonymous</span></div>
            <p style="font-size:13px; margin:10px 0;">"199 rs is best"</p>
            <div style="font-size:10px; color:#ffeb3b;">📦 INDIAN CP</div>
        </div>
    </div>

    <!-- PROFILE PAGE -->
    <div id="page-profile" class="page-section">
        <div class="store-title">✨ CP STORE</div>
        <div class="profile-card" style="text-align:center;">
            <div style="font-size:40px; margin-bottom:10px;">👤</div>
            <div style="font-size:16px; font-weight:900; color:#fff;">Tu6</div>
            <div style="display:inline-block; background:rgba(255,255,255,0.1); padding:5px 15px; border-radius:15px; font-size:11px; margin-top:10px; border:1px solid rgba(255,255,255,0.2);">User ID: 7435</div>
        </div>
        
        <div class="profile-card" style="text-align:center;">
            <div style="font-size:11px; color:#aaa;">TOTAL PURCHASES</div>
            <div style="font-size:22px; font-weight:900; color:#ffeb3b; margin-top:5px;">0</div>
        </div>

        <div class="profile-card" style="text-align:center;">
            <div style="font-size:11px; color:#aaa;">MEMBER SINCE</div>
            <div style="font-size:16px; font-weight:900; color:#ffeb3b; margin-top:5px;">Mar 2026</div>
        </div>
    </div>

    <!-- BOTTOM NAVIGATION -->
    <div class="bottom-nav">
        <div class="nav-item active" onclick="switchPage('home', this)">
            <div>🏠</div> Home
        </div>
        <div class="nav-item" onclick="switchPage('reviews', this)">
            <div>⭐</div> Reviews
        </div>
        <div class="nav-item" onclick="switchPage('profile', this)">
            <div>👤</div> Profile
        </div>
    </div>

    <div id="p" class="popup">
        <div class="box" id="content-box">
            <div class="back-btn" onclick="closePopup()">BACK TO HOME</div>
            <h3>PAY & ADD DETAILS ✍️</h3>
            <div id="timer" style="color:yellow; font-weight:900; font-size:15px; margin-bottom:10px;">04:00</div>
            <img src="/static/qr.jpg" style="width:100%; background:white; padding:5px; border-radius:5px;">
            <input id="tid" placeholder="12 DIGIT TRANSACTION ID" style="width:90%; padding:10px; margin:5px; background:#990000; border:1px solid rgba(255,255,255,0.3); color:#fff; border-radius:5px; font-weight:bold; text-align:center; text-transform:uppercase;"><br>
            <button class="btn-buy" onclick="verify()">SUBMIT DETAILS</button>
        </div>
    </div>

    <script>
        let timerInterval;
        let currentPrice = 0;
        
        function switchPage(pageId, element) {
            document.querySelectorAll('.page-section').forEach(el => el.classList.remove('active'));
            document.querySelectorAll('.nav-item').forEach(el => el.classList.remove('active'));
            
            document.getElementById('page-' + pageId).classList.add('active');
            if(element) element.classList.add('active');
            window.scrollTo(0, 0);
        }

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
    <h3 style='color:#32cd32; font-size:16px; font-weight:900;'>✅ PAYMENT VERIFIED! ACCESS MIL GAYA!</h3>
    <p style='font-size:14px; font-weight:900; color:white;'>💋 WATCH VIDEO 💋</p>
    <a href='https://t.me/+DVwN8sdnvDQ1YWE9' style='color:#00ffff; text-decoration:none; font-weight:900; font-size:14px;'>⚡️ JOIN CHANNEL</a>
    """
    return {"success": True, "html": success_html, "new_wallet": total_wallet}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
