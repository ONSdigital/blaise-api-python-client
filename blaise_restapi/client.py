from typing import Any, Dict, List, Union

import requests
from urllib3.exceptions import HTTPError

from blaise_restapi.functions.questionnaire_functions import get_questionnaire_name_from_id


class Client(object):
    def __init__(self, restapi_url):
        self.restapi_url = restapi_url

    def format_url_query_string(self, key_names: list, key_values: list) -> str:
        query_string = '&'.join([f"keyNames={name}" for name in key_names] +
                                [f"keyValues={value}" for value in key_values])
        return query_string

    def get_all_questionnaires_with_cati_data(self) -> List[Dict[str, Any]]:
        response = requests.get(f"{self.restapi_url}/api/v2/cati/questionnaires")
        return response.json()

    def get_all_questionnaires_with_cati_data_for_server_park(self, server_park: str) -> List[Dict[str, Any]]:
        response = requests.get(f"{self.restapi_url}/api/v2/cati/serverparks/{server_park}/questionnaires")
        return response.json()

    def get_questionnaire_with_cati_data_for_server_park(self, server_park: str, questionnaire_name: str) -> Dict[
        str, Any]:
        response = requests.get(
            f"{self.restapi_url}/api/v2/cati/serverparks/{server_park}/questionnaires/{questionnaire_name}")
        return response.json()

    def get_all_questionnaires_for_server_park(self, server_park: str) -> List[Dict[str, Any]]:
        response = requests.get(f"{self.restapi_url}/api/v2/serverparks/{server_park}/questionnaires")
        return response.json()

    def get_questionnaire_for_server_park(self, server_park: str, questionnaire_name: str) -> Dict[str, Any]:
        response = requests.get(
            f"{self.restapi_url}/api/v2/serverparks/{server_park}/questionnaires/{questionnaire_name}")
        return response.json()

    def questionnaire_exists_on_server_park(self, server_park: str, questionnaire_name: str) -> bool:
        response = requests.get(
            f"{self.restapi_url}/api/v2/serverparks/{server_park}/questionnaires/{questionnaire_name}/exists")
        return response.json()

    def get_questionnaire_name_from_id(self, server_park: str, questionnaire_id: str) -> Union[Any, None, str]:
        response = requests.get(f"{self.restapi_url}/api/v2/serverparks/{server_park}/questionnaires")
        questionnaire_list = response.json()
        return get_questionnaire_name_from_id(questionnaire_id, questionnaire_list)

    def get_questionnaire_data(self, server_park: str, questionnaire_name: str, data_fields: List) -> Dict[str, Any]:
        data_field_params = []
        for field in data_fields:
            data_field_params.append(("fieldIds", field))
        response = requests.get(
            f"{self.restapi_url}/api/v2/serverparks/{server_park}/questionnaires/{questionnaire_name}/report",
            params=data_field_params)

        return response.json()

    def install_questionnaire(self, server_park: str, questionnaire_file: str) -> Dict[str, Any]:
        response = requests.post(
            f"{self.restapi_url}/api/v2/serverparks/{server_park}/questionnaires",
            json={'questionnaireFile': questionnaire_file})

        return response.json()

    def delete_questionnaire(self, server_park: str, questionnaire_name: str) -> Dict[str, Any]:
        response = requests.delete(
            f"{self.restapi_url}/api/v2/serverparks/{server_park}/questionnaires/{questionnaire_name}")

        return response.json()

    def create_case(self, server_park: str, questionnaire_name: str, case_id: str, data_fields: Dict[str, Any]) -> Dict[
        str, Any]:
        response = requests.post(
            f"{self.restapi_url}/api/v2/serverparks/{server_park}/questionnaires/{questionnaire_name}/cases/{case_id}",
            json=data_fields)

        return response.json()

    def create_multikey_case(self, server_park: str, questionnaire_name: str, key_names: list, key_values: list,
                             data_fields: Dict[str, Any]) -> Dict[str, Any]:
        query_string = self.format_url_query_string(key_names, key_values)
        response = requests.post(
            f"{self.restapi_url}/api/v2/serverparks/{server_park}/questionnaires/{questionnaire_name}/multikey?{query_string}",
            json=data_fields
        )

        return response.json()

    def delete_case(self, server_park: str, questionnaire_name: str, case_id: str) -> Dict[str, Any]:
        response = requests.delete(
            f"{self.restapi_url}/api/v2/serverparks/{server_park}/questionnaires/{questionnaire_name}/cases/{case_id}")

        return response.json()

    def delete_multikey_case(self, server_park: str, questionnaire_name: str, key_names: list, key_values: list) -> Dict[str, Any]:
        query_string = self.format_url_query_string(key_names, key_values)
        response = requests.delete(
            f"{self.restapi_url}/api/v2/serverparks/{server_park}/questionnaires/{questionnaire_name}/multikey?{query_string}"
        )

        return response.json()

    def get_case(self, server_park: str, questionnaire_name: str, case_id: str) -> Dict[str, Any]:
        response = requests.get(
            f"{self.restapi_url}/api/v2/serverparks/{server_park}/questionnaires/{questionnaire_name}/cases/{case_id}")

        if response.status_code != 200:
            raise HTTPError(f"Failed to get {case_id}: {response.status_code} status code")

        return response.json()

    def get_multikey_case(self, server_park: str, questionnaire_name: str, key_names: list, key_values: list) -> Dict[
        str, Any]:
        query_string = self.format_url_query_string(key_names, key_values)
        response = requests.get(
            f"{self.restapi_url}/api/v2/serverparks/{server_park}/questionnaires/{questionnaire_name}/cases/multikey?{query_string}",
        )

        if response.status_code != 200:
            raise HTTPError(f"Failed to get {key_values[1]}: {response.status_code} status code")

        return response.json()

    def case_exists_for_questionnaire(self, server_park: str, questionnaire_name: str, case_id: str) -> bool:
        response = requests.get(
            f"{self.restapi_url}/api/v2/serverparks/{server_park}/questionnaires/{questionnaire_name}/cases/{case_id}/exists")

        return response.json()

    def multikey_case_exists_for_questionnaire(self, server_park: str, questionnaire_name: str, key_names: list, key_values: list) -> bool:
        query_string = self.format_url_query_string(key_names, key_values)
        response = requests.get(
            f"{self.restapi_url}/api/v2/serverparks/{server_park}/questionnaires/{questionnaire_name}/exists/multikey?{query_string}")

        return response.json()

    def patch_case_data(self, server_park: str, questionnaire_name: str, case_id: str, data_fields: dict) -> None:
        response = requests.patch(
            f"{self.restapi_url}/api/v2/serverparks/{server_park}/questionnaires/{questionnaire_name}/cases/{case_id}",
            json=data_fields)

        if response.status_code not in (200, 204):
            raise HTTPError(
                f"Failed to patch {case_id} with {data_fields} for questionnaire {questionnaire_name}: {response.status_code} status code")

    def patch_multikey_case_data(self, server_park: str, questionnaire_name: str, key_names: list, key_values: list, data_fields: dict) -> None:
        query_string = self.format_url_query_string(key_names, key_values)
        response = requests.patch(
            f"{self.restapi_url}/api/v2/serverparks/{server_park}/questionnaires/{questionnaire_name}/cases/multikey?{query_string}",
            json=data_fields)

        if response.status_code not in (200, 204):
            raise HTTPError(
                f"Failed to patch {key_values[1]} with {data_fields} for questionnaire {questionnaire_name}: {response.status_code} status code")

    def get_case_status(self, server_park: str, questionnaire_name: str) -> Dict[str, Any]:
        response = requests.get(
            f"{self.restapi_url}/api/v2/serverparks/{server_park}/questionnaires/{questionnaire_name}/cases/status")
        return response.json()

    def get_users(self) -> Dict[str, Any]:
        response = requests.get(
            f"{self.restapi_url}/api/v2/users")
        return response.json()
