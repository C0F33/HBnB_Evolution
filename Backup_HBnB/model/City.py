import uuid
from model import BaseModel
import datetime


class City(BaseModel):
    def __init__(self, name, state_id):
        self.id = str(uuid.uuid4())
        self.name = name
        self.state_id = state_id
