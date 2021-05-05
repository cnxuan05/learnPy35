from locust import HttpUser,TaskSet,between,task

class WebsiteTasks(TaskSet):

    def on_start(self):
        self.client.post("/login", {
            "username": "admin",
            "password": "123456"
        })

    @task(2)
    def index(self):
        self.client.get("/")

    @task(1)
    def about(self):
        self.client.get("/admin/")

    def on_stop(self):
        print("stop")

class WebSiteUser(HttpUser):
    task_set = WebsiteTasks
    host = "http://104.224.145.110"
    wait_time = between(1, 2)


