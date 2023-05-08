class BaseModel:

    json_fields = [] 

    def to_json(self):
        return {field: getattr(self, field) for field in self.json_fields}