import uuid
from model.BaseModel import BaseModel

""" This class represents the user"""


class User(BaseModel):
	"""
	Represents a user in the system.

	Attributes:
		email (str): The email address of the user.
		first_name (str): The first name of the user.
		last_name (str): The last name of the user.
		password (str): The password of the user.
		reviews (list): A list of reviews made by the user.
	"""

	_users = []  # List of users

	def __init__(self, email, first_name="", last_name="", password=""):
		"""
		Initializes a new instance of the User class.

		Args:
			email (str): The email address of the user.
			first_name (str, optional): The first name of the user. Defaults to an empty string.
			last_name (str, optional): The last name of the user. Defaults to an empty string.
			password (str, optional): The password of the user. Defaults to an empty string.

		Raises:
			ValueError: If the email address is already in use.
		"""
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
