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
    def read_projects(self):
        project_model = self.client.get_model('project.project')
        project_ids = project_model.search([])
        projects = project_model.read(project_ids)
        print(projects)