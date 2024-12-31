from locust import HttpUser, task, between
from OdooLocust.OdooLocustUser import OdooLocustUser
import json
import random


# class PartnerUser(OdooLocustUser):
#     wait_time = between(1,3)
#     host = '192.168.56.101'
#     database = "training"
#     login = "admin"
#     password = "admin"
#     port = 8069
#     protocol = "jsonrpc"

    # @task(5)
    # def create_product(self):
    #     product_model = self.client.get_model('product.product')
    #     product_data = {
    #         'name': f"Locust Product {self.user_id}", 
    #         'type': 'product',   
    #         'list_price': 100.0, 
    #         'default_code': f"P{self.user_id}",
    #         'uom_id': 1, 
    #         'uom_po_id': 1, 
    #     }
    #     product_id = product_model.create(product_data)
    #     print(f"Product created with ID: {product_id}")

class MyUser(HttpUser):
    wait_time = between(1, 2)
    waktu = 0
    waktu2 = 0
    waktu3 = 0

    @task(1)  # Task 1
    def task_one(self):
        print("Task One Executed")

    @task(2)  # Task 2
    def task_two(self):
        print("Task Two Executed")

    # @task(100)  # Task 3
    # def task_three(self):
    #     print("Task Three Executed")

