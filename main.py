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

# --- TUMHARA ORIGINAL CONTENT ---
T1 = "😍 <b>80000+ zip file's Channel</b> 💔"
T3 = "🥷 <b>VIP STUFF AVAILABLE</b> 🇨🇦"
T4 = "🎀 <b>PREMIUM CUTIES LEAK</b> 🎀"
T5 = "🔞 <b>PREMIUM DESI MAAL</b> 🍑"
T6 = "🎬 <b>PREMIUM ADULT COLLECTION</b> ✅"

content = [
    {"text": T1, "media": "/static/1.jpg", "price": "₹999"},
    {"text": T3, "media": "/static/3.jpg", "price": "₹149"},
    {"text": T4, "media": "/static/3.jpg", "price": "₹99"},
    {"text": T5, "media": "/static/2.jpg", "price": "₹69"},
    {"text": T6, "media": "/static/1.jpg", "price": "₹49"}
]

# --- ORIGINAL DESIGN + NAYE FEATURES ---
HTML = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { background:#0b1626; color:#fff; font-family:sans-serif; margin:0; padding-top:70px; }
        .header { position:fixed; top:0; width:100%; background:#15253d; padding:15px; display:flex; justify-content:space-between; border-bottom:2px solid #007bff; align-items:center; z-index:1000; }
        .nav-btn { cursor:pointer; font-weight:bold; color:#00d4ff; padding:8px 12px; border-radius:5px; background:rgba(0,123,255,0.1); border:1px solid #007bff; }
        .card { background:#15253d; padding:15px; margin:15px auto; width:90%; border-radius:15px; border:1px solid #2c3e50; }
        .btn-demo { background:#ffc107; color:black; width:100%; padding:10px; margin-bottom:10px; border:none; border-radius:5px; font-weight:bold; cursor:pointer; }
        .btn-buy { background:#28a745; color:white; width:100%; padding:10px; border:none; border-radius:5px; font-weight:bold; cursor:pointer; }
        .popup { display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.95); z-index:9999; justify-content:center; align-items:center; }
        .box { background:#15253d; padding:20px; border-radius:15px; width:85%; border:1px solid #333; text-align:center; position:relative; }
        .back-btn { position:absolute; top:10px; right:10px; color:#ff4d4d; cursor:pointer; font-weight:bold; font-size:12px; }
    </style>
</head>
<body>
    <div class="header">
        <div class="nav-btn">⚙️ Settings</div>
        <div class="nav-btn" style="border-color:#28a745; color:#28a745;">💰 Wallet: ₹0</div>
    </div>

    {% for i in content %}
    <div class="card">
        <img src="{{ i.media }}" style="width:100%; border-radius:10px;">
        <p>{{ i.text|safe }}</p>
        <p style="color:#ffc107; font-weight:bold;">Price: {{ i.price }}</p>
        <button class="btn-demo" onclick="window.open('https://t.me/+JBVaDAvX-To1NzRl')">FREE DEMO</button>
        <button class="btn-buy" onclick="showPopup()">BUY NOW</button>
    </div>
    {% endfor %}

    <div id="p" class="popup">
        <div class="box" id="content-box">
            <div class="back-btn" onclick="closePopup()">BACK TO HOME</div>
            <h3>Pay & Add Details ✍️</h3>
            <div id="timer" style="color:yellow; font-weight:bold; margin-bottom:10px;">04:00</div>
            <img src="/static/qr.jpg" style="width:100%; background:white; padding:5px; border-radius:5px;">
            <input id="tid" placeholder="Enter 12 Digit Transaction ID" style="width:90%; padding:10px; margin:5px;"><br>
            <button class="btn-buy" onclick="verify()">Submit Details</button>
        </div>
    </div>

    <script>
        let timerInterval;
        function showPopup() { 
            document.getElementById('p').style.display = 'flex';
            startTimer(240);
        }
        function closePopup() { 
            document.getElementById('p').style.display = 'none'; 
            clearInterval(timerInterval);
        }
        function startTimer(duration) {
            let timer = duration, minutes, seconds;
            timerInterval = setInterval(function () {
                minutes = parseInt(timer / 60, 10);
                seconds = parseInt(timer % 60, 10);
                document.getElementById('timer').textContent = "0" + minutes + ":" + (seconds < 10 ? "0" + seconds : seconds);
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
    if not re.match(r'^\d{12}$', tid): return "<h3>❌ Invalid TID format!</h3>"
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
    <p>💋 WATCH VIRAL MEMES FULL VIDEO 💋</p>
    <a href='https://t.me/+DVwN8sdnvDQ1YWE9' style='color:#00d4ff;'>⚡️ JOIN OUR CHANNEL: 💋 𝐃𝐄𝐒𝐈 𝐌𝐀𝐀𝐋 💋</a><br><br>
    <a href='https://t.me/+b9VNf96P_Z9mNjk1' style='color:#00d4ff;'>❤️‍🔥 𝗝𝗔𝗣𝗔𝗡𝗘𝗦𝗘 𝗛𝗨𝗕 ❤️‍🔥</a>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
