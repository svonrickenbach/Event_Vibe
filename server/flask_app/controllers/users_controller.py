from flask_app import app 
from flask import request, jsonify
from datetime import datetime 
from flask_app.models.user_model import User
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
dateFormat = "%m/%d/%Y %I:%M %p"

@app.route('/register', methods=['POST'])
def register_user():
    print("run")
    data = request.json # extract the data submitted from the request. Handle EXACTLY like you do request.form.
    user = {"id": User.save(data)}
    user_object = User.getByID(user)

    print(user_object)
    return jsonify(user_object.to_json()), 201

@app.route('/login', methods=['POST'])
def login_user():
    data = request.json # extract the data submitted from the request. Handle EXACTLY like you do request.form.
    user_object = User.get_by_email(data)
    if user_object:
        print(user_object)
        user_id = user_object.id
        access_token = create_access_token(identity=user_id)
        return jsonify({'access_token': access_token}), 200
        # return jsonify(user_object.to_json()), 201
    else: 
        return jsonify({'message': 'Invalid credentials'}), 401


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
def delete_user(id):
    User.delete({"id":id})
    return jsonify({}), 204