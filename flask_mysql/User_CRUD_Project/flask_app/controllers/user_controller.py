from flask_app import app
from flask import render_template , redirect, session, request


# import the class from user.py
from flask_app.models.user import User


@app.route("/")
def index():
    # call the get all classmethod to get all users
    users = User.get_all()
    print(users)
    return render_template("index.html" , all_users = users)


@app.route('/user')
def add_user():


    return render_template("add_user.html")

@app.route('/user/create')
def one_user():

    return redirect('/')

@app.route('/user/create', methods=["POST"])
def create_user():
    # 1 Collect the information from our form to send to query
    data ={
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }

    # 2 call on query from our model file

    new_user =User.create_new_user(data)

    #  3 redirect elsewhere once query is done

    return redirect('/')

@app.route('/user/return')
def return_user():


    return redirect('/')

@app.route('/user/<int:user_id>/show')
def show_user(user_id):

    data =  {
        "id" : user_id
    }

    one_user = User.show_one_user(data)

    return render_template("show_one.html", one_user = one_user)


@app.route('/user/<int:user_id>/edit')
def edit_user(user_id):

    data= {
        "id" : user_id
    }

    one_user = User.show_one_user(data)

    return render_template("edit_user.html" , one_user = one_user)


@app.route('/user/update/<int:user_id>', methods=["POST"])
def update_user(user_id):
        # 1 Collect the information from our form to send to query
    data ={

        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"],
        "user_id" : user_id
    }

    # 2 call on query from our model file

    User.update(data)

    #  3 redirect elsewhere once query is done

    return redirect('/')

@app.route('/user/<int:user_id>/delete')
def user_delete(user_id):

    # 1 gather query data
    data = {
        "user_id" : user_id
    }

    # 2 run query
    User.delete_user(data)


    # 3 redirect elsewhere 

    return redirect('/')



















