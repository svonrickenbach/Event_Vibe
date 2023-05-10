from flask_app import app 
from flask import request, jsonify
from datetime import datetime 
from flask_app.models.event_model import Event
dateFormat = "%m/%d/%Y %I:%M %p"

@app.route('/event', methods=['POST'])
def create_event():
    print("run")
    data = request.json # extract the data submitted from the request. Handle EXACTLY like you do request.form.
    event = {"id": Event.save(data)}
    event_object = Event.getByID(event)

    return jsonify(event_object.to_json()), 201,


@app.route('/event', methods=['GET'])
def get_all_events(): 
    events = Event.get_all()
    events_converted_to_json = [event.to_json() for event in events]
    return jsonify(events_converted_to_json), 200

@app.route('/event/<int:id>', methods=['GET'])
def get_event(id):
    event = Event.getByID({"id":id})
    return jsonify(event.to_json()), 200

@app.route('/event/<int:id>', methods=['PUT'])
def update_event(id):
    data = request.json
    data["event_id"] = id
    Event.update(data)
    event_object = Event.getByID({"id":id})
    return jsonify(event_object.to_json()), 200

@app.route('/event/<int:id>', methods=['DELETE'])
def delete_event(id):
    Event.delete({"id":id})
    return jsonify({}), 204