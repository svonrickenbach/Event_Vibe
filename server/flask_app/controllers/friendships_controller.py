from flask_app import app 
from flask import request, jsonify
from flask_app.models.friendship_model import Friendship

@app.route('/friendship', methods=['POST'])
def create_friendship():
    print("run")
    data = request.json # extract the data submitted from the request. Handle EXACTLY like you do request.form.
    friendship = {"id": Friendship.save(data)}
    friendship_object = Friendship.getByID(friendship)

    return jsonify(friendship_object.to_json()), 201

@app.route('/friendship/<int:user_id>/<int:user_id1>', methods=['DELETE'])
def delete_friendship(user_id, user_id1):
    Friendship.delete({"user_id":user_id,
                        "user_id1": user_id1})
    return jsonify({}), 2040