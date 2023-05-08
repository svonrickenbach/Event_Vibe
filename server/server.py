from flask import Flask, request, jsonify
from flask_app.models import user

app = Flask(__name__)
app.secret_key="abcd" # This is only needed because I am using sessions. It is not required for the API to work.

#CORS - This allows the React app to connect to the API.
from flask_cors import CORS
CORS(app, support_credentials=True)

if __name__=="__main__":    
    app.run(debug=True)    