#!/usr/bin/python3
"""
Module for Amenity class
"""

import uuid  

class Amenity:
    """
    Amenity class to define amenity properties and behaviors
    """

    def __init__(self, name, Description, Type):
        """
        Initialize a new Amenity instance
        Args:
            name (str): The name of the amenity
            Description (str): The description of the amenity
            Type (str): The type of the amenity
        """
        self.id = uuid.uuid4()  
        self.name = name  
        self.Description = Description  
        self.Type = Type  
        self.places = []  

    def add_place(self, place):
        """
        Add a place to the amenity's places list if it's not already present
        Args:
            place (str): The place to be added
        """
        if place not in self.places:  
            self.places.append(place)  
