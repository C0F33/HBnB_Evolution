import uuid
from datetime import datetime
""" Base Model class, inherited by derived classes"""


class BaseModel:
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        """universal unique identifier created on initialization"""
        self.created_at = datetime.now()
        """time and date of innitialization"""
        self.updated_at = datetime.now()
        """time and date of last update"""

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        return self.__dict__.copy()
