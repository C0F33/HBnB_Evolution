import sys
import os

# Get the directory that contains the current script.
current_directory = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory.
parent_directory = os.path.dirname(current_directory)

# Add the parent directory to the Python path.
sys.path.append(parent_directory)

import unittest
from model import User
from model import Place
from model import Review
from persistence import IPersistenceManager


class DataManager(IPersistenceManager):
    def __init__(self):
        self.storage = {}

    def save(self, entity):
        entity_id = entity.id
        entity_type = type(entity).__name__
        if entity_type not in self.storage:
            self.storage[entity_type] = {}
        self.storage[entity_type][entity_id] = entity

    def get(self, entity_id, entity_type):
        return self.storage.get(entity_type, {}).get(entity_id)

    def update(self, entity):
        entity_id = entity.id
        entity_type = type(entity).__name__
        if entity_type in self.storage and entity_id in self.storage[entity_type]:
            self.storage[entity_type][entity_id] = entity

    def delete(self, entity_id, entity_type):
        if entity_type in self.storage and entity_id in self.storage[entity_type]:
            del self.storage[entity_type][entity_id]


class UserService(DataManager):
    def __init__(self, data_manager):
        self.data_manager = data_manager

    def create_user(self, email, first_name, last_name, password):
        user = User(email, first_name, last_name, password)
        self.data_manager.save(user)
        return user

    def get_user(self, user_id):
        return self.data_manager.get(user_id, User)

    def update_user(self, user):
        user = self.data_manager.get(user.id, User)
        if user:
            self.data_manager.update(user)

    def delete_user(self, user_id):
        self.data_manager.delete(user_id, User)
