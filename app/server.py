from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from api.user_Api import user_blueprint
from api.country_city_Api import country_city_Api_blueprint
from api.place_Api import place_Api_blueprint
from api.review_Api import review_Api_blueprint
from api.amenity_Api import amenity_Api_blueprint
app = Flask(__name__)

api = Api(app)

app.register_blueprint(user_blueprint)
app.register_blueprint(country_city_Api_blueprint)
app.register_blueprint(place_Api_blueprint)
app.register_blueprint(review_Api_blueprint)
app.register_blueprint(amenity_Api_blueprint)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8000)
