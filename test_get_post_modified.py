
import requests

BASE_URL = "https://devops-gcp-ahi6kdipra-uc.a.run.app"  # Ersetzen Sie dies durch die URL Ihrer Anwendung

def test_get_and_post(base_url):
    # Test GET-Anfrage
    response_get = requests.get(f"{base_url}/")  # Testen des Home (Index) Endpunkts
    assert response_get.status_code == 200, "GET request failed"
    print("GET request passed!")

    # Test POST-Anfrage
    payload = {
        "title": "Test Task"
    }
    response_post = requests.post(f"{base_url}/add", data=payload)  # Testen des Add Endpunkts
    assert response_post.status_code == 200, "POST request failed"
    print("POST request passed!")

# Führt die Tests aus
if __name__ == "__main__":
    test_get_and_post(BASE_URL)
