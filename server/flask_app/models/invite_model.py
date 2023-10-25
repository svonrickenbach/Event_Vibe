from flask_app.config.mysqlconnection import connectToMySQL
from .base_model import BaseModel
mydb = 'event_vibe'

class Invite(BaseModel):

    json_fields = ['id', 'user_invite_id', 'event_id']

    def __init__(self, data):
        self.id = data['id']
        self.user_invite_id = data['user_invite_id']
        self.event_id = data['event_id']

# I want to user INSERT IGNORE here to prevent any duplicates. However, if something is not sent to the database, then we don't have an id returned for the getByID method to use to return an object to satify the .to_json requirenment. Will have to control it on the front end for now. 
    @classmethod
    def save(cls, data):
        query = "INSERT INTO invites (user_invite_id, event_id) VALUES (%(user_invite_id)s, %(event_id)s);"
        results = connectToMySQL(mydb).query_db(query, data)
        # print("RESULTS:" + results)
        return results

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM invites WHERE user_invite_id = %(user_invite_id)s AND event_id = %(event_id)s;"
        return connectToMySQL(mydb).query_db(query, data)

# The only reason I'm doing this is so that there is an object to return to jsonify when in my create method. I feel like there should be a better way to suffice that need. 
    @classmethod
    def getByID(cls, data):
        query = "SELECT * FROM invites WHERE id = %(id)s;"
        results = connectToMySQL(mydb).query_db(query, data)
        return cls(results[0]) 
    
# I'm using this next database query classmethod to query for all invites for a given user filtered to one instance of an event
    @classmethod
    def get_all(cls):
        query = "SELECT DISTINCT e.id, e.title, e.date, e.time, e.location, e.description, e.image, i.user_invite_id, i.event_id FROM event_vibe.invites AS i LEFT JOIN event_vibe.events AS e ON i.event_id = e.id WHERE i.user_invite_id = %(user_invite_id)s;"
        results = connectToMySQL(mydb).query_db(query)
        # print(results)
        events = []
        for event in results:
            # print(user)
            events.append(cls(event))
        return events