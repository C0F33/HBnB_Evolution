from flask import Flask, request, jsonify
import datetime
app = Flask(__name__)

# In-memory storage for user data
users = []

# Endpoint for creating a new user
@app.route('/users', methods=['POST'])
def create_user():
	data = request.get_json()
	email = data.get('email')
	first_name = data.get('first_name')
	last_name = data.get('last_name')

	# Validate inputs
	if not email or not first_name or not last_name:
		return jsonify({'error': 'Missing required fields'}), 400

	# Check if email is unique
	if any(user['email'] == email for user in users):
		return jsonify({'error': 'Email already exists'}), 409

	# Create new user
	user = {
		'id': len(users) + 1,
		'email': email,
		'first_name': first_name,
		'last_name': last_name,
		'created_at': datetime.now(),
		'updated_at': datetime.now()
	}
	users.append(user)

	return jsonify(user), 201

# Endpoint for retrieving all users
@app.route('/users', methods=['GET'])
def get_users():
	return jsonify(users), 200

# Endpoint for retrieving a specific user
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
	user = next((user for user in users if user['id'] == user_id), None)
	if user:
		return jsonify(user), 200
	else:
		return jsonify({'error': 'User not found'}), 404

# Endpoint for updating a user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
	user = next((user for user in users if user['id'] == user_id), None)
	if user:
		data = request.get_json()
		email = data.get('email')
		first_name = data.get('first_name')
		last_name = data.get('last_name')

		# Validate inputs
		if not email or not first_name or not last_name:
			return jsonify({'error': 'Missing required fields'}), 400

		# Check if email is unique
		if any(u['email'] == email and u['id'] != user_id for u in users):
			return jsonify({'error': 'Email already exists'}), 409

		# Update user
		user['email'] = email
		user['first_name'] = first_name
		user['last_name'] = last_name
		user['updated_at'] = datetime.now()

		return jsonify(user), 200
	else:
		return jsonify({'error': 'User not found'}), 404

# Endpoint for deleting a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
	user = next((user for user in users if user['id'] == user_id), None)
	if user:
		users.remove(user)
		return '', 204
	else:
		return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
	app.run()