from flask import Flask, request, jsonify, abort, Blueprint
import sys
import os

# Get the directory that contains the current script.
current_directory = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory.
parent_directory = os.path.dirname(current_directory)

# Add the parent directory to the Python path.
sys.path.append(parent_directory)
from model.Place import Place
from Data.DataManager import DataManager

place_Api_blueprint = Blueprint('place_Api', __name__)
data_manager = DataManager()

@place_Api_blueprint.route('/Place', methods=['POST'])
def create_place():
	required_fields = ['name', 'price', 'description', 'address', 'city_id', 'latitude', 'longitude', 'host_id',
					 'number_of_rooms', 'price_per_night', 'max_guests', 'amenity_ids']
	if not required_fields.json or not all(field in request.json for field in required_fields):
		abort(400, description="Missing requirements")

	data = request.json
	name = data['name']
	description = data.get('description', '')
	address = data['address']
	city_id = data['city_id']
	latitude = data['latitude']
	longitude = data['longitude']
	host_id = data['host_id']
	number_of_rooms = data['number_of_rooms']
	price_per_night = data['price_per_night']
	max_guests = data['max_guests']
	amenity_ids = data['amenity_ids']

	 # Validar existencia de city_id
	if not data_manager.get(city_id, 'City'):
		abort(400, description="Invalid city_id")

	# Validar existencia de amenity_ids
	for amenity_id in amenity_ids:
		if not data_manager.get(amenity_id, 'Amenity'):
			abort(400, description=f"Invalid amenity_id: {amenity_id}")

	Place = Place(name=name, description=description, address=address, city_id=city_id, latitude=latitude, longitude=longitude,
				  host_id=host_id, number_of_rooms=number_of_rooms, number_of_bathrooms=number_of_bathrooms,
				  price_per_night=price_per_night, max_guests=max_guests, amenity_ids=amenity_ids)
	data_manager.save(Place)

	return jsonify(Place.to_dict()), 201


@place_Api_blueprint.route('/Place', methods=['GET'])
def get_places():
	Places = [Place.to_dict()
			  for Place in data_manager.storage.get('Place', {}).values()]
	return jsonify(Places), 200


@place_Api_blueprint.route('/places/<place_id>', methods=['GET'])
def get_place(place_id):
	Place = data_manager.get(place_id, 'Place')
	if not Place:
		abort(404, description="Place not found")
	return jsonify(Place.to_dict()), 200


@place_Api_blueprint.route('/places/<place_id>', methods=['PUT'])
def update_place(place_id):
	Place = data_manager.get(place_id, 'Place')
	if not Place:
		abort(404, description="Place not found")

	if not request.json:
		abort(400, description="Missing required fields")

	data = request.json
	Place.name = data.get('name', Place.name)
	Place.description = data.get('description', Place.description)
	Place.address = data.get('address', Place.address)
	if 'city_id' in data:
		Place.city_id = data['city_id']
		if not data_manager.get(Place.city_id, 'City'):
			abort(400, description="Invalid city_id")
	Place.latitude = data.get('latitude', Place.latitude)
	Place.longitude = data.get('longitude', Place.longitude)
	Place.host_id = data.get('host_id', Place.host_id)
	Place.number_of_rooms = data.get('number_of_rooms', Place.number_of_rooms)
	Place.number_of_bathrooms = data.get(
		'number_of_bathrooms', Place.number_of_bathrooms)
	Place.price_per_night = data.get('price_per_night', Place.price_per_night)
	Place.max_guests = data.get('max_guests', Place.max_guests)
	Place.amenity_ids = data.get('amenity_ids', Place.amenity_ids)

	# Validar existencia de amenity_ids
	for amenity_id in Place.amenity_ids:
		if not data_manager.get(amenity_id, 'Amenity'):
			abort(400, description=f"Invalid amenity_id: {amenity_id}")

	data_manager.update(Place)
	return jsonify(Place.to_dict()), 200


@place_Api_blueprint.route('/places/<place_id>', methods=['DELETE'])
def delete_place(place_id):
	Place = data_manager.get(place_id, 'Place')
	if not Place:
		abort(404, description="Place not found")
	data_manager.delete(place_id, 'Place')
	return '', 204
