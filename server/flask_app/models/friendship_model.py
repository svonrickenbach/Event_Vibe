from flask_app.config.mysqlconnection import connectToMySQL
from .base_model import BaseModel
mydb = 'event_vibe'

class Friendship(BaseModel):

    json_fields = ['user_id', 'user_id1' 'created_at']

    def __init__(self, data):
        self.user_id = data['user_id']
        self.user_id1 = data['user_id1']
        self.created_at = data['created_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO friendships (user_id, user_id1, created_at) VALUES (%(user_id)s, %(user_id1)s, NOW());"
        results = connectToMySQL(mydb).query_db(query, data)
        # print("RESULTS:" + results)
        return results

    # @classmethod
    # def get_all(cls):
    #     query = "SELECT * FROM events;"
    #     results = connectToMySQL(mydb).query_db(query)
    #     # print(results)
    #     events = []
    #     for event in results:
    #         # print(user)
    #         events.append(cls(event))
    #     return events

    # @classmethod
    # def update(cls, data):
    #     query = "UPDATE events SET title = %(title)s, date = %(date)s, time = %(time)s, location = %(location)s, description = %(description)s, image = %(image)s, updated_at = CURRENT_TIMESTAMP WHERE id = %(event_id)s;"
    #     return connectToMySQL(mydb).query_db(query, data)

    # @classmethod
    # def delete(cls, data):
    #     query = "DELETE FROM events WHERE id = %(id)s;"
    #     return connectToMySQL(mydb).query_db(query, data)

# The only reason I'm doing this is so that there is an object to return to jsonify when in my create method. I feel like there should be a better way to suffice that need. 
    # @classmethod
    # def getByID(cls, data):
    #     query = "SELECT * FROM events WHERE id = %(id)s;"
    #     results = connectToMySQL(mydb).query_db(query, data)
    #     return cls(results[0]) 