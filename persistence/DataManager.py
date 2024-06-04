import unittest
from model import user
from model import place
from model import review
from persistence import IPersistenceManager


class DataManager(IPersistenceManager):
    def save(self, entity):

        pass

    def get(self, entity_id, entity_type):
        # Logic to retrieve an entity based on ID and type
        pass

    def update(self, entity):
        # Logic to update an entity in storage
        pass

    def delete(self, entity_id, entity_type):
        # Logic to delete an entity from storage
        pass
