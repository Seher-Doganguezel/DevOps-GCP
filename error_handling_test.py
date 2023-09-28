
import requests

def error_handling_test(base_url):
    # Try to access a nonexistent resource
    response = requests.get(f"{base_url}/nonexistent-endpoint")
    
    # Check if a 404 status code is returned
    assert response.status_code == 404, "Expected a 404 status code for a nonexistent endpoint"
    
    print("Error handling test passed!")

# Execute the function
if __name__ == "__main__":
    BASE_URL = "https://devops-gcp-ahi6kdipra-uc.a.run.app"  # Replace URL
    error_handling_test(BASE_URL)
