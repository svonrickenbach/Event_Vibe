from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash 
from .base_model import BaseModel
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-0._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$')
mydb = 'event_vibe'

class User(BaseModel):

    json_fields = ['id', 'first_name', 'last_name', 'email', 'password', 'created_at', 'updated_at']

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
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());"
        results = connectToMySQL(mydb).query_db(query, data)
        # print("RESULTS:" + results)
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
    def update(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, password = %(password)s, updated_at = CURRENT_TIMESTAMP WHERE id = %(user_id)s;"
        return connectToMySQL(mydb).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL(mydb).query_db(query, data)

    @classmethod
    def getByID(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(mydb).query_db(query, data)
        return cls(results[0]) 

    @classmethod 
    def get_by_email(cls, data):
        # print(data)
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(mydb).query_db(query, data)
        # print(f'results: {results}')
        if len(results) < 1: 
            return False
        # print(results)
        return cls(results[0])

    @staticmethod
    def validate_user(user): 

        errors = {}

        if len(user['first_name']) < 1: 
            errors['first_name'] = "must enter a first name"
        elif len(user['first_name']) < 2:
            errors['first_name_min'] = "first name must be minimum 2 characters"
        elif not NAME_REGEX.match(user['first_name']): 
            errors['first_name_reg'] = "name must only contain letters!"
        if len(user['last_name']) < 1:
            errors['last_name'] = "must enter a last name"
        elif len(user['last_name']) < 2:
            errors['last_name_min'] = "last name must be minimum 2 characters"
        elif not NAME_REGEX.match(user['last_name']): 
            errors['last_name_reg'] = "last name must only contain letters!"
        if len(user['email']) < 1: 
            errors['email'] = "must enter an email"
        elif not EMAIL_REGEX.match(user['email']): 
            errors['email_reg'] = "Invalid email address!"
        if User.get_by_email(user) != False:
            errors['email_db'] = "An account already exists with this email"
        if len(user['password']) < 1: 
            errors['password'] = "must enter a password"
        elif len(user['password']) < 9:
            errors['password_len'] = "password must be 8 characters or more"
        elif not PASSWORD_REGEX.match(user['password']): 
            errors['password_reg'] = "Password must contain at least one uppercase letter and a number!"
        if len(user['confirmPassword']) < 1: 
            errors['confirm_password'] = "please confirm your password"
        elif user['password'] != user['confirmPassword']:
            errors['password_match'] = "passwords do not match"
        
        return errors