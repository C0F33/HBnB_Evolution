import uuid
from model import BaseModel
"""place class, inherited by derived classes"""


class Places(BaseModel):
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description
        self.reviews = []  # List of reviews for the place
