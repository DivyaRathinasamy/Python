from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app
from flask_app.models import user
from flask_app.models import party

class Party:
    db="parties_schema"
    def __init__(self,data):
        self.id = data['id']

        self.what = data['what']
        self.location = data['location']
        self.date = data['date']
        self.all_ages = data['all_ages']
        self.description = data['description']



        self.created_at = data['created_at']
        self.updated_at = data['updared_at']



    @classmethod
    def register_user(cls,data):
        query = "INSERT INTO parties (what, location, date,all_ages,decription,user_id) VALUES (%(first_name)s, %(location)s, %(date)s, %(all_ages)s, %(description)s,%(user_id)s);"

        results = connectToMySQL(cls.db).query_db(query,data)
        return results

    @classmethod
    def get_all(cls):
        query ="SELECT * FROM parties JOIN users on parties.users_id = user.id"
        results= connectToMySQL(cls.db).query_db(query)
        if len(results)> 0:
            all_parties =[]
            for row in results:
                this_party = cls(row)
                data ={
                    **row,
                    "id": row["id"],
                    "created_at": row["created_at"],
                    "updated_at": row["updated_at"]

                }
                this_user =user.User(data)
                this_party.planner = this_user
                all_parties.append(this_party)
                return all_parties
                return []

