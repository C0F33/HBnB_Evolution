import sys
import os
from model.Review import Review
import unittest
from model import BaseModel, User, Place, Review, Country, City, Amenity
from Data import IPersistenceManager
import json

# Get the directory that contains the current script.
current_directory = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory.
parent_directory = os.path.dirname(current_directory)

# Add the parent directory to the Python path.
sys.path.append(parent_directory)



class DataManager(IPersistenceManager.IPersistenceManager):
	def __init__(self, save, get, update, delete, file_path):
		self.file_path = file_path
		self.load_data()

	def load_data(self):
		try:
			with open(self.file_path, 'r') as file:
				self.storage = json.load(file)
		except FileNotFoundError:
			self.storage = {}

	def save(self, entity):
		if not isinstance(entity, BaseModel):
			raise ValueError("Entity must be an instance of BaseModel")

		entity_id = entity.id
		entity_type = type(entity).__name__

		if entity_type not in self.storage:
			self.storage[entity_type] = {}

		self.storage[entity_type][entity_id] = entity.to_dict()  # Convert object to dictionary

		with open(self.file_path, 'w') as file:
			json.dump(self.storage, file, indent=4)

	def get(self, entity_id, entity_type):
		if entity_type in self.storage and entity_id in self.storage[entity_type]:
			entity_dict = self.storage[entity_type][entity_id]
			return self.create_entity_from_dict(entity_dict, entity_type)
		else:
			return None

	def update(self, entity):
		if not isinstance(entity, BaseModel):
			raise TypeError("entity must be an instance of BaseModel")
		entity_type = type(entity).__name__
		if entity_type in self.storage and entity.id in self.storage[entity_type]:
			self.storage[entity_type][entity.id] = entity.to_dict()  # Convert object to dictionary
			self.save_data()
		else:
			raise ValueError("Entity not found in storage")

	def delete(self, entity_id, entity_type):
		if entity_type in self.storage and entity_id in self.storage[entity_type]:
			del self.storage[entity_type][entity_id]
			self.save_data()
		else:
			raise ValueError("Entity not found in storage")

	def create_entity_from_dict(self, entity_dict, entity_type):
		# Create and return an instance of the entity using the dictionary
		if entity_type == 'Review':
			return Review.from_dict(entity_dict)
		# Add other entity types as needed

# Example usage
file_path = 'Data.json'  # Specify the file path for data storage

