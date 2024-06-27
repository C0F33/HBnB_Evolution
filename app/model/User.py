import uuid
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from model.BaseModel import BaseModel
from app import db
Base = declarative_base()
class User(BaseModel, Base):
	__tablename__ = 'users'
	id = Column(String, primary_key=True, default=uuid.uuid4())
	first_name = db.Column(String)
	last_name = db.Column(String)
	email = db.Column(String)
	password = db.Column(String)
	reviews = db.Column(String, ForeignKey('reviews.id'), default = uuid.uuid4())

	_user = relationship("User", back_populates="owner")
	_reviews = relationship("Review", back_populates="user")
	_users = []
	def __init__(self, id, email, first_name="", last_name="", password=""):
		if any(user['email'] == email for user in User._users):
			raise ValueError("This email is already in use")
		self.id = uuid.uuid4()
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.password = password
		self.reviews = []  # List of reviews made by the user
		User._users.append(self.to_dict())  # Add user to list of users


	def to_dict(self):
		"""Returns the dictionary representation of the user."""
		return {
			'id': self.id,
			'first_name': self.first_name,
			'last_name': self.last_name,
			'email': self.email,
			'password': self.password,
			'reviews': self.reviews
		}
	def from_dict(cls, data):
		"""Returns a user object from a dictionary."""
		return cls(**data)

	@classmethod
	def get_user_list(cls):
		"""Returns the list of users."""
		return cls._users

	@classmethod
	def get_user(cls, email):
		"""Returns the user object with the given email."""
		for user in cls._users:
			if user['email'] == email:
				return cls(**user)
		return None

db = "sqlite:///development/db"
engine = create_engine(db)
Base.metadata.create_all(engine)
