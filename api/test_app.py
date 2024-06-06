import unittest
from flask import Flask, json
from app import app


class GetUsersTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()

    def test_get_users(self):
        response = self.client.get('/users')
        data = json.loads(response.get_data(as_text=True))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['email'], 'test@example.com')
        self.assertEqual(data['first_name'], 'First')
        self.assertEqual(data['last_name'], 'Last')


if __name__ == '__main__':
    unittest.main()
