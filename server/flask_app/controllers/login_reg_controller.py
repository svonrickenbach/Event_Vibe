from flask_app import app 
from flask import render_template, redirect, request, session, flash 
from flask_app.models import user
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from datetime import datetime 
dateFormat = "%m/%d/%Y %I:%M %p"

@app.route('/')
def login_reg():
    return render_template("login_reg.html")

@app.route('/register', methods=['POST'])
def register():
    if user.User.validate_user(request.form):
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        data = {
            "fname" : request.form["fname"],
            "lname" : request.form["lname"],
            "email" : request.form["email"],
            "password" : pw_hash,
        }
        session['user_id'] = user.User.save(data)
        return redirect('/home')
    session['fname'] = request.form['fname']
    session['lname'] = request.form['lname']
    session['email'] = request.form['email']
    return redirect('/')

@app.route('/login', methods = ['POST'])
def login(): 
    data = { "email" : request.form["email"] }
    user_in_db = user.User.get_by_email(data)
    if user_in_db:
        if bcrypt.check_password_hash(user_in_db.password, request.form['password']):
            session['user_id'] = user_in_db.id
            return redirect("/home")
    flash("Invalid Email/Password", 'loginError')
    return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
