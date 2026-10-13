import pytest
import responses
from urllib3.exceptions import HTTPError

from blaise_restapi.client import Client
from blaise_restapi.stubs.questionnaire_stubs import (
    api_create_case_response,
    api_ingest_response,
    api_install_questionnaire_response,
    api_questionnaire_data_response,
    api_questionnaire_stub_response,
    api_questionnaires_stub_response,
    api_questionnaires_with_cati_data_stub_response,
)


@responses.activate
def test_get_all_questionnaires_with_cati_data(client: Client) -> None:
    responses.add(
        responses.GET,
        "http://localhost/api/v2/cati/questionnaires",
        json=api_questionnaires_with_cati_data_stub_response(),
    )

    result = client.get_all_questionnaires_with_cati_data()
    assert result == api_questionnaires_with_cati_data_stub_response()


@responses.activate
def test_get_all_questionnaires_with_cati_data_for_server_park(
    client: Client, server_park: str
) -> None:
    responses.add(
        responses.GET,
        f"http://localhost/api/v2/cati/serverparks/{server_park}/questionnaires",
        json=api_questionnaires_with_cati_data_stub_response(),
    )

    result = client.get_all_questionnaires_with_cati_data_for_server_park(server_park)
    assert result == api_questionnaires_with_cati_data_stub_response()


@responses.activate
def test_get_questionnaire_with_cati_data_for_server_park(
    client: Client, server_park: str, questionnaire_name: str
) -> None:
    responses.add(
        responses.GET,
        f"http://localhost/api/v2/cati/serverparks/{server_park}/questionnaires/{questionnaire_name}",
        json=api_questionnaires_with_cati_data_stub_response(),
    )

    result = client.get_questionnaire_with_cati_data_for_server_park(
        server_park, questionnaire_name
    )
    assert result == api_questionnaires_with_cati_data_stub_response()


@responses.activate
def test_get_all_questionnaires_for_server_park(
    client: Client, server_park: str
) -> None:
    responses.add(
        responses.GET,
        f"http://localhost/api/v2/serverparks/{server_park}/questionnaires",
        json=api_questionnaires_stub_response(),
    )

    result = client.get_all_questionnaires_for_server_park(server_park)
    assert result == api_questionnaires_stub_response()


@responses.activate
def test_get_questionnaire_for_server_park(
    client: Client, server_park: str, questionnaire_name: str
) -> None:
    responses.add(
        responses.GET,
        f"http://localhost/api/v2/serverparks/{server_park}/questionnaires/{questionnaire_name}",
        json=api_questionnaire_stub_response(),
    )

    result = client.get_questionnaire_for_server_park(server_park, questionnaire_name)
    assert result == api_questionnaire_stub_response()


@responses.activate
def test_questionnaire_exists_on_server_park_returns_true_if_exists(
    client: Client, server_park: str, questionnaire_name: str
) -> None:
    responses.add(
        responses.GET,
        f"http://localhost/api/v2/serverparks/{server_park}/questionnaires/{questionnaire_name}/exists",
        json=True,
    )

    result = client.questionnaire_exists_on_server_park(server_park, questionnaire_name)
    assert result is True


@responses.activate
def test_questionnaire_exists_on_server_park_returns_false_if_it_does_not_exist(
    client: Client, server_park: str
) -> None:
    responses.add(
        responses.GET,
        f"http://localhost/api/v2/serverparks/{server_park}/questionnaires/notfound/exists",
        json=False,
    )

    result = client.questionnaire_exists_on_server_park(server_park, "notfound")
    assert result is False


@responses.activate
def test_get_questionnaire_name_from_id(
    client: Client, server_park: str, questionnaire_id: str, questionnaire_name: str
) -> None:
    responses.add(
        responses.GET,
        f"http://localhost/api/v2/serverparks/{server_park}/questionnaires",
        json=api_questionnaires_stub_response(),
    )

    result = client.get_questionnaire_name_from_id(server_park, questionnaire_id)
    assert result == questionnaire_name


@responses.activate
def test_get_questionnaire_data(
    client: Client, server_park: str, questionnaire_name: str, data_fields: list[str]
) -> None:
    responses.add(
        responses.GET,
        f"http://localhost/api/v2/serverparks/{server_park}/questionnaires/{questionnaire_name}/report",
        json=api_questionnaire_data_response(),
    )

    result = client.get_questionnaire_data(server_park, questionnaire_name, data_fields)
    assert result == api_questionnaire_data_response()


