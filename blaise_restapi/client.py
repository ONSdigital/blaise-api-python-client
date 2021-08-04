import requests


class Client(object):
    def __init__(self, restapi_url):
        self.restapi_url = restapi_url

    def get_all_questionnaires_with_cati_data(self):
        response = requests.get(f"{self.restapi_url}/api/v1/cati/instruments")
        return response.json()

    def get_all_questionnaires_with_cati_data_for_server_park(self, server_park):
        response = requests.get(f"{self.restapi_url}/api/v1/cati/serverparks/{server_park}/instruments")
        return response.json()

    def get_questionnaire_with_cati_data_for_server_park(self, server_park, instrument_name):
        response = requests.get(f"{self.restapi_url}/api/v1/cati/serverparks/{server_park}/instruments/{instrument_name}")
        return response.json()

    def get_all_questionnaires_for_server_park(self, server_park):
        response = requests.get(f"{self.restapi_url}/api/v1/serverparks/{server_park}/instruments")
        return response.json()

    def get_questionnaire_for_server_park(self, server_park, instrument_name):
        response = requests.get(f"{self.restapi_url}/api/v1/serverparks/{server_park}/instruments/{instrument_name}")
        return response.json()

