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
    def read_so(self):
        purchase_model = self.client.get_model('purchase.order')
        purchase_ids = purchase_model.search([('name', '=', 'P00051')])
        transaction_purchase = purchase_model.read(purchase_ids)
        print(transaction_purchase[0]['name'])
