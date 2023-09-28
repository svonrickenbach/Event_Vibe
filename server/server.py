# Importing app from __init__.py
from flask_app import app
# Importing controllers from various files
from flask_app.controllers import users_controller, events_controller, friendships_controller, status_controller

# In this conditional the built-in variable __name__ represents the current script. If the current script is equal to "__main__" (the main program, i.e. being run directly and not when it is imported as a module in another script), than the app will "run" (a flask specific method) and because debug = true, the server will automatically reload when you make changes and it will provide error messages if an error occurs. 
if __name__ =="__main__":
    app.run(debug=True)