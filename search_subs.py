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
        subscription_model = self.client.get_model('sale.subscription')
        subscription_ids = subscription_model.search([('id', '=', 1)])
        transaction_subs = subscription_model.read(subscription_ids)
        print(transaction_subs[0]['display_name'])
