from flask import Flask 
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret' # Replace with a secret key of your choice
jwt = JWTManager(app)
# app.secret_key = "secret_key"