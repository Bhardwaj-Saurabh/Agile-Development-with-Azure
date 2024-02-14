from locust import HttpUser, task, between

class WebsiteTestUser(HttpUser):
    wait_time = between(0.5, 3.0)

    @task(1)
    def test_root(self):
        self.client.get("")

    @task(2)
    def test_predict(self):
        self.client.post("predict", json={
                                "CHAS":{
                                    "0":0
                                },
                                "RM":{
                                    "0":6.575
                                },
                                "TAX":{
                                    "0":296.0
                                },
                                "PTRATIO":{
                                    "0":15.3
                                },
                                "B":{
                                    "0":396.9
                                },
                                "LSTAT":{
                                    "0":4.98
                                }
                            }
                        )