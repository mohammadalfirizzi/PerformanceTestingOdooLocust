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
    def create_subs(self):
        try:
            prod_model = self.client.get_model('product.product')
            cust_model = self.client.get_model('res.partner')
            subs_model = self.client.get_model('sale.subscription')

            cust_ids = cust_model.search([('name', 'ilike', 'Nurosoft')])
            prod_ids = prod_model.search([('name', 'ilike', 'Office Cleaning Subscription (Yearly)')])

            if not cust_ids:
                print("Customer not found.")
                return
            if not prod_ids:
                print("Product not found.")
                return
            cust_id = cust_ids[0]
            payload = {
                'partner_id': cust_id,
                'template_id': 2,
                'recurring_invoice_line_ids': [(0, 0, {
                    'product_id': prod_ids[0],
                    'quantity': 1,
                    'uom_id' : 24,
                    'price_unit': 100
                })]
            }
            subs_id = subs_model.create(payload)
            print(f"Subscription Created: {subs_id}")
            subs_model.start_subscription([subs_id])
        except json.JSONDecodeError as e:
            print(f"JSON Decode Error: {e}")
        except Exception as e:
            print(f"Error creating subscription: {e}")

