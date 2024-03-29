from flask_app import app 
from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from flask_app.models.invite_model import Invite

@app.route('/invite', methods=['POST'])
def create_invite():
    print("run")
    data = request.json # extract the data submitted from the request. Handle EXACTLY like you do request.form.
    # print("data")
    print("data: " + str(data))
    invite = {"id": Invite.save(data)}
    print(invite)
    invite_object = Invite.getByID(invite)

    return jsonify(invite_object.to_json()), 201

@app.route('/invite/<int:id>', methods=['GET'])
@jwt_required()
def get_all_invites(id): 
        invites = Invite.get_all({"user_invite_id":id})
        invites_converted_to_json = [invite.to_json() for invite in invites]
        print(invites_converted_to_json)
        return jsonify(invites_converted_to_json), 200



# @app.route('/invite/<int:user_invite_id>/<int:event_id>', methods=['DELETE'])
# def delete_status(user_invite_id, event_id):
#     Status.delete({"user_invite_id":user_invite_id,
#                         "event_id": event_id})
#     return jsonify({}), 204