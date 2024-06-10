from app.model import BaseModel

class Country(BaseModel):
	def __init__(self, name, **kwargs,):
		super().__init__(**kwargs)
		self.name = name
		self.country_code = country_code

	def __str__(self):
		"""Returns a string representation of the country."""
		return f"[Country] ({self.id}) {self.to_dict()}"
