from flask import Flask, jsonify, request, Blueprint, abort
import sys
import os

# Get the directory that contains the current script.
current_directory = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory.
parent_directory = os.path.dirname(current_directory)

# Add the parent directory to the Python path.
sys.path.append(parent_directory)
import datetime

from model.User import User
from Data.DataManager import DataManager
from flask import jsonify
app = Flask(__name__)

data = DataManager('save', 'get', 'update', 'delete', 'file_path')

user_blueprint = Blueprint('user_Api', __name__)

@user_blueprint.route('/User', methods=['POST'])
def create_user():
    """Crear un nuevo usuario."""
    if not request.json or not 'email' in request.json or not 'password' in request.json:
        abort(400, description="Missing required fields")

    email = request.json['email']
    password = request.json['password']
    first_name = request.json.get('first_name', '')
    last_name = request.json.get('last_name', '')

    if '@' not in email:  # Simple email validation
        abort(400, description="Invalid email format")

    if data.get_user_by_email(email):
        abort(409, description="Email already exists")

    user = {
        'user_id' : len('user_id') + 1,
        'email': email,
        'first_name': first_name,
        'last_name': last_name,
        'created_at': datetime.now(),
        'updated_at': datetime.now()
    }
    new_user = data.create_user(user)
    return jsonify(new_user), 201


@user_blueprint.route('/User/<user_id>', methods=['GET'])
def get_user(user_id):
	# Retrieve the user from the database or perform any necessary operations

	# Create a user instance
	user_instance = User('test@example.com', 'First', 'Last', 'password')

	# Convert the user instance to a dictionary that can be returned as a response
	user_data = {
		'id': str(user_instance.id),
		'email': user_instance.email,
		'first_name': user_instance.first_name,
		'last_name': user_instance.last_name,
		'created_at': user_instance.created_at.isoformat(),
		'updated_at': user_instance.updated_at.isoformat(),
	}

	return jsonify(user_data)


@user_blueprint.route('/User/<user_id>', methods=['PUT'])
def update_user(user_id):
	# Retrieve the user from the database or perform any necessary operations

	# Create a user instance
	user_instance = User('test@example.com', 'First', 'Last', 'password')

	# Update the user instance with the new data
	user_instance.email = 'new_email@example.com'
	user_instance.first_name = 'New First Name'
	user_instance.last_name = 'New Last Name'
	user_instance.password = 'new_password'

	# Save the updated user instance to the database or perform any necessary operations

	# Convert the user instance to a dictionary that can be returned as a response
	user_data = {
		'id': str(user_instance.id),
		'email': user_instance.email,
		'first_name': user_instance.first_name,
		'last_name': user_instance.last_name,
		'created_at': user_instance.created_at.isoformat(),
		'updated_at': user_instance.updated_at.isoformat(),
	}

	return jsonify(user_data)


@user_blueprint.route('/User/<user_id>', methods=['DELETE'])
def delete_user(user_id):
	# Retrieve the user from the database or perform any necessary operations

	# Delete the user instance from the database or perform any necessary operations

	return 'User deleted'


app.register_blueprint(user_blueprint, url_prefix='/User')

if __name__ == '__main__':
	app.run(debug=True)
	# Test the endpoints
	test_create_user('1')
	test_get_user('1')  # Assuming '1' is the user id returned when creating the user
	test_update_user('1')  # Update the user with id '1' # Delete the user with id '1'
	test_save_user('1')
