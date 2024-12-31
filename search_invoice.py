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
    def read_invoice(self):
        customer_inv_model = self.client.get_model('account.move')
        cust_ids = customer_inv_model.search([('name', '=', 'INV/2024/12/0001')])
        transaction_inv = customer_inv_model.read(cust_ids)
        print(transaction_inv[0]['name'])
