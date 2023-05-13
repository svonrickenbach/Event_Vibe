from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager


app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret' # Replace with a secret key of your choice
jwt = JWTManager(app)
CORS(app, origins=['http://localhost:3000'])
# app.secret_key = "secret_key"