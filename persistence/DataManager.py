from persistence.IPersistenceManager import IPersistenceManager
import json


class DataManager(IPersistenceManager):
    """Class for managing data persistence."""

    def __init__(self):
        """Initializes the data storage."""
        self.storage = {}

    def save(self, entity):
        """Saves an entity to the storage."""
        entity_type = type(entity).__name__
        entity_id = getattr(entity, 'id', None)
        if not entity_id:
            raise ValueError("Entity must have an 'id' attribute.")

        if entity_type not in self.storage:
            self.storage[entity_type] = {}

        self.storage[entity_type][entity_id] = entity
        print(f"Saved entity: {entity}")

    def get(self, entity_id, entity_type):
        """Retrieves an entity by ID and type from the storage."""
        if entity_type in self.storage and entity_id in self.storage[entity_type]:
            return self.storage[entity_type][entity_id]
        else:
            print(f"Entity not found: {entity_type} with ID {entity_id}")
            return None

    def update(self, entity):
        """Updates an existing entity in the storage."""
        entity_type = type(entity).__name__
        entity_id = getattr(entity, 'id', None)
        if not entity_id:
            raise ValueError("Entity must have an 'id' attribute.")

        if entity_type in self.storage and entity_id in self.storage[entity_type]:
            self.storage[entity_type][entity_id] = entity
            print(f"Updated entity: {entity}")
        else:
            print(f"Entity not found: {entity_type} with ID {entity_id}")

    def delete(self, entity_id, entity_type):
        """Deletes an entity by ID and type from the storage."""
        if entity_type in self.storage and entity_id in self.storage[entity_type]:
            del self.storage[entity_type][entity_id]
            print(f"Deleted entity: {entity_type} with ID {entity_id}")
        else:
            print(f"Entity not found: {entity_type} with ID {entity_id}")
