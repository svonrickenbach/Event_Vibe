from flask_app import app 
from flask import request, jsonify
from datetime import datetime 
from flask_app.models.user_model import User
dateFormat = "%m/%d/%Y %I:%M %p"

@app.route('/', methods=['POST'])
def create_user():
    print("run")
    data = request.json # extract the data submitted from the request. Handle EXACTLY like you do request.form.
    user = {"id": User.save(data)}
    user_object = User.getByID(user)

    return jsonify(user_object.to_json()), 201


@app.route('/', methods=['GET'])
def get_all(): 
    users = User.get_all()
    users_converted_to_json = [user.to_json() for user in users]
    return jsonify(users_converted_to_json), 200

@app.route('/<int:id>', methods=['GET'])
def get_user(id):
    user = User.getByID({"id":id})
    return jsonify(user.to_json()), 200

@app.route('/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.json
    data["user_id"] = id
    User.update(data)
    user_object = User.getByID({"id":id})
    return jsonify(user_object.to_json()), 200

@app.route('/<int:id>', methods=['DELETE'])
def delete_joke(id):
    User.delete({"id":id})
    return jsonify({}), 204