from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    db ="recipe_schema"
    def __init__(self,data):
        self.id=data['id']

        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.email=data['email']
        self.password=data['password']

        self.created_at=data['created_at']
        self.updated_at=data['updated_at']


    @classmethod
    def create(cls,data):
        query="INSERT INTO users(first_name,last_name,email,password) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s);"
        return connectToMySQL(cls.db).query_db(query,data)


    @classmethod
    def get_all(cls):
        query="SELECT * FROM users;"
        results =connectToMySQL(cls.db).query_db(query)
        users=[]
        for row in results:
            users.append(cls(row))
            return users



    @classmethod
    def get_by_email(cls,data):
        query="SELECT* FROM users WHERE email= %(email)s;"
        results =connectToMySQL(cls.db).query_db(query,data)
        if len(results) <1:
            return False
        return cls(results[0])


    @classmethod
    def get_by_id(cls,data):
        query="SELECT* FROM users WHERE id= %(id)s;"
        results =connectToMySQL(cls.db).query_db(query,data)
        if len(results) <1:
            return False
        return cls(results[0])

    @staticmethod
    def validate(user_data):
        is_valid =True
        if len(user_data['first_name']) < 1:
            flash("First Name must be Present!",'reg')
            is_valid =False
        if len(user_data['last_name']) < 1:
            flash("Last Name must be Present!",'reg')
            is_valid = False
        if len(user_data['email']) < 1:
            flash("Valid Email must be Given!",'reg')
            is_valid =False
        elif not EMAIL_REGEX.match(user_data['email']):
            flash("Invalid email Format!", 'reg')
            is_valid=False
        else:
            data={
                'email':user_data['email']
            }
            potential_user=User.get_by_email(data)
            if potential_user:
                flash('Email Already Registerd!','reg')
                is_valid =False


        if len(user_data['password']) < 8:
            flash("Password must be atleast 8 characters long!",'reg')
            is_valid= False

        elif not user_data['password'] == user_data['conf_pass']:
            flash("Password Does not Match", 'reg')
            is_valid=False
        return is_valid



    