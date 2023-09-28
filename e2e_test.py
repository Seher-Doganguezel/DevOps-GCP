
from selenium import webdriver

def e2e_test(base_url):
    # Start the browser
    browser = webdriver.Chrome()

    # Visit the main page of your application
    browser.get(base_url)


    # Close the browser at the end of the test
    browser.quit()

    print("E2E test passed!")

# Execute the function
if __name__ == "__main__":
    BASE_URL = "https://devops-gcp-ahi6kdipra-uc.a.run.app"  
    e2e_test(BASE_URL)
