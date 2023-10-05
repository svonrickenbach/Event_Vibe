from flask_app.config.mysqlconnection import connectToMySQL
from .base_model import BaseModel
from datetime import datetime, timedelta
mydb = 'event_vibe'


class Event(BaseModel):

    json_fields = ['id', 'title', 'date', 'location',
        'description', 'user_id', 'created_at', 'updated_at', 'user_status_id']
    


    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.date = data['date']
        self.time = data['time']
        self.location = data['location']
        self.description = data['description']
        self.image = data['image']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_status_id = data['user_status_id']


    @classmethod
    def save(cls, data):
        query = "INSERT INTO events (title, date, time, location, description, image, user_id, created_at, updated_at) VALUES (%(title)s, %(date)s, %(time)s, %(location)s, %(description)s, %(image)s, %(user_id)s,  NOW(), NOW());"
        results = connectToMySQL(mydb).query_db(query, data)
        # print("RESULTS:" + results)
        return results

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM event_vibe.events LEFT JOIN event_vibe.statuses ON events.id = statuses.event_id;"
        results = connectToMySQL(mydb).query_db(query)
        # print(results)
        events = []
        for event in results:
            # print(user)
            events.append(cls(event))
        return events

    @classmethod
    def update(cls, data):
        query = "UPDATE events SET title = %(title)s, date = %(date)s, time = %(time)s, location = %(location)s, description = %(description)s, image = %(image)s, updated_at = CURRENT_TIMESTAMP WHERE id = %(event_id)s;"
        return connectToMySQL(mydb).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM events WHERE id = %(id)s;"
        return connectToMySQL(mydb).query_db(query, data)

    @classmethod
    def getByID(cls, data):
        query = "SELECT * FROM events WHERE id = %(id)s;"
        results = connectToMySQL(mydb).query_db(query, data)
        return cls(results[0])

    @staticmethod
    def validate_event(event):
        errors = {}
        form_date_str = event['date'] 

        if len(event['title']) < 1:
            errors['title'] = "must enter a title"
        elif len(event['title']) < 2:
            errors['title_min'] = "title must be two characters or more"
        if not form_date_str:
            errors['date'] = "must enter a date"
        else: 
            form_date = datetime.strptime(form_date_str, '%Y-%m-%d').date()
            today = datetime.today().date()
            if form_date <= today:
                errors['date_future'] = "Invalid date selection"
        # if not event['time']:
        #     errors['time'] = "mmust enter a time"
        if not event['location']:
            errors['location'] = "Must enter a location"
        elif len(event['location']) < 3:
            errors['location_min'] = "Location must be 3 or more characters"
        if len(event['description']) < 1:
            errors['description'] = "please enter a description"

        return errors