@responses.activate
def test_get_questionnaire_data_with_filter(
    client: Client, server_park: str, questionnaire_name: str, data_fields: list[str]
) -> None:
    responses.add(
        responses.GET,
        f"http://localhost/api/v2/serverparks/{server_park}/questionnaires/{questionnaire_name}/report",
        json=api_questionnaire_data_response(),
    )

    result = client.get_questionnaire_data(
        server_park, questionnaire_name, data_fields, "ID=2"
    )
    assert result == api_questionnaire_data_response()


@responses.activate
def test_install_questionnaire(
    client: Client, server_park: str, questionnaire_file: str
) -> None:
    responses.add(
        responses.POST,
        f"http://localhost/api/v2/serverparks/{server_park}/questionnaires",
        json=api_install_questionnaire_response(),
    )

    result = client.install_questionnaire(server_park, questionnaire_file)
    assert result == api_install_questionnaire_response()


@responses.activate
def test_delete_questionnaire(
    client: Client, server_park: str, questionnaire_name: str
) -> None:
    responses.add(
        responses.DELETE,
        f"http://localhost/api/v2/serverparks/{server_park}/questionnaires/{questionnaire_name}",
        json={},
    )

    result = client.delete_questionnaire(server_park, questionnaire_name)
    assert result == {}


@responses.activate
def test_create_case(
    client: Client,
    server_park: str,
    questionnaire_name: str,
    case_id: str,
    field_data: dict[str, str],
) -> None:
    responses.add(
        responses.POST,
        f"http://localhost/api/v2/serverparks/{server_park}/questionnaires/{questionnaire_name}/cases/{case_id}",
        json=api_create_case_response(),
    )

    result = client.create_case(server_park, questionnaire_name, case_id, field_data)
    assert result == api_create_case_response()


@responses.activate
def test_create_multikey_case(
    client: Client,
    server_park: str,
    questionnaire_name: str,
    key_names: list[str],
    key_values: list[str],
    field_data: dict[str, str],
) -> None:
    responses.add(
        responses.POST,
        "http://localhost/api/v2/serverparks/gusty/questionnaires/DST2106Y/cases/multikey?keyNames=MainSurveyID&keyNames=ID&keyValues=12345-12345-12345-12345&keyValues=1000001",
        json=api_create_case_response(),
    )

    result = client.create_multikey_case(
        server_park, questionnaire_name, key_names, key_values, field_data
    )
    assert result == api_create_case_response()


@responses.activate
def test_delete_case(
    client: Client, server_park: str, questionnaire_name: str, case_id: str
) -> None:
    responses.add(
        responses.DELETE,
        f"http://localhost/api/v2/serverparks/{server_park}/questionnaires/{questionnaire_name}/cases/{case_id}",
        json={},
    )

    result = client.delete_case(server_park, questionnaire_name, case_id)
    assert result == {}


@responses.activate
def test_delete_case_with_multikey(
    client: Client,
    server_park: str,
    questionnaire_name: str,
    key_names: list[str],
    key_values: list[str],
) -> None:
    responses.add(
        responses.DELETE,
        "http://localhost/api/v2/serverparks/gusty/questionnaires/DST2106Y/cases/multikey?keyNames=MainSurveyID&keyNames=ID&keyValues=12345-12345-12345-12345&keyValues=1000001",
        json={},
    )

    result = client.delete_multikey_case(
        server_park, questionnaire_name, key_names, key_values
    )
    assert result == {}


@responses.activate
def test_get_case(
    client: Client, server_park: str, questionnaire_name: str, case_id: str
) -> None:
    responses.add(
        responses.GET,
        f"http://localhost/api/v2/serverparks/{server_park}/questionnaires/{questionnaire_name}/cases/{case_id}",
        json={"caseId": "12345", "fieldData": {}},
    )

    result = client.get_case(server_park, questionnaire_name, case_id)
    assert result == {"caseId": "12345", "fieldData": {}}


@responses.activate
def test_get_multikey_case(
    client: Client,
    server_park: str,
    questionnaire_name: str,
    key_names: list[str],
    key_values: list[str],
) -> None:
    responses.add(
        responses.GET,
        "http://localhost/api/v2/serverparks/gusty/questionnaires/DST2106Y/cases/multikey?keyNames=MainSurveyID&keyNames=ID&keyValues=12345-12345-12345-12345&keyValues=1000001",
        json={"fieldData": {}},
        status=200,
    )

    result = client.get_multikey_case(
        server_park, questionnaire_name, key_names, key_values
    )
    assert result == {"fieldData": {}}


