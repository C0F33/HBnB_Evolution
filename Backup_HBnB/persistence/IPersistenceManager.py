from abc import ABC, abstractmethod


class IPersistenceManager(ABC):
    """
    IPersistenceManager is an abstract base class that defines the interface for a persistence manager.
    A persistence manager is responsible for managing the storage of entities in an application.

    Methods:
        save(entity): Save an entity to the storage.
        get(entity_id, entity_type): Retrieve an entity from the storage by its ID and type.
        update(entity): Update an existing entity in the storage.
        delete(entity_id, entity_type): Delete an entity from the storage by its ID and type.
    """

    @abstractmethod
    def save(self, entity):
        """
        Save an entity to the storage.

        Args:
            entity: The entity to save.
        """
        pass

    @abstractmethod
    def get(self, entity_id, entity_type):
        """
        Retrieve an entity from the storage by its ID and type.

        Args:
            entity_id: The ID of the entity.
            entity_type: The type of the entity.

        Returns:
            The entity if found, None otherwise.
        """
        pass

    @abstractmethod
    def update(self, entity):
        """
        Update an existing entity in the storage.

        Args:
            entity: The entity to update.
        """
        pass

    @abstractmethod
    def delete(self, entity_id, entity_type):
        """
        Delete an entity from the storage by its ID and type.

        Args:
            entity_id: The ID of the entity.
            entity_type: The type of the entity.
        """
        pass
