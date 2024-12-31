from locust import task, between
from OdooLocust.OdooLocustUser import OdooLocustUser
import json
import random


class Seller(OdooLocustUser):
    wait_time = between(0.1, 10)
    host = '192.168.56.101'
    database = "training"
    login = "admin"
    password = "admin"
    port = 8069
    protocol = "jsonrpc"
    @task(10)
    def create_partner(self):
        try:
            customer_model = self.client.get_model('res.partner')
            payload = {
                'name': 'test partner company',
                'company_type' : 'company'
            }
            customer_id = customer_model.create(payload)
            print(f"Contact Created: {customer_id}")
        except json.JSONDecodeError as e:
            print(f"JSON Decode Error: {e}")
        except Exception as e:
            print(f"Error creating subscription: {e}")

