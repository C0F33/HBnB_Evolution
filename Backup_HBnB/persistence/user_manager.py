from persistence import DataManager
from flask import Flask, request, jsonify
from model.User import User
import sys
import os

# Get the directory that contains the current script.
current_directory = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory.
parent_directory = os.path.dirname(current_directory)

# Add the parent directory to the Python path.
sys.path.append(parent_directory)


app = Flask(__name__)
datamanager = DataManager()


@app.route('/users', methods=['POST'])
def create_user():
    """
    Create a new user.

    This function handles the POST request to create a new user. It expects a JSON payload
    containing the user's email, first name, and last name. If any of these fields are missing,
    it will return a JSON response with an error message and a status code of 400.

    Returns:
            A JSON response with the created user's information.

    """
    data = request.json
    if 'email' not in data or 'first_name' not in data or 'last_name' not in data:
        return jsonify({'error': "Missing required fields"}), 400
    pass


@app.route('/users', methods=['GET'])
def get_users():
    pass


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    pass


@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    pass


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    pass


if __name__ == '__main__':
    app.run(debug=True)
