import uuid

from model import BaseModel


class Review(BaseModel):
    def __init__(self, place_id, user_id, text, score):
        self.place_id = place_id
        self.user_id = user_id
        self.text = text
        self.score = score
