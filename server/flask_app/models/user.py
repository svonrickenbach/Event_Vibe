from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash 
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-0._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$')
mydb = 'login_reg_flask'

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(fname)s, %(lname)s, %(email)s, %(password)s, NOW(), NOW());"
        results = connectToMySQL(mydb).query_db(query, data)
        # print(results)
        return results

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(mydb).query_db(query)
        # print(results)
        users = []
        for user in results:
            # print(user)
            users.append(cls(user))
        return users

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE id = %(current_id)s;"
        return connectToMySQL(mydb).query_db(query, data)

    @classmethod
    def getByID(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(mydb).query_db(query, data)
        # print(results)
        return cls(results[0]) 

    @classmethod 
    def get_by_email(cls, data):
        print(data)
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(mydb).query_db(query, data)
        print(f'results: {results}')
        if len(results) < 1: 
            return False
        return cls(results[0])

    @staticmethod
    def validate_user(user): 
        is_valid = True
        if len(user['fname']) < 1: 
            flash("must enter a first name", 'regError')
            is_valid = False 
        elif len(user['fname']) < 3:
            flash('first name must be longer than two characters', 'regError')
            is_valid = False
        elif not NAME_REGEX.match(user['fname']): 
            flash("First name cannot contain numbers (unless you're Elon Musks child)!", 'regError')
            is_valid = False
        if len(user['lname']) < 1:
            flash("must enter a last name", 'regError')
            is_valid = False
        elif len(user['lname']) < 3:
            flash('last name must be longer than two characters', 'regError')
            is_valid = False
        elif not NAME_REGEX.match(user['lname']): 
            flash("Last name cannot contain numbers (unless you're Elon Musks child)!", 'regError')
            is_valid = False
        if len(user['email']) < 1: 
            flash("must enter an email", 'regError')
            is_valid = False 
        elif not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!", 'regError')
            is_valid = False
        if User.get_by_email(user) != False:
                flash("Invalid email address! ", 'regError')
                is_valid = False
        if len(user['password']) < 1: 
            flash("must enter a password", 'regError')
            is_valid = False 
        elif len(user['password']) < 9:
            flash('password must be longer than 8 characters', 'regError')
            is_valid = False
        elif not PASSWORD_REGEX.match(user['password']): 
            flash("Password must contain at least one uppercase letter and a number!", 'regError')
            is_valid = False
        if len(user['passConf']) < 1: 
            flash("please confirm your password", 'regError')
            is_valid = False 
        elif user['password'] != user['passConf']:
            flash('passwords do not match', 'regError')
            is_valid = False
        return is_valid