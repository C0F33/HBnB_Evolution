from abc import ABC, abstractmethod

class IPersistenceManager(ABC):
    """Interface that defines methods for CRUD operations in data management."""

    @abstractmethod
    def save(self, entity):
        """Saves an entity to the storage."""
        pass

    @abstractmethod
    def get(self, entity_id, entity_type):
        """Retrieves an entity by ID and type from the storage."""
        pass

    @abstractmethod
    def update(self, entity):
        """Updates an existing entity in the storage."""
        pass

    @abstractmethod
    def delete(self, entity_id, entity_type):
        """Deletes an entity by ID and type from the storage."""
        pass
