from app.model import BaseModel

class Place(BaseModel):
	def __init__(self, name, price, description, address, city_id, latitude, longitude, host_id, number_of_rooms, price_per_night, max_guests, amenity_ids):
		self.name = name
		self.description = description
		self.address = address
		self.city_id = city_id
		self.latitude = latitude
		self.longitude = longitude
		self.host_id = host_id
		self.number_of_rooms = number_of_rooms
		self.price_per_night = price_per_night
		self.max_guests = max_guests
		self.amenity_ids = amenity_ids
		self.amenity_ids = []
		self.reviews = []  # List of reviews for the place

	def __str__(self):
		"""Returns a string representation of the place."""
		return f"[Place] ({self.id}) {self.to_dict()}"
