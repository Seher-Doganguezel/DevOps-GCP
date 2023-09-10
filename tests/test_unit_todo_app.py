
import unittest
from app import app

class TestUnitTodoApp(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()

    def test_index_route(self):
        # Test if the main page returns a 200 status code
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_add_todo(self):
        # Test if adding a new Todo through the Flask app works correctly
        response = self.app.post('/', data={"title": "Unit Test Todo"}, follow_redirects=True)
        self.assertIn(b"Unit Test Todo", response.data)

if __name__ == "__main__":
    unittest.main()
