import unittest
import requests
from app import app  

class GetTest(unittest.TestCase):

    def test_get_todos(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
