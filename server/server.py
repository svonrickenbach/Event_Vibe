# Importing app from __init__.py
from flask_app import app
# Importing controllers from various files
from flask_app.controllers import users_controller, events_controller, friendships_controller, status_controller


from flask_cors import CORS
CORS(app, support_credentials=True)

if __name__ =="__main__":
    app.run(debug=True)