@responses.activate
def test_get_case_when_case_not_found(
    client: Client, server_park: str, questionnaire_name: str, case_id: str
) -> None:
    responses.add(
        responses.GET,
        f"http://localhost/api/v2/serverparks/{server_park}/questionnaires/{questionnaire_name}/cases/{case_id}",
        status=404,
    )
    with pytest.raises(HTTPError):
        client.get_case(server_park, questionnaire_name, case_id)


@responses.activate
def test_get_multikey_case_when_case_not_found(
    client: Client,
    server_park: str,
    questionnaire_name: str,
    key_names: list[str],
    key_values: list[str],
) -> None:
    responses.add(
        responses.GET,
        "http://localhost/api/v2/serverparks/gusty/questionnaires/DST2106Y/cases/multikey?keyNames=MainSurveyID&keyNames=ID&keyValues=12345-12345-12345-12345&keyValues=1000001",
        status=404,
    )
    with pytest.raises(HTTPError):
        client.get_multikey_case(server_park, questionnaire_name, key_names, key_values)


@responses.activate
def test_get_case_when_case_errors(
    client: Client, server_park: str, questionnaire_name: str, case_id: str
) -> None:
    responses.add(
        responses.GET,
        f"http://localhost/api/v2/serverparks/{server_park}/questionnaires/{questionnaire_name}/cases/{case_id}",
        status=500,
    )
    with pytest.raises(HTTPError):
        client.get_case(server_park, questionnaire_name, case_id)


@responses.activate
def test_get_mulitkey_case_when_case_errors(
    client: Client,
    server_park: str,
    questionnaire_name: str,
    key_names: list[str],
    key_values: list[str],
) -> None:
    responses.add(
        responses.GET,
        "http://localhost/api/v2/serverparks/gusty/questionnaires/DST2106Y/cases/multikey?keyNames=MainSurveyID&keyNames=ID&keyValues=12345-12345-12345-12345&keyValues=1000001",
        status=500,
    )
    with pytest.raises(HTTPError):
        client.get_multikey_case(server_park, questionnaire_name, key_names, key_values)


@responses.activate
def test_case_exists_for_questionnaire_returns_true_if_exists(
    client: Client, server_park: str, questionnaire_name: str, case_id: str
) -> None:
    responses.add(
        responses.GET,
        f"http://localhost/api/v2/serverparks/{server_park}/questionnaires/{questionnaire_name}/cases/{case_id}/exists",
        json=True,
    )

    result = client.case_exists_for_questionnaire(
        server_park, questionnaire_name, case_id
    )
    assert result is True


@responses.activate
def test_multikey_case_exists_for_questionnaire_returns_true_if_exists(
    client: Client,
    server_park: str,
    questionnaire_name: str,
    key_names: list[str],
    key_values: list[str],
) -> None:
    responses.add(
        responses.GET,
        "http://localhost/api/v2/serverparks/gusty/questionnaires/DST2106Y/cases/exists/multikey?keyNames=MainSurveyID&keyNames=ID&keyValues=12345-12345-12345-12345&keyValues=1000001",
        json=True,
    )

    result = client.multikey_case_exists_for_questionnaire(
        server_park, questionnaire_name, key_names, key_values
    )
    assert result is True


@responses.activate
def test_case_exists_for_questionnaire_returns_false_if_it_does_not_exist(
    client: Client, server_park: str, questionnaire_name: str
) -> None:
    responses.add(
        responses.GET,
        f"http://localhost/api/v2/serverparks/{server_park}/questionnaires/{questionnaire_name}/cases/notfound/exists",
        json=False,
    )

    result = client.case_exists_for_questionnaire(
        server_park, questionnaire_name, "notfound"
    )
    assert result is False


@responses.activate
def test_multikey_case_exists_for_questionnaire_returns_false_if_it_does_not_exist(
    client: Client, server_park: str, questionnaire_name: str
) -> None:
    responses.add(
        responses.GET,
        "http://localhost/api/v2/serverparks/gusty/questionnaires/DST2106Y/cases/exists/multikey",
        json=False,
    )

    result = client.multikey_case_exists_for_questionnaire(
        server_park, questionnaire_name, ["notfound"], ["notfound"]
    )
    assert result is False


@responses.activate
def test_patch_case_data_happy_path(
    client: Client,
    server_park: str,
    questionnaire_name: str,
    case_id: str,
    update_telephone_data_fields: dict[str, str],
) -> None:
    responses.add(
        responses.PATCH,
        f"http://localhost/api/v2/serverparks/{server_park}/questionnaires/{questionnaire_name}/cases/{case_id}",
        json={},
    )

    assert (
        client.patch_case_data(
            server_park, questionnaire_name, case_id, update_telephone_data_fields
        )
        is None
    )


