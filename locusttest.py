"""Module contains locusts user stress tests"""
from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):
    """class contains tests to stress the user basic actions"""
    @task
    def register(self):
        """Method stress tests the user registration end point"""
        response = self.client.post("/", {

        })
        print("response code: ", response.status_code)
        print("response content:", response.content)
    @task
    def login(self):
        """method stress tests the user login endpoint"""
        response = self.client.post("/", {

        })
        print("response code: ", response.status_code)
        print("response content:", response.content)
    @task
    def homepage(self):
        """method stress tests the user login endpoint"""
        response = self.client.get("/#/index")
        print("response code: ", response.status_code)
        print("response content:", response.content)
class WebAppUser(HttpLocust):
    """Class runs the tests as a user"""
    task_set = UserBehavior
