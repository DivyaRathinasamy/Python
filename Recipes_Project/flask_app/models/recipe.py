from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user


class Recipe:
    db = "recipe_schema"

    def __init__(self, data):
        self.id = data['id']

        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.under30 = data['under30']
        self.date_made = data['date_made']

        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.user_id = data['user_id']

    @classmethod
    def create(cls, data):
        query = "INSERT INTO recipes(name,description,instructions,under30,date_made,user_id) VALUES (%(name)s,%(description)s,%(instructions)s,%(under30)s,%(date_made)s,%(user_id)s)"
        return connectToMySQL(cls.db).query_db(query, data)

    
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM recipes WHERE id=%(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = "UPDATE recipes SET name=%(name)s, description=%(description)s,instructions=%(instructions)s,date_made=%(date_made)s WHERE id=%(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_by_id(cls,data):
        query="SELECT* FROM recipes JOIN users on users.id=recipes.user_id WHERE recipes.id= %(id)s;"
        results =connectToMySQL(cls.db).query_db(query,data)
        if len(results) <1:
            return False
        # return cls(results[0])
        # changing lines showing one user
        row = results[0]
        this_recipe =cls(row)
        data ={
             **row,
                    'id': ['users.id'],
                    'created_at': ['users.created_at'],
                    'updated_at': ['users.updated_at'],

        }
        planner=user.User(data)
        this_recipe.planner = planner
        return this_recipe


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes JOIN users ON recipes.user_id = users.id;"
        results = connectToMySQL(cls.db).query_db(query)
        if len(results) > 0:
            all_recipes = []
            for row in results:
                this_recipe = (cls(row))
                data = {
                    **row,
                    'id': ['users.id'],
                    'created_at': ['users.created_at'],
                    'updated_at': ['users.updated_at'],

                }
                this_user = user.User(data)
                this_recipe.planner = this_user
                all_recipes.append(this_recipe)
            return all_recipes
        return []

    @staticmethod
    def validator(form_data):
        is_valid =True
        if len(form_data['name']) < 1:
            flash(" Name must be Present!")
            is_valid =False
        if len(form_data['description']) < 1:
            flash("Description must be Present!")
            is_valid = False
        if len(form_data['instructions']) < 1:
            flash("Instructions must be Given!")
            is_valid =False
        if len(form_data['date_made']) < 1:
            flash("Date must be Given!")
            is_valid =False
        if "under30" not in form_data:
            flash("Field Required!")
            is_valid =False

        return is_valid
