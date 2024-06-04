import uuid
from model import BaseModel
from datetime import datetime
""" This class represents the user"""


class User(BaseModel):
    """ Add a new user to the system"""

    def __init__(self, email, first_name="", last_name="", password=""):
        self.email = email
        """user email string"""
        self.first_name = first_name
        self.last_name = last_name
        """ user first and last name strings"""
        self.password = password
        """ user password string"""
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        """inherited from BaseModel"""
