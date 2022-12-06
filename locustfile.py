from locust import HttpUser, task


class LoadTestCityInfo(HttpUser):
    @task
    def post_detail(self):
        self.client.get("/city?city=Lucknow&country=IN")
        # http://127.0.0.1:8000/city?city=Lucknow&country=IN
