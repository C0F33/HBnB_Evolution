import uuid
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from model.BaseModel import BaseModel

Base = declarative_base()
class User(BaseModel, Base):
	__tablename__ = 'users'
	userID = Column(String, primary_key=True, default=uuid.uuid4())
	first_name = Column(String)
	last_name = Column(String)
	email = Column(String)
	password = Column(String)
	reviews = Column(String)
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


	def __str__(self):
		"""Returns a string representation of the user."""
		return f"[User] ({self.id}) {self.to_dict()}"

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
