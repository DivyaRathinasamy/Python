from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user


class Party:
    db = "parties_schema"

    def __init__(self, data):
        self.id = data['id']
        self.what = data['what']
        self.location = data['location']
        self.date = data['id']
        self.all_ages = data['all_ages']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod
    def create(cls, data):
        query = "INSERT INTO parties (what,location,date,all_ages,description,user_id) VALUES (%(what)s,%(location)s,%(date)s,%(all_ages)s,%(description)s,%(user_id)s);"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM parties JOIN users on parties.user_id = users.id;"
        results = connectToMySQL(cls.db).query_db(query)
        # THIS IS CHECKING IF THE QUERY RESULT IS EMPTY AKA THERE IS NOTHING IN THE DATABASE
        if len(results) > 0:
            # THE EMPTY LIST IS CREATED TO HOLD THE MANY IN THIS CASE IT IS THE PARTIES
            all_parties = []
            # THIS WILL ITERATE THROUGH EACH ROW OF THE RESULTS FROM THE QUERY
            for row in results:
                # MAKING AN INSTANCE OF THE PARTY CLASS
                this_party = cls(row)

                # PREPARING TO MAKE AN INSTANCE OF THE USER CLASS
                print("*****************************")
                print(this_party)
                print("*****************************")
                print(row)
                print("*****************************")
                data = {
                    **row,
                    'id': row['users.id'],
                    'created_at': row['users.created_at'],
                    'updated_at': row['users.updated_at']
                }
                this_user = user.User(data)
                this_party.planner = this_user
                all_parties.append(this_party)
            return all_parties
        return []

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM parties WHERE id=%(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT* FROM parties JOIN users on user.id= parties.user_id WHERE parties.id= %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        row = results[0]
        this_party = cls(row)
        data = {
            **row,
            'id': row['users.id'],
            'created_at': row['users.created_at'],
            'updated_at': row['users.updated_at']

        }
        planner=user.User(data)
        this_party.planner=planner
        return this_party

    @classmethod
    def update(cls, data):
        query = "UPDATE parties SET what=%(what)s, location=%(location)s,date=%(date)s,all_ages=%(all_ages)s,description=%(description)s WHERE id=%(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

    @staticmethod
    def validator(form_data):
        is_valid = True
        if len(form_data['what']) < 1:
            flash("What must be Present!")
            is_valid = False
        if len(form_data['location']) < 1:
            flash("Location must be Present!")
            is_valid = False
        if len(form_data['date']) < 1:
            flash("Date must be Present!")
            is_valid = False
        if len(form_data['description']) < 1:
            flash("Description must be Present!")
            is_valid = False
        if "all_ages" not in form_data:
            flash("All Ages must be Present!")
            is_valid = False
        return is_valid
