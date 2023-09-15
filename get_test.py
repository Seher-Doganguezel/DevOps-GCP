import unittest
import requests
from app import app  # Stellen Sie sicher, dass Ihr Flask-App-Objekt importiert wird

class GetTest(unittest.TestCase):

    def test_get_todos(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)
        # Hier können Sie weitere Assertions hinzufügen, um den Inhalt der Antwort zu überprüfen

if __name__ == "__main__":
    unittest.main()
