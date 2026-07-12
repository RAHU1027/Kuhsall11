from flask import Flask, render_template_string, request
import sqlite3, re

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('payments.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS transactions (tid TEXT PRIMARY KEY)')
    conn.commit()
    conn.close()
init_db()

content = [
    {
        "text": "😍 <b>80000+ zip file's Channel</b> 💔<br>━━━━━━━━━━━━━━━━━━━━<br>Benefits:<br>• 📁 All Dark Zip Files Available<br>• 🆕 New Files Added Daily<br>• 🔄 Forwarding Files is Allowed<br><br>🤔 Want to Buy?<br>🚀 Offers Are Live Now!", 
        "media_type": "img",
        "media": "/static/1.jpg", 
        "price": "Rs. 799.00 <span style='text-decoration:line-through; color:gray; font-size:12px;'>Rs. 3,999.00</span><br><span style='color:red;'>🔥 174 people bought this</span>"
    },
    {
        "text": "🔞 <b>50K+ MMS LEAK IN JUST ₹120/-</b> 💦<br>━━━━━━━━━━━━━━━━━━━━<br>🔥 ALL TYPE AVAILABLE<br>✨ 90% OFF SALE<br>👇 CLICK SHOP NOW 👇", 
        "media_type": "video",
        "media": "/static/1.mp4", 
        "price": "Rs. 120.00 <span style='text-decoration:line-through; color:gray; font-size:12px;'>Rs. 249.00</span><br><span style='color:red;'>🔥 450+ people bought this</span>"
    },
    {
        "text": "🥷 <b>VIP STUFF AVAILABLE</b> 🇨🇦<br>━━━━━━━━━━━━━━━━━━━━", 
        "media_type": "img",
        "media": "/static/3.jpg", 
        "price": "Rs. 69.00 <span style='text-decoration:line-through; color:gray; font-size:12px;'>Rs. 199.00</span><br><span style='color:red;'>🔥 94 people bought this</span>"
    },
    {
        "text": "🔞 <b>PREMIUM DESI MAAL</b> 🍑<br>━━━━━━━━━━━━━━━━━━━━", 
        "media_type": "video",
        "media": "/static/2.mp4", 
        "price": "Rs. 99.00 <span style='text-decoration:line-through; color:gray; font-size:12px;'>Rs. 499.00</span><br><span style='color:red;'>🔥 314 people bought this</span>"
    },
    {
        "text": "🔞 <b>PREMIUM DESI MAAL 2</b> 🍑<br>━━━━━━━━━━━━━━━━━━━━", 
        "media_type": "img",
        "media": "/static/2.jpg", 
        "price": "Rs. 99.00 <span style='text-decoration:line-through; color:gray; font-size:12px;'>Rs. 399.00</span><br><span style='color:red;'>🔥 314 people bought this</span>"
    }
]

