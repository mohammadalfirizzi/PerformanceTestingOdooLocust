from locust import task, between
from OdooLocust.OdooLocustUser import OdooLocustUser

class Seller(OdooLocustUser):
    wait_time = between(0.1, 10)
    host = '192.168.56.101'
    database = "training"
    login = "admin"
    password = "admin"
    port = 8069
    protocol = "jsonrpc"
    @task(10)
    def read_partners(self):
        customer_model = self.client.get_model('res.partner')
        customer_ids = customer_model.search([])
        customers = customer_model.read(customer_ids)
        print(customers)