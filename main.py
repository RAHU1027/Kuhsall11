from flask import Flask, render_template_string, request, session
import sqlite3, re

app = Flask(__name__)
app.secret_key = 'kushal_secret_key'

# --- DATABASE SETUP ---
def init_db():
    conn = sqlite3.connect('payments.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS transactions (tid TEXT PRIMARY KEY, amount INTEGER)''')
    conn.commit()
    conn.close()
init_db()

# --- ORIGINAL DATA & DESIGN ---
content = [
    {"text": "😍 <b>80000+ zip file's Channel</b> 💔", "media": "/static/1.jpg", "price": 999},
    {"text": "🥷 <b>VIP STUFF AVAILABLE</b> 🇨🇦", "media": "/static/3.jpg", "price": 149}
]

HTML = """
<!DOCTYPE html>
<html>
<head><meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
    body { background:#0b1626; color:#fff; font-family:sans-serif; margin:0; padding-top:70px; }
    .card { background:#15253d; padding:15px; margin:15px auto; width:90%; border-radius:15px; border:1px solid #2c3e50; }
    .btn-buy { background:#28a745; color:white; width:100%; padding:10px; border:none; border-radius:5px; font-weight:bold; cursor:pointer; }
    .popup { display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.95); z-index:9999; justify-content:center; align-items:center; }
    .box { background:#15253d; padding:20px; border-radius:15px; width:85%; border:1px solid #333; text-align:center; }
</style>
</head>
<body>
    {% for i in content %}
    <div class="card">
        <p>{{ i.text|safe }}</p>
        <p style="color:#ffc107;">Price: ₹{{ i.price }}</p>
        <button class="btn-buy" onclick="openPopup('{{ i.price }}')">BUY NOW</button>
    </div>
    {% endfor %}

    <div id="paymentPopup" class="popup">
        <div class="box">
            <h3>Pay & Add Details ✍️</h3>
            <form action="/verify-payment" method="POST">
                <input type="hidden" name="amount" id="amtInput">
                <p>Amount: <span id="amtText"></span></p>
                <input name="tid" placeholder="12 Digit Transaction ID" required style="width:90%; padding:8px; margin:5px;">
                <button type="submit" class="btn-buy">Submit & Verify</button>
            </form>
        </div>
    </div>
    <script>
        function openPopup(price) {
            document.getElementById('amtInput').value = price;
            document.getElementById('amtText').innerText = "₹" + price;
            document.getElementById('paymentPopup').style.display = 'flex';
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML, content=content)

@app.route('/verify-payment', methods=['POST'])
def verify():
    tid = request.form.get('tid').strip()
    amount = request.form.get('amount')
    
    # REAL-TIME VALIDATION:
    # 1. Check if TID is exactly 12 digits (Standard UPI format)
    if not re.match(r'^\d{12}$', tid):
        return "❌ Error: Invalid Transaction ID! Must be 12 digits."

    # 2. Check Database for duplicate TID
    conn = sqlite3.connect('payments.db')
    c = conn.cursor()
    c.execute("SELECT * FROM transactions WHERE tid=?", (tid,))
    if c.fetchone():
        conn.close()
        return "❌ Error: This Transaction ID has already been used!"
    
    # 3. Successful Verification Logic
    c.execute("INSERT INTO transactions VALUES (?, ?)", (tid, amount))
    conn.commit()
    conn.close()
    
    return f"✅ Payment Verified! Access granted for ₹{amount}."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
