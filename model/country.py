import uuid


class Country(self, name):
    def __init__(self, name, zip_code):
        self.id = str(uuid.uuid4())
        self.name = name
        self.zip_code = zip_code
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        return self.__dict__.copy()
