
import time
from selenium import webdriver
from todo_page import TodoPage
import config

def test_todo_app():
    driver = webdriver.Chrome()
    todo_page = TodoPage(driver)
    
    try:
        todo_page.open().add_todo("Test Todo")
        time.sleep(2)
    finally:
        driver.quit()

if __name__ == "__main__":
    test_todo_app()
