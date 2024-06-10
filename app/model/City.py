from app.model import BaseModel

class City(BaseModel):
	def __init__(self, name, country_code, **kwargs):
		super().__init__(**kwargs)
		self.name = name
		self.country_code = country_code

	def __str__(self):
		"""Returns a string representation of the city."""
		return f"[City] ({self.id}) {self.to_dict()}"
