import unittest
import requests
from app import app  # Stellen Sie sicher, dass Ihr Flask-App-Objekt importiert wird

class PostTest(unittest.TestCase):

    def test_create_todo(self):
        tester = app.test_client(self)
        response = tester.post('/add', data=dict(title="Test todo text"))
        self.assertEqual(response.status_code, 200)
        # Hier können Sie weitere Assertions hinzufügen, um den Inhalt der Antwort oder die Datenbank zu überprüfen

if __name__ == "__main__":
    unittest.main()
