from flask_app import app 
from flask import request, jsonify
from flask_app.models.status_model import Status

@app.route('/status', methods=['POST'])
def create_status():
    print("run")
    data = request.json # extract the data submitted from the request. Handle EXACTLY like you do request.form.
    # print("data")
    print("data: " + str(data))
    status = {"id": Status.save(data)}
    print(status)
    status_object = Status.getByID(status)

    return jsonify(status_object.to_json()), 201

@app.route('/status/<int:user_status_id>/<int:event_id>', methods=['DELETE'])
def delete_status(user_status_id, event_id):
    Status.delete({"user_status_id":user_status_id,
                        "event_id": event_id})
    return jsonify({}), 204