from flask_app.config.mysqlconnection import connectToMySQL
from .base_model import BaseModel
mydb = 'event_vibe'

class Status(BaseModel):

    json_fields = ['id', 'user_id', 'event_id']

    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.event_id = data['event_id']

# I want to user INSERT IGNORE here to prevent any duplicates. However, if something is not sent to the database, then we don't have an id returned for the getByID method to use to return an object to satify the .to_json requirenment. Will have to control it on the front end for now. 
    @classmethod
    def save(cls, data):
        query = "INSERT INTO statuses (user_id, event_id) VALUES (%(user_id)s, %(event_id)s);"
        results = connectToMySQL(mydb).query_db(query, data)
        # print("RESULTS:" + results)
        return results

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM statuses WHERE user_id = %(user_id)s AND event_id = %(event_id)s;"
        return connectToMySQL(mydb).query_db(query, data)

# The only reason I'm doing this is so that there is an object to return to jsonify when in my create method. I feel like there should be a better way to suffice that need. 
    @classmethod
    def getByID(cls, data):
        query = "SELECT * FROM statuses WHERE id = %(id)s;"
        results = connectToMySQL(mydb).query_db(query, data)
        return cls(results[0]) 