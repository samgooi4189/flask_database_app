from flask import Flask, flash, redirect, render_template, request, session, abort
from database import Database
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
db = Database()

@app.route("/")
def index():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Welcome %s! You are logged in" % session.get('username')

@app.route("/register", methods=['GET','POST'])
def user_register():
    if request.method == "GET":
        return render_template('register.html')
    elif request.form['password'] and request.form['username']:
        password = request.form['password']
        username = request.form['username']

        db.insert("INSERT INTO users (`username`, `password`) VALUES ('%s', '%s')" % (username, password))
        session['logged_in'] = True
        session['username'] = username
    else:
        flash("Incomplete form!")
    return index()

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return index()

@app.route("/login", methods=["POST"])
def login():
    if request.form['password'] and request.form['username']:
        user = db.query("SELECT * FROM users WHERE username='%s' AND password='%s'; " % (request.form["username"], request.form["password"]))
        if user:
            session['logged_in'] = True
    return render_template('login.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
