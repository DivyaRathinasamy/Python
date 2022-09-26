from flask_app import app
from flask import render_template,redirect,session,request,flash
from flask_app.models.user import User
from flask_app.models.recipe import Recipe

@app.route('/recipes/new')
def new_recipe_form():
    if 'user_id' not in session:
        return redirect('/')
    # logged_user=User.get_by_id({'id':session['user_id']})
    return render_template("recipes_new.html")



@app.route('/recipes/create', methods=["POST"])
def process_recipe():
    if 'user_id' not in session:
        return redirect('/')
    if not Recipe.validator(request.form):
        return redirect('/recipes/new')
    data = {
        **request.form,
        'user_id': session['user_id']
    }
    Recipe.create(data)
    return redirect('/dashboard')


@app.route('/recipes/<int:id>/delete')
def del_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    recipe=Recipe.get_by_id({'id':id})
    if not int(session['user_id']) == recipe.user_id:
        flash("Error!! Not Allowed!")
        return redirect('/dashboard')
    Recipe.delete({'id': id})
    return redirect('/dashboard')

@app.route('/recipes/edit/<int:id>')
def edit_recipe_form(id):
    if 'user_id' not in session:
        return redirect('/')
    recipe=Recipe.get_by_id({'id':id})
    if not int(session['user_id']) == recipe.user_id:
        flash("Error!! Not Allowed!")
        return redirect('/dashboard')
    recipe = Recipe.get_by_id({'id': id})
    return render_template('recipes_edit.html', recipe=recipe)

@app.route('/recipes/update/<int:id>', methods=['POST'])
def update_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    recipe=Recipe.get_by_id({'id':id})
    if not int(session['user_id']) == recipe.user_id:
        flash("Error!! Not Allowed!")
        return redirect('/dashboard')
    if not Recipe.validator(request.form):
        return redirect(f"/recipes/edit/{id}")
    data = {
        **request.form,
        'id': id
    }
    Recipe.update(data)
    return redirect('/dashboard')

@app.route('/recipes/<int:id>')
def show_recipe(id):
    recipe =Recipe.get_by_id({'id':id})
    data={
        'id':session['user_id']
    }
    logged_user=User.get_by_id(data)
    return render_template('recipes_one.html', recipe=recipe, logged_user=logged_user)


@app.route('/recipes')
def back_to_main():

    return redirect('/dashboard')

