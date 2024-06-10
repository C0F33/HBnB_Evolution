import sys
import os
import unittest
from app.model import BaseModel, User, Place, Review, Country, City, Amenity
from app.Data import IPersistenceManager


class DataManager(IPersistenceManager):
    def __init__(self):
        self.storage = {}

    def save(self, entity):
        if not isinstance(entity, BaseModel):
            raise ValueError("Entity must be an instance of BaseModel")
        entity_id = entity.id
        entity_type = type(entity).__name__
        if entity_type not in self.storage:
            self.storage[entity_type] = {}
        self.storage[entity_type][entity_id] = entity
        entity.save()

    def get(self, entity_id, entity_type):
        return self.storage.get(entity_type, {}).get(entity_id)

    def update(self, entity):
        if not isinstance(entity, BaseModel):
            raise TypeError("entity must be an instance of BaseModel")
        entity_type = type(entity).__name__
        if entity_type in self.storage and entity.id in self.storage[entity_type]:
            self.storage[entity_type][entity.id] = entity
            entity.save()
        else:
            raise ValueError("Entity not found in storage")

    def delete(self, entity_id, entity_type):
        if entity_type in self.storage and entity_id in self.storage[entity_type]:
            del self.storage[entity_type][entity_id]
		else: