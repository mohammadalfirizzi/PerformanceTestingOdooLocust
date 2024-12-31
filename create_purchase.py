from locust import HttpUser, task, between
from OdooLocust.OdooLocustUser import OdooLocustUser
import json
import random, time


class PartnerUser(OdooLocustUser):
    wait_time = between(1,3)
    host = '192.168.56.101'
    database = "training"
    login = "admin"
    password = "admin"
    port = 8069
    protocol = "jsonrpc"

    @task(1)
    def create_invoice(self):
        try:
            prod_model = self.client.get_model('product.product')
            cust_model = self.client.get_model('res.partner')
            purchase_model = self.client.get_model('purchase.order')

            cust_ids = cust_model.search([('name', 'ilike', 'Nurosoft')])
            prod_ids = prod_model.search([('name', 'ilike', 'Whiteboard Pen')])

            if not cust_ids:
                print("Customer not found.")
                return
            if not prod_ids:
                print("Product not found.")
                return
            cust_id = cust_ids[0]
            payload = {
                'partner_id': cust_id,
                'order_line': [(0, 0, {
                    'product_id': prod_ids[0],
                    'product_qty': 1,
                    'price_unit': 1000
                })]
            }
            purchase_id = purchase_model.create(payload)
            # time.sleep(2)
            purchase_model.button_confirm([purchase_id])
            print(f"Purchase Created: {purchase_id}")
        except json.JSONDecodeError as e:
            print(f"JSON Decode Error: {e}")
        except Exception as e:
            print(f"Error creating Purchase: {e}")
