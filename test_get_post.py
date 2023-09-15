
import requests

def test_get_and_post(base_url):
    # Test GET request
    response_get = requests.get(base_url)
    assert response_get.status_code == 200, f"GET request failed with status code {response_get.status_code}"
    print("GET request passed!")

    # Test POST request
    payload = {
        "key1": "value1",
        "key2": "value2"
    }
    response_post = requests.post(base_url, data=payload)
    assert response_post.status_code == 200, f"POST request failed with status code {response_post.status_code}"
    print("POST request passed!")

# Execute the tests
if __name__ == "__main__":
    BASE_URL = "YOUR_APPLICATION_URL"  # Replace with your application's URL
    test_get_and_post(BASE_URL)