HTML = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { background:#0b1626; color:#fff; font-family:sans-serif; margin:0; padding-top:70px; }
        .header { position:fixed; top:0; width:100%; background:#15253d; padding:10px; display:flex; justify-content:space-between; align-items:center; z-index:1000; box-sizing:border-box; border-bottom:2px solid #007bff; }
        .nav-btn { font-size:11px; font-weight:bold; color:#00d4ff; padding:6px 10px; border-radius:5px; background:rgba(0,123,255,0.1); border:1px solid #007bff; white-space:nowrap; cursor:pointer; }
        .card { background:#15253d; padding:15px; margin:15px auto; width:90%; border-radius:15px; border:1px solid #2c3e50; }
        .btn-demo { background:#ffc107; color:black; width:100%; padding:10px; margin-bottom:10px; border:none; border-radius:5px; font-weight:bold; cursor:pointer; }
        .btn-buy { background:#28a745; color:white; width:100%; padding:10px; border:none; border-radius:5px; font-weight:bold; cursor:pointer; }
        .popup { display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.95); z-index:9999; justify-content:center; align-items:center; }
        .box { background:#15253d; padding:20px; border-radius:15px; width:85%; border:1px solid #333; text-align:center; position:relative; }
        .back-btn { position:absolute; top:10px; right:10px; color:#ff4d4d; cursor:pointer; font-weight:bold; font-size:11px; }
        .menu { display:none; position:absolute; top:45px; left:10px; background:#1e2a38; border-radius:10px; padding:10px; border:1px solid #007bff; width:120px; z-index:1001; }
        /* Welcome Overlay */
        #welcome-overlay { position:fixed; top:0; left:0; width:100%; height:100%; background:black; z-index:10000; display:flex; justify-content:center; align-items:center; text-align:center; padding:20px; }
        .ok-btn { background:#007bff; color:white; padding:12px 30px; border:none; border-radius:25px; font-weight:bold; cursor:pointer; margin-top:20px; }
    </style>
</head>
<body>
    <div id="welcome-overlay">
        <div>
            <h2>Welcome to Premium Access</h2>
            <p style="color:#aaa;">Category wise content niche diya gaya hai.<br>Payment ke liye 'Unlock Premium' par click karein.</p>
            <button class="ok-btn" onclick="document.getElementById('welcome-overlay').style.display='none'">OK, GOT IT</button>
        </div>
    </div>

    <div class="header">
        <div style="position:relative;">
            <div class="nav-btn" onclick="document.getElementById('m').style.display='block'">⚙️ SETTINGS</div>
            <div id="m" class="menu" onclick="this.style.display='none'">
                <div style="padding:5px;">👤 Profile</div>
                <div style="padding:5px;">💳 Add Funds</div>
                <div style="padding:5px;">🎧 Support</div>
            </div>
        </div>
        <div class="nav-btn" style="border-color:#28a745; color:#28a745;">💰 WALLET: ₹0</div>
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
        <p style="color:#ffc107; font-weight:bold;">Price: {{ i.price|safe }}</p>
        <button class="btn-demo" onclick="window.open('https://t.me/+JBVaDAvX-To1NzRl')">FREE DEMO</button>
        <button class="btn-buy" onclick="showPopup()">UNLOCK PREMIUM</button>
    </div>
    {% endfor %}

    <div id="p" class="popup">
        <div class="box" id="content-box">
            <div class="back-btn" onclick="closePopup()">BACK TO HOME</div>
            <h3>Pay & Add Details ✍️</h3>
            <div id="timer" style="color:yellow; font-weight:bold; margin-bottom:10px;">04:00</div>
            <img src="/static/qr.jpg" style="width:100%; background:white; padding:5px; border-radius:5px;">
            <input id="tid" placeholder="12 Digit Transaction ID" style="width:90%; padding:10px; margin:5px;"><br>
            <button class="btn-buy" onclick="verify()">Submit Details</button>
        </div>
    </div>

    <script>
        let timerInterval;
        function showPopup() { document.getElementById('p').style.display = 'flex'; startTimer(240); }
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
                body: 'tid=' + tid
            }).then(r => r.text()).then(data => {
                clearInterval(timerInterval);
                document.getElementById('content-box').innerHTML = data;
            });
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML, content=content)

@app.route('/verify', methods=['POST'])
def verify():
    tid = request.form.get('tid').strip()
    if not re.match(r'^\d{12}$', tid): return "<h3>❌ Invalid TID!</h3>"
    conn = sqlite3.connect('payments.db')
    c = conn.cursor()
    c.execute("SELECT * FROM transactions WHERE tid=?", (tid,))
    if c.fetchone():
        conn.close()
        return "<h3>❌ TID already used!</h3>"
    c.execute("INSERT INTO transactions VALUES (?)", (tid,))
    conn.commit()
    conn.close()
    return """
    <h3 style='color:green;'>✅ Payment Verified! Access Mil Gaya!</h3>
    <p>💋 WATCH VIDEO 💋</p>
    <a href='https://t.me/+DVwN8sdnvDQ1YWE9' style='color:#00d4ff;'>⚡️ JOIN CHANNEL</a>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
