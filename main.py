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

# Naya content list (Sirf wahi jo aapne diya hai)
content = [
    {
        "text": "🔞 <b>50K+ MMS LEAK IN JUST ₹69/-</b> 💦<br>━━━━━━━━━━━━━━━━━━━━<br>🔥 ALL TYPE AVAILABLE<br>✨ 90% OFF SALE<br>👇 CLICK SHOP NOW 👇", 
        "media": "/static/4.jpg", 
        "price": "Rs. 69.00 <span style='text-decoration:line-through; color:gray; font-size:12px;'>Rs. 699.00</span><br><span style='color:red;'>🔥 450+ people bought this</span>"
    },
    {
        "text": "😍 <b>80000+ zip file's Channel</b> 💔<br>━━━━━━━━━━━━━━━━━━━━<br>Benefits:<br>• 📁 All Dark Zip Files Available<br>• 🆕 New Files Added Daily<br>• 🔄 Forwarding Files is Allowed", 
        "media": "/static/1.jpg", 
        "price": "Rs. 1,499.00 <span style='text-decoration:line-through; color:gray; font-size:12px;'>Rs. 3,999.00</span><br><span style='color:red;'>🔥 174 people bought this</span>"
    },
    {
        "text": "🎀 <b>PREMIUM CUTIES LEAK</b> 🎀<br>━━━━━━━━━━━━━━━━━━━━<br>🤡 HELLO USER<br>Direct P#rn Video Channel 🫧<br>D#si Maal Ke Deewan 🥀 Ke Liye ✨<br>51000+ rare D#si le#ks ever.... 😍", 
        "media": "/static/3.jpg", 
        "price": "Rs. 99.00 <span style='text-decoration:line-through; color:gray; font-size:12px;'>Rs. 249.00</span><br><span style='color:red;'>🔥 55 people bought this</span>"
    }
]

HTML = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <div class="header">
        <div class="nav-btn" onclick="document.getElementById('m').style.display='block'">⚙️ SETTINGS</div>
        <div class="nav-btn" style="border-color:#28a745; color:#28a745;">💰 WALLET: ₹20</div>
    </div>

    {% for i in content %}
    <div class="card">
        <img src="{{ i.media }}" style="width:100%; border-radius:10px;">
        <p>{{ i.text|safe }}</p>
        <p style="font-weight:bold;">Price: {{ i.price|safe }}</p>
        <button class="btn-demo" onclick="window.open('https://t.me/+JBVaDAvX-To1NzRl')">FREE DEMO</button>
        <button class="btn-buy" onclick="showPopup()">UNLOCK PREMIUM</button>
    </div>
    {% endfor %}

    <div id="p" class="popup">
        <div class="box" id="content-box">
            <div class="back-btn" onclick="closePopup()">BACK TO HOME</div>
            <h3>Pay & Add Details ✍️</h3>
            <div id="timer" style="color:red; font-weight:bold; margin-bottom:10px;">04:00</div>
            <img src="/static/qr.jpg" style="width:100%; border-radius:5px;">
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
            fetch('/verify', { method: 'POST', headers: {'Content-Type': 'application/x-www-form-urlencoded'}, body: 'tid=' + tid })
            .then(r => r.text()).then(data => { clearInterval(timerInterval); document.getElementById('content-box').innerHTML = data; });
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
    # ... (Aapka purana verify logic yahan rahega)
    return "<h3>✅ Verified!</h3>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
