from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.user import User
from flask_app.models.party import Party


@app.route('/parties/new')
def new_party_form():
    if 'user_id' not in session:
        return redirect('/')
    return render_template("parties_new.html")


@app.route('/parties/create', methods=["POST"])
def process_party():
    if 'user_id' not in session:
        return redirect('/')
    if not Party.validator(request.form):
        return redirect('/parties/new')
    data = {
        **request.form,
        'user_id': session['user_id']
    }
    Party.create(data)
    return redirect('/dashboard')


@app.route('/parties/<int:id>/delete')
def del_party(id):
    if 'user_id' not in session:
        return redirect('/')
    party = Party.get_by_id({'id': id})
    if not int(session['user_id']) == party.user_id:
        flash("Error!! Not Allowed!")
        return redirect('/dashboard')
    Party.delete({'id': id})
    return redirect('/dashboard')


@app.route('/parties/<int:id>/edit')
def edit_party_form(id):
    if 'user_id' not in session:
        return redirect('/')
    party = Party.get_by_id({'id': id})
    if not int(session['user_id']) == party.user_id:
        flash("Error!! Not Allowed!")
        return redirect('/dashboard')
    party = Party.get_by_id({'id': id})
    return render_template('parties_edit.html', party=party)


@app.route('/parties/<int:id>/update', methods=['POST'])
def update_party(id):
    if 'user_id' not in session:
        return redirect('/')
    party = Party.get_by_id({'id': id})
    if not int(session['user_id']) == party.user_id:
        flash("Error!! Not Allowed!")
        return redirect('/dashboard')
    if not Party.validator(request.form):
        return redirect(f"/parties/{id}/edit")
    data = {
        **request.form,
        'id': id
    }
    Party.update(data)
    return redirect('/dashboard')

@app.route('/parties/<int:id>')
def show_party(id):
    party = Party.get_by_id({'id': id})
    return render_template("parties_one.html",party=party)

