from locust import HttpUser, task, between
from OdooLocust.OdooLocustUser import OdooLocustUser
import json
import random


class PartnerUser(OdooLocustUser):
    wait_time = between(1,3)
    host = '192.168.56.101'
    database = "training"
    login = "admin"
    password = "admin"
    port = 8069
    protocol = "jsonrpc"

    @task(1)
    def create_product(self):
        product_model = self.client.get_model('product.product')
        product_data = {
            'name': f"Test From Locust {self.user_id}", 
            'type': 'service',   
            'list_price': 1000.0, 
            'default_code': f"P{self.user_id}",
            'uom_id': 1, 
            'uom_po_id': 1, 
        }
        product_id = product_model.create(product_data)
        print(f"Product created with ID: {product_id}")

