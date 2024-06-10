from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from model import User
from user_blueprints import user_blueprint

app = Flask(__name__)

app.register_blueprint(user_blueprint)

if __name__ == "__main__":
	app.run(debug=True)
