import uuid
from app.model import BaseModel

class Review(BaseModel):
	def __init__(self, place_id, user_id, description, **kwargs):
		super().__init__(**kwargs)
		self.place_id = place_id
		self.user_id = user_id
		self.description = description

	def __str__(self):
		"""Returns a string representation of the review."""
		return f"[Review] ({self.id}) {self.to_dict()}"
