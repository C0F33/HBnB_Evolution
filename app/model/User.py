import uuid
from BaseModel import BaseModel

""" This class represents the user"""


class User(BaseModel):

	_users = []  # List of users

	def __init__(self, email, first_name="", last_name="", password=""):

		if any(User.email == email for User in User._users):
			raise ValueError("This email is already in use")
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.password = password
		self.reviews = []  # List of reviews made by the user
		User._users.append(self)  # Add user to list of users

	def __str__(self):
		"""Returns a string representation of the user."""
		return f"[User] ({self.id}) {self.to_dict()}"
