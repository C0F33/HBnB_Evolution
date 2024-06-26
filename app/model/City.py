from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from BaseModel import BaseModel


Base = declarative_base()

class City(BaseModel, Base):
    """ City class that inherits from BaseModel """
    __tablename__ = 'city'
    name = Column(String, nullable=False)
    country = Column(String, ForeignKey('country.id'))
    places = Column(String, ForeignKey('place.id'))

    user = relationship("User", back_populates="city")
    place = relationship("Place", back_populates="city")

    def __init__(self, name, country, **kwargs):
        """ Initializes the city with name, country and additional attributes """
        super().__init__(**kwargs)
        self.name = name
        self.country = country
        self.places = []

    def add_place(self, place):
        """ Adds a place to the list of places associated with the city class """
        self.places.append(place)
