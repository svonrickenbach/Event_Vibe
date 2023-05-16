from flask_app import app 
from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from datetime import datetime 
from flask_bcrypt import Bcrypt
bycrypt = Bcrypt(app)
from flask_app.models.user_model import User
dateFormat = "%m/%d/%Y %I:%M %p"

@app.route('/register', methods=['POST'])
def create_user():
    # print("run")
    data = request.json 
    errors = User.validate_user(data)
    if errors:
        print(errors)
        return jsonify({'errors': errors}), 422
    pw_hash = bycrypt.generate_password_hash(data['password'])
    data['password'] = pw_hash
    user = {"id": User.save(data)}
    access_token = create_access_token(identity=user["id"])
    return jsonify({"token": access_token}), 200

@app.route('/login', methods=['POST'])
def login_user():
    user = User.get_by_email(request.json)
    if user and bycrypt.check_password_hash(user.password, request.json['password']):
        access_token = create_access_token(identity=user.id)
        return jsonify({"token": access_token}), 200
    else:
        return jsonify({"error": "Invlaid credentials!"}), 401


@app.route('/', methods=['GET'])
def get_all(): 
    users = User.get_all()
    users_converted_to_json = [user.to_json() for user in users]
    return jsonify(users_converted_to_json), 200

@app.route('/oneuser', methods=['GET'])
@jwt_required()
def get_user():
    print("running")
    current_user_id = get_jwt_identity()
    print(current_user_id)
    user = User.getByID({"id":current_user_id})
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