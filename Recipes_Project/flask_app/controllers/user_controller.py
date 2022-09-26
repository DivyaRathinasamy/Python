from flask_app import app
from flask import render_template,redirect,session,request,flash
from flask_bcrypt import Bcrypt
from flask_app.models.user import User
from flask_app.models.recipe import Recipe

bcrypt =Bcrypt(app)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/users/register', methods=['POST'])
def register():
    if not User.validate(request.form):
        return redirect('/')

    hashed_pass =bcrypt.generate_password_hash(request.form['password'])
    data={
        **request.form,
        "password":hashed_pass
    }
    id = User.create(data)
    session['user_id'] = id
    return redirect('/dashboard')


@app.route('/users/login', methods=['POST'])
def login():
    data ={'email': request.form['email']}
    user_in_db =User.get_by_email(data)

    if not user_in_db:
        flash('Invalid Email/Password','log')
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password,request.form['password']):
        flash("Invalid Email/Password",'log')
        return redirect('/')

    session['user_id'] = user_in_db.id
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    all_recipes=Recipe.get_all()
    data={
        'id':session['user_id']
    }
    logged_user=User.get_by_id(data)
    return render_template('dashboard.html',all_recipes=all_recipes,logged_user=logged_user)





@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')



        

