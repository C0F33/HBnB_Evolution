import uuid
from model.BaseModel import BaseModel
from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base_model

Base = declarative_base_model()

class Review(BaseModel, Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True, default=uuid.uuid4)
    content = Column(String, nullable=False)
    user_id = Column(String, ForeignKey('users.id'))
    place_id = Column(String, ForeignKey('places.id'))
    review_count = 0

    user = relationship("User", back_populates="reviews")
    place = relationship("Place", back_populates="reviews")

    def __init__(self, content, rating, user_id, place_id):
        if not 1 <= rating <= 5:
            raise ValueError("Rating must be between 1 and 5")

        self.content = content
        self.rating = rating
        self.user_id = user_id
        self.place_id = place_id

        Review.review_count += 1

