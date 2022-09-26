from flask_app import app
from flask import render_template, request,redirect,session
from flask import flash

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
     

from flask_app.models.user import User


@app.route('/')
def index():


    return render_template("index.html")

@app.route('/register', methods= ['POST'])
def register():
    if not User.validate_register(request.form):
        return redirect('/')

    pw_hash = bcrypt.generate_password_hash(request.form["password"])

    data ={
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"],
        "password" : pw_hash
        
    }

    new_user_id=User.register_user(data)

    session['user_id'] = new_user_id



    return redirect('/dashboard')

@app.route('/login' , methods = ["POST"])
def login():
    # 1 validate our login info
    if not User.validate_login(request.form):
        return redirect('/')

    # 2 pull user data to log them in
    logged_user = User.get_by_email(request.form)

    session['user_id'] = logged_user.id

    # 3 redirect elsewhere
    return redirect('/dashboard')


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash("Please login or register before Proceeding!")
        return redirect('/')

    data ={
        "user_id" : session["user_id"]
    }
    user =User.get_by_id(data)

    return render_template("dashboard.html",user = user)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


    