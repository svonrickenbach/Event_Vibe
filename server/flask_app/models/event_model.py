from flask_app.config.mysqlconnection import connectToMySQL
from .base_model import BaseModel
mydb = 'event_vibe'

class Event(BaseModel):

    json_fields = ['id', 'title', 'date', 'time', 'location', 'description', 'user_id', 'created_at', 'updated_at']

    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.date = data['date']
        self.time = data['time']
        self.location = data['location']
        self.description = data['description']
        self.image = data['image']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO events (title, date, time, location, description, image, user_id, created_at, updated_at) VALUES (%(title)s, %(date)s, %(time)s, %(location)s, %(description)s, %(image)s, %(user_id)s,  NOW(), NOW());"
        results = connectToMySQL(mydb).query_db(query, data)
        # print("RESULTS:" + results)
        return results

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM events;"
        results = connectToMySQL(mydb).query_db(query)
        # print(results)
        events = []
        for event in results:
            # print(user)
            events.append(cls(event))
        return events

    @classmethod
    def update(cls, data):
        query = "UPDATE events SET title = %(title)s, date = %(date)s, time = %(time)s, location = %(location)s, description = %(description)s, image = %(image)s, updated_at = CURRENT_TIMESTAMP WHERE id = %(event_id)s;"
        return connectToMySQL(mydb).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM events WHERE id = %(id)s;"
        return connectToMySQL(mydb).query_db(query, data)

    @classmethod
    def getByID(cls, data):
        query = "SELECT * FROM events WHERE id = %(id)s;"
        results = connectToMySQL(mydb).query_db(query, data)
        return cls(results[0]) 


    # @staticmethod
    # def validate_user(user): 
    #     is_valid = True
    #     if len(user['fname']) < 1: 
    #         flash("must enter a first name", 'regError')
    #         is_valid = False 
    #     elif len(user['fname']) < 2:
    #         flash('first name must be longer than two characters', 'regError')
    #         is_valid = False
    #     elif not NAME_REGEX.match(user['fname']): 
    #         flash("First name cannot contain numbers (unless you're Elon Musks child)!", 'regError')
    #         is_valid = False
    #     if len(user['lname']) < 1:
    #         flash("must enter a last name", 'regError')
    #         is_valid = False
    #     elif len(user['lname']) < 2:
    #         flash('last name must be longer than two characters', 'regError')
    #         is_valid = False
    #     elif not NAME_REGEX.match(user['lname']): 
    #         flash("Last name cannot contain numbers (unless you're Elon Musks child)!", 'regError')
    #         is_valid = False
    #     if len(user['email']) < 1: 
    #         flash("must enter an email", 'regError')
    #         is_valid = False 
    #     elif not EMAIL_REGEX.match(user['email']): 
    #         flash("Invalid email address!", 'regError')
    #         is_valid = False
    #     if User.get_by_email(user) != False:
    #             flash("Invalid email address! ", 'regError')
    #             is_valid = False
    #     if len(user['password']) < 1: 
    #         flash("must enter a password", 'regError')
    #         is_valid = False 
    #     elif len(user['password']) < 9:
    #         flash('password must be longer than 8 characters', 'regError')
    #         is_valid = False
    #     elif not PASSWORD_REGEX.match(user['password']): 
    #         flash("Password must contain at least one uppercase letter and a number!", 'regError')
    #         is_valid = False
    #     if len(user['passConf']) < 1: 
    #         flash("please confirm your password", 'regError')
    #         is_valid = False 
    #     elif user['password'] != user['passConf']:
    #         flash('passwords do not match', 'regError')
    #         is_valid = False
    #     return is_valid