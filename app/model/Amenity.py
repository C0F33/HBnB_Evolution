from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from BaseModel import BaseModel
import uuid
Base = declarative_base()
class Amenity(BaseModel, Base):
    """ Amenity class that inherits from BaseModel """
    __tablename__ = 'amenity'
    id = Column(Integer, primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    Description = Column(String, nullable=False)
    type = Column(String, nullable=False)
    places = Column(String, ForeignKey('place.id'))

    _place = relationship("Place", back_populates="amenity")

    def __init__(self, name, Description, type, **kwargs):
        """ Initializes the Amenity class with its attributes """
        super().__init__(**kwargs)
        self.name = name
        self.Description = Description
        self.type = type
        self.places = []

    def add_place(self, place):
        """ adds place to the list of places associated with the amenity """
        if place not in self.places:
            self.places.append(place)