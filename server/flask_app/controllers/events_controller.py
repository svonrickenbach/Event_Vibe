from flask_app import app 
from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from datetime import datetime 
from flask_app.models.event_model import Event
dateFormat = "%m/%d/%Y %I:%M %p"


@app.route('/event', methods=['POST'])
@jwt_required()
def create_event():
    data = request.json 
    errors = Event.validate_event(data)
    if errors:
        print(errors)
        return jsonify({'errors': errors}), 422
    current_user_id = get_jwt_identity()
    data['user_id'] = current_user_id
    event = {"id": Event.save(data)}
    print(event)
    event_object = Event.getByID(event)
    return jsonify(event_object.to_json()), 201,


@app.route('/event', methods=['GET'], endpoint='events_get')
@jwt_required()
def get_all_events(): 
        events = Event.get_all()
        events_converted_to_json = [event.to_json() for event in events]
        print(events_converted_to_json)
        return jsonify(events_converted_to_json), 200

@app.route('/event/<int:id>', methods=['GET'])
@jwt_required()
def get_event(id):
    event = Event.getByID({"id":id})
    return jsonify(event.to_json()), 200

@app.route('/event/<int:id>', methods=['PUT'])
@jwt_required()
def update_event(id):
    data = request.json 
    print(data)
    errors = Event.validate_event(data)
    if errors:
        print(errors)
        return jsonify({'errors': errors}), 422
    Event.update(data)
    event_object = Event.getByID({'id': id})
    return jsonify(event_object.to_json()), 201,

@app.route('/event/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_event(id):
    Event.delete({"id":id})
    return jsonify({}), 204