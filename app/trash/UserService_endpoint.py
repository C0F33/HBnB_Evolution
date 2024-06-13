from flask import Flask, request, jsonify
import requests
app = Flask(__name__)

# In-memory storage for user data
users = []

# Endpoint for creating a new user
def create_user():
	url = 'http://localhost:5000/User'
	data = {
		'email': 'example@example.com',
		'first_name': 'John',
		'last_name': 'Doe'
	}
	response = requests.post(url, json=data)
	print(response.json())

# Endpoint for retrieving all users
def get_users():
	url = 'http://localhost:5000/User'
	response = requests.get(url)
	print(response.json())

# Endpoint for retrieving a specific user
def get_user(user_id):
	url = f'http://localhost:5000/User/{user_id}'
	response = requests.get(url)
	print(response.json())

# Endpoint for updating a user
def update_user(user_id):
	url = f'http://localhost:5000/User/{user_id}'
	data = {
		'email': 'new_email@example.com',
		'first_name': 'Updated',
		'last_name': 'User'
	}
	response = requests.put(url, json=data)
	print(response.json())

# Endpoint for deleting a user
def delete_user(user_id):
	url = f'http://localhost:5000/User/{user_id}'
	response = requests.delete(url)
	print(response.status_code)

# Example usage
create_user()
get_users()
get_user(1)
update_user(1)
delete_user(1)
