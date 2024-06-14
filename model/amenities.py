import uuid
from model import BaseModel


class Amenity(BaseModel):
    amenities = 0

    def __init__(self, name, description):
        self.name = name
        self.description = description

        Amenity.amenities += 1
