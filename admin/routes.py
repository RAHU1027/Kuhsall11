from flask import Blueprint, render_template_string, request, session, redirect
import json, os

admin_bp = Blueprint('admin', __name__)
USER_DB = "users_data.json"

def get_users():
    with open(USER_DB, "r") as f: return json.load(f)

@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        users = get_users()
        user = request.form.get('username')
        pw = request.form.get('password')
        if user in users and users[user]['password'] == pw:
            session['user'] = user
            return redirect('/admin/dashboard')
        return "Invalid Login!"
    return '<form method="POST">User: <input name="username"><br>Pass: <input name="password"><br><button>Login</button></form>'

@admin_bp.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'user' not in session: return redirect('/admin/login')
    # Dashboard logic yahan...
    return "<h2>Dashboard Page</h2>"
