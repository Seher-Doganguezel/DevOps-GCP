
import unittest
import sqlite3
from app import app

class TestIntegrationTodoApp(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.db = sqlite3.connect("db/db.sqlite")

    def tearDown(self):
        # Clean up the database after each test
        cursor = self.db.cursor()
        cursor.execute("DELETE FROM todo WHERE title=?", ("Test Todo",))
        self.db.commit()
        cursor.close()
        self.db.close()

    def test_add_todo(self):
        # Step 1: Add a new Todo through the Flask app
        response = self.app.post('/', data={"title": "Test Todo"}, follow_redirects=True)
        self.assertIn(b"Test Todo", response.data)  # Check if the Todo is displayed in the response

        # Step 2: Check if the Todo is correctly stored in the database
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM todo WHERE title=?", ("Test Todo",))
        todo = cursor.fetchone()
        self.assertIsNotNone(todo)  # Check if the Todo is found in the database

        # Step 3: Check if the Todo can be correctly retrieved by the Flask app
        response = self.app.get('/')
        self.assertIn(b"Test Todo", response.data)  # Check if the Todo is displayed in the response

if __name__ == "__main__":
    unittest.main()
