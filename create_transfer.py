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
            transfer_model = self.client.get_model('stock.picking')

            cust_ids = cust_model.search([('name', 'ilike', 'Nurosoft')])
            prod_ids = prod_model.search([('name', 'ilike', 'Customizable Desk (CONFIG)')])

            if not cust_ids:
                print("Customer not found.")
                return
            if not prod_ids:
                print("Product not found.")
                return
            cust_id = cust_ids[0]
            payload = {
                'partner_id': cust_id,
                'picking_type_id' : 5,
                'location_id' : 8,
                'location_dest_id' : 8,
                'move_ids_without_package': [(0, 0, {
                    'product_id': prod_ids[0],
                    'product_uom_qty': 1,
                    'name': 'Stock Move',
                    'product_uom': 1,
                    'quantity_done': 1,
                })]
            }
            transfer_id = transfer_model.create(payload)
            # time.sleep(2)
            transfer_model.action_confirm([transfer_id])
            transfer_model.action_assign([transfer_id])
            transfer_model.button_validate([transfer_id])
            print(f"Transfer Created: {transfer_id}")
        except json.JSONDecodeError as e:
            print(f"JSON Decode Error: {e}")
        except Exception as e:
            print(f"Error creating Transfer: {e}")

