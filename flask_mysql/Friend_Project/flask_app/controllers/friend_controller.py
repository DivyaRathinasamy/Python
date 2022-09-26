from flask_app import app

from flask import render_template, redirect, session, request





# import the class from friend.py
from flask_app.models.friend import Friend





@app.route("/")
def index():
    # call the get all classmethod to get all friends
    friends = Friend.get_all()
    print(friends)
    return render_template("index.html", all_friends = friends)


@app.route("/friend/<int:friend_id>")
def one_friend(friend_id):

    data = {
        "id" : friend_id
    }
     
    one_friend = Friend.get_one_friend(data)

    return render_template("show_one.html", one_friend = one_friend)


@app.route("/friend/new")
def add_friend():


    return render_template("add_friend.html")


@app.route('/friend/create', methods =["POST"])
def create_friend():

    data ={
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "age" : int(request.form["age"]),
        "occupation" : request.form["occupation"]
    }

    new_friend_id = Friend.create_new_friend(data)


    return redirect(f'/friend/{new_friend_id}')
