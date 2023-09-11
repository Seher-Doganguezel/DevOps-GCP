
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class TodoE2ETestCase(unittest.TestCase):

    # This method will be called before every test
    def setUp(self):
        # You need to download the chromedriver and specify its path here
        self.browser = webdriver.Chrome('/path/to/chromedriver')
        self.browser.get('http://localhost:5000/')

    # This method will be called after every test
    def tearDown(self):
        self.browser.quit()

    def test_add_todo_e2e(self):
        input_box = self.browser.find_element_by_id('task')
        input_box.send_keys('E2E Test Task')
        input_box.send_keys(Keys.ENTER)
        time.sleep(2) # Wait for the page to load
        tasks = self.browser.find_elements_by_class_name('task')
        tasks_text = [task.text for task in tasks]
        self.assertIn('E2E Test Task', tasks_text)

    def test_delete_todo_e2e(self):
        # Assuming that the E2E Test Task is the last task
        delete_buttons = self.browser.find_elements_by_class_name('delete')
        delete_buttons[-1].click()
        time.sleep(2) # Wait for the page to load
        tasks = self.browser.find_elements_by_class_name('task')
        tasks_text = [task.text for task in tasks]
        self.assertNotIn('E2E Test Task', tasks_text)

    def test_update_todo_e2e(self):
        # Assuming that the E2E Test Task is the last task
        update_buttons = self.browser.find_elements_by_class_name('update')
        update_buttons[-1].click()
        time.sleep(2) # Wait for the page to load
        tasks = self.browser.find_elements_by_class_name('completed-task')
        tasks_text = [task.text for task in tasks]
        self.assertIn('E2E Test Task', tasks_text)

if __name__ == "__main__":
    unittest.main()
