import unittest
import uuid
from datetime import datetime
import sys
import os

# Get the directory that contains the current script.
current_directory = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory.
parent_directory = os.path.dirname(current_directory)

# Add the parent directory to the Python path.
sys.path.append(parent_directory)

# Now you can import the User class.
from City import City

class TestCity(unittest.TestCase):
    def setUp(self):
        self.name = "New York"
        self.country = "USA"
        self.city = City(self.name, self.country)

    def test_initialization(self):
        self.assertEqual(self.city.name, self.name)
        self.assertEqual(self.city.country, self.country)
        # Verifica que places se inicializa como una lista vacía
        self.assertIsInstance(self.city.places, list)

    def test_add_place(self):
        place_id = uuid.uuid4()
        self.city.add_place(place_id)
        self.assertIn(place_id, self.city.places)
        # Verifica que se haya añadido un solo lugar
        self.assertEqual(len(self.city.places), 1)

    def test_add_duplicate_place(self):
        place_id = uuid.uuid4()
        self.city.add_place(place_id)
        # Intentar añadir el mismo lugar nuevamente
        self.city.add_place(place_id)
        # Verifica que el tamaño de places no haya cambiado


if __name__ == '__main__':
    unittest.main()