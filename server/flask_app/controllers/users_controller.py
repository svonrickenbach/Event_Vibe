from flask_app import app 
from flask import request, jsonify
from datetime import datetime 
from flask_app.models.user_model import User
dateFormat = "%m/%d/%Y %I:%M %p"

@app.route('/', methods=['POST'])
def create_user():
    print("run")
    data = request.json # extract the data submitted from the request. Handle EXACTLY like you do request.form.

    user = User.save(data)
    print(user)
    user2 = User.getByID(user)
    print(user2)

    return jsonify(user2.to_json()), 201

