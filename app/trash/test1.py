import requests
from app.model import BaseModel
from model import User, Place, Country, City, Review
BASE = "http://127.0.0.1:5000/"

data = [{"email"}]

response = requests.put(BASE + "users/1", {"email": "angelo1998bg@gmail.com", "first_name": "Angelo", "last_name": "bermudez", "password": "password"})