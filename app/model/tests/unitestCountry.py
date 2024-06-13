import unittest

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
from Country import Country


class TestCountry(unittest.TestCase):
    def setUp(self):
        self.id = 1
        self.name = "United States"
        self.code = "US"

    def test_initialization(self):
        country = Country(self.id, self.name, self.code)

        self.assertEqual(country.id, self.id)
        self.assertEqual(country.name, self.name)
        self.assertEqual(country.code, self.code)
        self.assertIsInstance(country.created_at, datetime)
        self.assertIsInstance(country.updated_at, datetime)
        self.assertLessEqual(country.created_at, datetime.now())
        self.assertLessEqual(country.updated_at, datetime.now())

    def test_country_count_increment(self):
        initial_count = Country.country_count
        Country(self.id, "Canada", "CA")
        self.assertEqual(Country.country_count, initial_count + 1)


if __name__ == '__main__':
    unittest.main()