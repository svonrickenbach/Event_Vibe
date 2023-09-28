# The base_model acts as a parent class for the rest of the model subclasses in the project. It allows the sublcasses to convert their data to serializable json objects. 
class BaseModel:

# Defines an empty list to insert data into. 
    json_fields = []

    """
The jsonify method used in your controller cannot convert a class object to JSON. 
So, before returning the object to the React app, we need to convert it to a dictionary.
    """

# Defines the function to serialize data into a json object. 
    def to_json(self):
        return {field: getattr(self, field) for field in self.json_fields}
