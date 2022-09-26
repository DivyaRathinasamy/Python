from flask import Flask, render_template, render_template,session,request,redirect
# import the class from user.py
app = Flask(__name__)
app.secret_key ="jhdgsfjhdb"

from user import User


@app.route("/")
def index():
    # call the get all classmethod to get all users
    users = User.get_all()
    print(users)
    return render_template("index.html" , all_users = users)


@app.route('/user')
def add_user():


    return render_template("add_user.html")

    
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
            




























if __name__ == "__main__":
    app.run(debug=True)