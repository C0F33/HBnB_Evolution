from flask import Flask, jsonify, request, Blueprint
from model import User
app = Flask(__name__)



user_blueprint = Blueprint('user_blueprint', __name__)

@user_blueprint.route('/User', methods=['POST'])
def create_user():
	# Get user data from the request
	user_data = request.get_json()

	# Create a user instance
	user_instance = User(user_data['email'], user_data['first_name'],
						 user_data['last_name'], user_data['password'])

	# Save the user instance to the database or perform any necessary operations

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


app.register_blueprint(user_blueprint, url_prefix='/user')

if __name__ == '__main__':
	app.run(debug=True)