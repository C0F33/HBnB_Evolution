import uuid
import datetime


class Country:
    def __init__(self, name, zip_code):
        self.id = str(uuid.uuid4())
        self.name = name
        self.zip_code = zip_code