@responses.activate
def test_patch_multikey_case_data_happy_path(
    client: Client,
    server_park: str,
    questionnaire_name: str,
    key_names: list[str],
    key_values: list[str],
    update_telephone_data_fields: dict[str, str],
) -> None:
    responses.add(
        responses.PATCH,
        "http://localhost/api/v2/serverparks/gusty/questionnaires/DST2106Y/cases/multikey?keyNames=MainSurveyID&keyNames=ID&keyValues=12345-12345-12345-12345&keyValues=1000001",
        status=204,
    )

    assert (
        client.patch_multikey_case_data(
            server_park,
            questionnaire_name,
            key_names,
            key_values,
            update_telephone_data_fields,
        )
        is None
    )


@responses.activate
def test_patch_case_data_raises_error(
    client: Client,
    server_park: str,
    questionnaire_name: str,
    case_id: str,
    update_telephone_data_fields: dict[str, str],
) -> None:
    responses.add(
        responses.PATCH,
        f"http://localhost/api/v2/serverparks/{server_park}/questionnaires/{questionnaire_name}/cases/{case_id}",
        status=500,
    )

    with pytest.raises(HTTPError) as err:
        client.patch_case_data(
            server_park, questionnaire_name, case_id, update_telephone_data_fields
        )

    assert (
        str(err.value)
        == "Failed to patch 1000001 with {'qDataBag.TelNo': '07000 000 01'} "
        "for questionnaire DST2106Y: 500 status code"
    )


@responses.activate
def test_patch_multikey_case_data_raises_error(
    client: Client,
    server_park: str,
    questionnaire_name: str,
    key_names: list[str],
    key_values: list[str],
    update_telephone_data_fields: dict[str, str],
) -> None:
    responses.add(
        responses.PATCH,
        "http://localhost/api/v2/serverparks/gusty/questionnaires/DST2106Y/cases/multikey?keyNames=MainSurveyID&keyNames=ID&keyValues=12345-12345-12345-12345&keyValues=1000001",
        status=500,
    )

    with pytest.raises(HTTPError) as err:
        client.patch_multikey_case_data(
            server_park,
            questionnaire_name,
            key_names,
            key_values,
            update_telephone_data_fields,
        )

    assert (
        str(err.value)
        == "Failed to patch 1000001 with {'qDataBag.TelNo': '07000 000 01'} "
        "for questionnaire DST2106Y: 500 status code"
    )


@responses.activate
def test_get_case_status(
    client: Client, server_park: str, questionnaire_name: str
) -> None:
    responses.add(
        responses.GET,
        f"http://localhost/api/v2/serverparks/{server_park}/questionnaires/{questionnaire_name}/cases/status",
        json={"primaryKey": "12345", "outcome": 0},
    )

    result = client.get_case_status(server_park, questionnaire_name)
    assert result == {"primaryKey": "12345", "outcome": 0}


@responses.activate
def test_get_users(client: Client) -> None:
    responses.add(
        responses.GET,
        "http://localhost/api/v2/users",
        json={
            "name": "rich",
            "role": "DST",
            "serverParks": ["gusty", "cma"],
            "defaultServerPark": "gusty",
        },
    )

    result = client.get_users()
    assert result == {
        "defaultServerPark": "gusty",
        "name": "rich",
        "role": "DST",
        "serverParks": ["gusty", "cma"],
    }


@responses.activate
def test_format_url_query_string(
    client: Client, key_names: list[str], key_values: list[str]
) -> None:
    assert client.format_url_query_string(key_names, key_values) == (
        "keyNames=MainSurveyID&keyNames=ID&keyValues=12345-12345-12345-12345&keyValues=1000001"
    )


@responses.activate
def test_ingest(
    client: Client,
    server_park: str,
    questionnaire_name: str,
    field_data: dict[str, str],
) -> None:
    responses.add(
        responses.POST,
        f"http://localhost/api/v2/serverparks/{server_park}/questionnaires/{questionnaire_name}/ingest",
        json=api_ingest_response(),
    )

    result = client.get_ingest(server_park, questionnaire_name, field_data)
    assert result == api_ingest_response()

    # f"{self.restapi_url}/api/v2/serverparks/{server_park}/questionnaires/{questionnaire_name}/ingest",  # noqa: E501
