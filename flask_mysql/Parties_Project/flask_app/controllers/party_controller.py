from flask_app import app
from flask import render_template, request,redirect,session
from flask_app.models.user import User
from flask_app.models.party import Party
from flask import flash


@app.route('/parties/new')
def add_new_party():
    if 'user_id' not in session:
        flash("Please login or register before Proceeding!")
        return redirect('/')

    return render_template("parties_new.html")



   