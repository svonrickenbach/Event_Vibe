# The __init__.py file name tells python that the file directory should be treated as a package. 

# Imports Flask class functionality from the flask library. 
from flask import Flask
# Imports CORS functionality from the flask_cors library 
from flask_cors import CORS
# an external library that helps handle JWTs
from flask_jwt_extended import JWTManager

# This defines the app variable as the flask app object
app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret' # Replace with a secret key of your choice
# This line of code instatiates an instance of the JWTManager class and passes through the app object created in lines above. JWTManager knows to look for a key called 'JWT_SECRET_KEY' and extracts the password from it. 
jwt = JWTManager(app)
# Defining the origin domain for cross traffic to the server. 
CORS(app, origins=['http://localhost:3000'])
# app.secret_key = "secret_key"