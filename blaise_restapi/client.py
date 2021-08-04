from typing import Any, Dict, List

import requests

from blaise_restapi.functions.instrument_functions import get_instrument_name_from_id


class Client(object):
    def __init__(self, restapi_url):
        self.restapi_url = restapi_url

    def get_all_instruments_with_cati_data(self) -> List[Dict[str, Any]]:
        response = requests.get(f"{self.restapi_url}/api/v1/cati/instruments")
        return response.json()

    def get_all_instruments_with_cati_data_for_server_park(self, server_park: str) -> List[Dict[str, Any]]:
        response = requests.get(f"{self.restapi_url}/api/v1/cati/serverparks/{server_park}/instruments")
        return response.json()

    def get_instrument_with_cati_data_for_server_park(self, server_park: str, instrument_name: str) -> Dict[str, Any]:
        response = requests.get(f"{self.restapi_url}/api/v1/cati/serverparks/{server_park}/instruments/{instrument_name}")
        return response.json()

    def get_all_instruments_for_server_park(self, server_park: str) -> List[Dict[str, Any]]:
        response = requests.get(f"{self.restapi_url}/api/v1/serverparks/{server_park}/instruments")
        return response.json()

    def get_instrument_for_server_park(self, server_park: str, instrument_name: str) -> Dict[str, Any]:
        response = requests.get(f"{self.restapi_url}/api/v1/serverparks/{server_park}/instruments/{instrument_name}")
        return response.json()

    def instrument_exists_on_server_park(self, server_park: str, instrument_name: str) -> bool:
        response = requests.get(f"{self.restapi_url}/api/v1/serverparks/{server_park}/instruments/{instrument_name}/exists")
        return response.json()

    def get_instrument_name_from_id(self, server_park: str, instrument_id: str) -> str:
        response = requests.get(f"{self.restapi_url}/api/v1/serverparks/{server_park}/instruments")
        instrument_list = response.json()
        return get_instrument_name_from_id(instrument_id, instrument_list)

    def get_instrument_data(self, server_park: str, instrument_name: str, data_fields: List) -> Dict[str, Any]:
        data_field_params = []
        for field in data_fields:
            data_field_params.append(("fieldIds", field))
        response = requests.get(
            f"{self.restapi_url}/api/v1/serverparks/{server_park}/instruments/{instrument_name}/report",
            params=data_field_params)

        return response.json()
