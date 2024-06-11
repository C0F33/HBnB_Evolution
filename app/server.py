from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from app.api import user_Api

app = Flask(__name__)

api = Api(app)

app.register_blueprint(user_blueprint)

if __name__ == "__main__":
	app.run(debug=True)
