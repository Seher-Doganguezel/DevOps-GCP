
from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(5, 15)
    
    @task
    def index(self):
        self.client.get("/")

    @task
    def another_endpoint(self):
        self.client.get("/another-endpoint")  # Replace this with a valid endpoint of your application
