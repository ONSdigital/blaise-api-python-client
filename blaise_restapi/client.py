import requests


class Client(object):
    def __init__(self, restapi_url):
        self.restapi_url = restapi_url


    def get_all_questionnaires_from_server_park(self, server_park):
        response = requests.get(f"{self.restapi_url}/api/v1/serverparks/{server_park}/instruments")
        return response.json()

