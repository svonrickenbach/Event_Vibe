from flask_app import app 
from flask import request, jsonify
from flask_app.models.friendship_model import Friendship

@app.route('/friendship', methods=['POST'])
def create_friendship():
    print("run")
    data = request.json # extract the data submitted from the request. Handle EXACTLY like you do request.form.
    friendship = {"id": Friendship.save(data)}
    friendship_object = {
        "message": "Success!!"
    }

    return jsonify(friendship_object.to_json()), 201