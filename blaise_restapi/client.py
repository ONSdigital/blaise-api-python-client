from typing import Any, Dict, List, Union

import requests
from urllib3.exceptions import HTTPError

from blaise_restapi.functions.questionnaire_functions import (
    get_questionnaire_name_from_id,
)


class Client(object):
    def __init__(self, restapi_url):
        self.restapi_url = restapi_url

    def format_url_query_string(self, key_names: list, key_values: list) -> str:
        query_string = "&".join(
            [f"keyNames={name}" for name in key_names]
            + [f"keyValues={value}" for value in key_values]
        )
        return query_string

    def get_all_questionnaires_with_cati_data(self) -> List[Dict[str, Any]]:
        url = f"{self.restapi_url}/api/v2/cati/questionnaires"
        response = requests.get(url)
        return response.json()

    def get_all_questionnaires_with_cati_data_for_server_park(
        self, server_park: str
    ) -> List[Dict[str, Any]]:
        url = f"{self.restapi_url}/api/v2/cati/serverparks/{server_park}/questionnaires"
        response = requests.get(url)
        return response.json()

    def get_questionnaire_with_cati_data_for_server_park(
        self, server_park: str, questionnaire_name: str
    ) -> Dict[str, Any]:
        url = f"{self.restapi_url}/api/v2/cati/serverparks/{server_park}/questionnaires/{questionnaire_name}"
        response = requests.get(url)
        return response.json()

    def get_all_questionnaires_for_server_park(
        self, server_park: str
    ) -> List[Dict[str, Any]]:
        url = f"{self.restapi_url}/api/v2/serverparks/{server_park}/questionnaires"
        response = requests.get(url)
        return response.json()

    def get_questionnaire_for_server_park(
        self, server_park: str, questionnaire_name: str
    ) -> Dict[str, Any]:
        url = f"{self.restapi_url}/api/v2/serverparks/{server_park}/questionnaires/{questionnaire_name}"
        response = requests.get(url)
        return response.json()

    def questionnaire_exists_on_server_park(
        self, server_park: str, questionnaire_name: str
    ) -> bool:
        url = f"{self.restapi_url}/api/v2/serverparks/{server_park}/questionnaires/{questionnaire_name}/exists"
        response = requests.get(url)
        return response.json()

    def get_questionnaire_name_from_id(
        self, server_park: str, questionnaire_id: str
    ) -> Union[Any, None, str]:
        url = f"{self.restapi_url}/api/v2/serverparks/{server_park}/questionnaires"
        response = requests.get(url)
        questionnaire_list = response.json()
        return get_questionnaire_name_from_id(questionnaire_id, questionnaire_list)

    def get_questionnaire_data(
        self,
        server_park: str,
        questionnaire_name: str,
        data_fields: List,
        filter: str | None = None,
    ) -> Dict[str, Any]:
        data_field_params = []
        for field in data_fields:
            data_field_params.append(("fieldIds", field))
        if filter is not None:
            data_field_params.append(("filter", filter))
        url = f"{self.restapi_url}/api/v2/serverparks/{server_park}/questionnaires/{questionnaire_name}/report"
        response = requests.get(url, params=data_field_params)
        return response.json()

    def install_questionnaire(
        self, server_park: str, questionnaire_file: str
    ) -> Dict[str, Any]:
        url = f"{self.restapi_url}/api/v2/serverparks/{server_park}/questionnaires"
        response = requests.post(url, json={"questionnaireFile": questionnaire_file})
        return response.json()

    def delete_questionnaire(
        self, server_park: str, questionnaire_name: str
    ) -> Dict[str, Any]:
        url = f"{self.restapi_url}/api/v2/serverparks/{server_park}/questionnaires/{questionnaire_name}"
        response = requests.delete(url)
        return response.json()

    def create_case(
        self,
        server_park: str,
        questionnaire_name: str,
        case_id: str,
        data_fields: Dict[str, Any],
    ) -> Dict[str, Any]:
        url = (
            f"{self.restapi_url}/api/v2/serverparks/{server_park}/"
            f"questionnaires/{questionnaire_name}/cases/{case_id}"
        )
        response = requests.post(url, json=data_fields)
        return response.json()

    def create_multikey_case(
        self,
        server_park: str,
        questionnaire_name: str,
        key_names: list,
        key_values: list,
        data_fields: Dict[str, Any],
    ) -> Dict[str, Any]:
        query_string = self.format_url_query_string(key_names, key_values)
        url = (
            f"{self.restapi_url}/api/v2/serverparks/{server_park}/"
            f"questionnaires/{questionnaire_name}/cases/multikey?{query_string}"
        )
        response = requests.post(url, json=data_fields)
        return response.json()

    def delete_case(
        self, server_park: str, questionnaire_name: str, case_id: str
    ) -> Dict[str, Any]:
        url = (
            f"{self.restapi_url}/api/v2/serverparks/{server_park}/"
            f"questionnaires/{questionnaire_name}/cases/{case_id}"
        )
        response = requests.delete(url)
        return response.json()

    def delete_multikey_case(
        self,
        server_park: str,
        questionnaire_name: str,
        key_names: list,
        key_values: list,
    ) -> Dict[str, Any]:
        query_string = self.format_url_query_string(key_names, key_values)
        url = (
            f"{self.restapi_url}/api/v2/serverparks/{server_park}/"
            f"questionnaires/{questionnaire_name}/cases/multikey?{query_string}"
        )
        response = requests.delete(url)
        return response.json()

    def get_case(
        self, server_park: str, questionnaire_name: str, case_id: str
    ) -> Dict[str, Any]:
        url = (
            f"{self.restapi_url}/api/v2/serverparks/{server_park}/"
            f"questionnaires/{questionnaire_name}/cases/{case_id}"
        )
        response = requests.get(url)
        if response.status_code != 200:
            raise HTTPError(
                f"Failed to get {case_id}: {response.status_code} status code"
            )
        return response.json()

    def get_multikey_case(
        self,
        server_park: str,
        questionnaire_name: str,
        key_names: list,
        key_values: list,
    ) -> Dict[str, Any]:
        query_string = self.format_url_query_string(key_names, key_values)
        url = (
            f"{self.restapi_url}/api/v2/serverparks/{server_park}/"
            f"questionnaires/{questionnaire_name}/cases/multikey?{query_string}"
        )
        response = requests.get(url)
        if response.status_code != 200:
            raise HTTPError(
                f"Failed to get {key_values[1]}: {response.status_code} status code"
            )
        return response.json()

    def case_exists_for_questionnaire(
        self, server_park: str, questionnaire_name: str, case_id: str
    ) -> bool:
        url = (
            f"{self.restapi_url}/api/v2/serverparks/{server_park}/"
            f"questionnaires/{questionnaire_name}/cases/{case_id}/exists"
        )
        response = requests.get(url)
        return response.json()

    def multikey_case_exists_for_questionnaire(
        self,
        server_park: str,
        questionnaire_name: str,
        key_names: list,
        key_values: list,
    ) -> bool:
        query_string = self.format_url_query_string(key_names, key_values)
        url = (
            f"{self.restapi_url}/api/v2/serverparks/{server_park}/"
            f"questionnaires/{questionnaire_name}/cases/exists/multikey?{query_string}"
        )
        response = requests.get(url)
        return response.json()

    def patch_case_data(
        self, server_park: str, questionnaire_name: str, case_id: str, data_fields: dict
    ) -> None:
        url = (
            f"{self.restapi_url}/api/v2/serverparks/{server_park}/"
            f"questionnaires/{questionnaire_name}/cases/{case_id}"
        )
        response = requests.patch(url, json=data_fields)
        if response.status_code not in (200, 204):
            raise HTTPError(
                f"Failed to patch {case_id} with {data_fields} for questionnaire {questionnaire_name}: "
                f"{response.status_code} status code"
            )

    def patch_multikey_case_data(
        self,
        server_park: str,
        questionnaire_name: str,
        key_names: list,
        key_values: list,
        data_fields: dict,
    ) -> None:
        query_string = self.format_url_query_string(key_names, key_values)
        url = (
            f"{self.restapi_url}/api/v2/serverparks/{server_park}/"
            f"questionnaires/{questionnaire_name}/cases/multikey?{query_string}"
        )
        response = requests.patch(url, json=data_fields)
        if response.status_code not in (200, 204):
            raise HTTPError(
                f"Failed to patch {key_values[1]} with {data_fields} for questionnaire {questionnaire_name}: "
                f"{response.status_code} status code"
            )

    def get_case_status(
        self, server_park: str, questionnaire_name: str
    ) -> Dict[str, Any]:
        url = (
            f"{self.restapi_url}/api/v2/serverparks/{server_park}/"
            f"questionnaires/{questionnaire_name}/cases/status"
        )
        response = requests.get(url)
        return response.json()

    def get_users(self) -> list[dict[str, Any]]:
        url = f"{self.restapi_url}/api/v2/users"
        response = requests.get(url)
        return response.json()

    def get_ingest(
        self, server_park: str, questionnaire_name: str, data_fields: Dict[str, Any]
    ) -> Dict[str, Any]:
        url = f"{self.restapi_url}/api/v2/serverparks/{server_park}/questionnaires/{questionnaire_name}/ingest"
        response = requests.post(url, json=data_fields)
        return response.json()
