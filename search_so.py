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
        sales_model = self.client.get_model('sale.order')
        sales_ids = sales_model.search([('id', '=', 145)])
        transaction_so = sales_model.read(sales_ids)
        print(transaction_so[0]['name'])
