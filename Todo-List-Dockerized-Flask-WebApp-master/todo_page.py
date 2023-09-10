
from selenium.webdriver.common.by import By
import config

class TodoPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(config.BASE_URL)
        return self

    def add_todo(self, task_name):
        input_element = self.driver.find_element(By.NAME, "title")
        input_element.send_keys(task_name)
        add_button = self.driver.find_element(By.XPATH, "//button[text()='Add']")
        add_button.click()
        return self
