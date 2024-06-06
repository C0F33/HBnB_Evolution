import uuid
from model import BaseModel
from datetime import datetime


class Amenity(BaseModel):
    def __init__(self, name, description, Type, **kwargs):
        self.name = name
        self.description = description
        self.Type = Type

    def add_place(self, place_id):
        """Add place to amenity."""
        if place_id not in self.place_ids:
            self.place_ids.append(place_id)
