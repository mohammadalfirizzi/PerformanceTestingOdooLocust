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
        transfer_model = self.client.get_model('stock.picking')
        transfer_ids = transfer_model.search([('name', '=', 'WH/OUT/00007')])
        transaction_transfer = transfer_model.read(transfer_ids)
        print(transaction_transfer[0]['name'])
