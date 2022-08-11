import responses
import pytest

from urllib3.exceptions import HTTPError

from blaise_restapi.stubs.questionnaire_stubs import api_questionnaires_with_cati_data_stub_response, \
    api_questionnaires_stub_response, api_questionnaire_stub_response, api_questionnaire_with_cati_data_stub_response, \
    api_questionnaire_data_response, api_install_questionnaire_response, api_create_case_response


@responses.activate
def test_get_all_questionnaires_with_cati_data(client):
    responses.add(
        responses.GET,
        f"http://localhost/api/v2/cati/questionnaires",
        json=api_questionnaires_with_cati_data_stub_response())

    result = client.get_all_questionnaires_with_cati_data()
    assert result == api_questionnaires_with_cati_data_stub_response()
    assert len(result) == 2


@responses.activate
def test_get_all_questionnaires_with_cati_data_for_server_park(client, server_park):
    responses.add(
        responses.GET,
        f"http://localhost/api/v2/cati/serverparks/{server_park}/questionnaires",
        json=api_questionnaires_with_cati_data_stub_response())

    result = client.get_all_questionnaires_with_cati_data_for_server_park(server_park)
    assert result == api_questionnaires_with_cati_data_stub_response()
    assert len(result) == 2


@responses.activate
def test_get_questionnaire_with_cati_data_for_server_park(client, server_park, questionnaire_name):
    responses.add(
        responses.GET,
        f"http://localhost/api/v2/cati/serverparks/{server_park}/questionnaires/{questionnaire_name}",
        json=api_questionnaires_with_cati_data_stub_response())

    result = client.get_questionnaire_with_cati_data_for_server_park(server_park, questionnaire_name)
    assert result == api_questionnaires_with_cati_data_stub_response()


@responses.activate
def test_get_all_questionnaires_for_server_park(client, server_park):
    responses.add(
        responses.GET,
        f"http://localhost/api/v2/serverparks/{server_park}/questionnaires",
        json=api_questionnaires_stub_response())

    result = client.get_all_questionnaires_for_server_park(server_park)
    assert result == api_questionnaires_stub_response()
    assert len(result) == 3


@responses.activate
def test_get_questionnaire_for_server_park(client, server_park, questionnaire_name):
    responses.add(
        responses.GET,
        f"http://localhost/api/v2/serverparks/{server_park}/questionnaires/{questionnaire_name}",
        json=api_questionnaire_stub_response())

    result = client.get_questionnaire_for_server_park(server_park, questionnaire_name)
    assert result == api_questionnaire_stub_response()


@responses.activate
def test_questionnaire_exists_on_server_park_returns_true_if_exists(client, server_park, questionnaire_name):
    responses.add(
        responses.GET,
        f"http://localhost/api/v2/serverparks/{server_park}/questionnaires/{questionnaire_name}/exists",
        json=True)

    result = client.questionnaire_exists_on_server_park(server_park, questionnaire_name)
    assert result is True


@responses.activate
def test_questionnaire_exists_on_server_park_returns_false_if_it_does_not_exist(client, server_park):
    responses.add(
        responses.GET,
        f"http://localhost/api/v2/serverparks/{server_park}/questionnaires/notfound/exists",
        json=False)

    result = client.questionnaire_exists_on_server_park(server_park, "notfound")
    assert result is False


@responses.activate
def test_get_questionnaire_name_from_id(client, server_park, questionnaire_id, questionnaire_name):
    responses.add(
        responses.GET,
        f"http://localhost/api/v2/serverparks/{server_park}/questionnaires",
        json=api_questionnaires_stub_response())

    result = client.get_questionnaire_name_from_id(server_park, questionnaire_id)
    assert result == questionnaire_name


@responses.activate
def test_get_questionnaire_data(client, server_park, questionnaire_name, data_fields):
    responses.add(
        responses.GET,
        f"http://localhost/api/v2/serverparks/{server_park}/questionnaires/{questionnaire_name}/report",
        json=api_questionnaire_data_response())

    result = client.get_questionnaire_data(server_park, questionnaire_name, data_fields)
    assert result == api_questionnaire_data_response()


@responses.activate
def test_install_questionnaire(client, server_park, questionnaire_file):
    responses.add(
        responses.POST,
        f"http://localhost/api/v2/serverparks/{server_park}/questionnaires",
        json=api_install_questionnaire_response())

    result = client.install_questionnaire(server_park, questionnaire_file)
    assert result == api_install_questionnaire_response()


@responses.activate
def test_delete_questionnaire(client, server_park, questionnaire_name):
    responses.add(
        responses.DELETE,
        f"http://localhost/api/v2/serverparks/{server_park}/questionnaires/{questionnaire_name}",
        json={})

    result = client.delete_questionnaire(server_park, questionnaire_name)
    assert result == {}


@responses.activate
def test_create_case(client, server_park, questionnaire_name, case_id, field_data):
    responses.add(
        responses.POST,
        f"http://localhost/api/v2/serverparks/{server_park}/questionnaires/{questionnaire_name}/cases/{case_id}",
        json=api_create_case_response())

    result = client.create_case(server_park, questionnaire_name, case_id, field_data)
    assert result == api_create_case_response()


@responses.activate
def test_delete_case(client, server_park, questionnaire_name, case_id):
    responses.add(
        responses.DELETE,
        f"http://localhost/api/v2/serverparks/{server_park}/questionnaires/{questionnaire_name}/cases/{case_id}",
        json={})

    result = client.delete_case(server_park, questionnaire_name, case_id)
    assert result == {}


@responses.activate
def test_get_case(client, server_park, questionnaire_name, case_id):
    responses.add(
        responses.GET,
        f"http://localhost/api/v2/serverparks/{server_park}/questionnaires/{questionnaire_name}/cases/{case_id}",
        json={
                "caseId": "12345",
                "fieldData": {}
            })

    result = client.get_case(server_park, questionnaire_name, case_id)
    assert result == {
                "caseId": "12345",
                "fieldData": {}
            }


@responses.activate
def test_get_case_when_case_not_found(client, server_park, questionnaire_name, case_id):
    responses.add(
        responses.GET,
        f"http://localhost/api/v2/serverparks/{server_park}/questionnaires/{questionnaire_name}/cases/{case_id}",
        status=404
        )
    with pytest.raises(HTTPError):
        client.get_case(server_park, questionnaire_name, case_id)
    

@responses.activate
def test_patch_case_data_happy_path(client, server_park, questionnaire_name, case_id, update_telephone_data_fields):
    responses.add(
        responses.PATCH,
        f"http://localhost/api/v2/serverparks/{server_park}/questionnaires/{questionnaire_name}/cases/{case_id}"
    )

    assert client.patch_case_data(server_park, questionnaire_name, case_id, update_telephone_data_fields) is None


@responses.activate
def test_patch_case_data_raises_error(client, server_park, questionnaire_name, case_id, update_telephone_data_fields):
    responses.add(
        responses.PATCH,
        f"http://localhost/api/v2/serverparks/{server_park}/questionnaires/{questionnaire_name}/cases/{case_id}",
        status=500
    )

    with pytest.raises(HTTPError) as err:
        client.patch_case_data(server_park, questionnaire_name, case_id, update_telephone_data_fields)

    assert str(err.value) == "Failed to patch 1000001 with {'qDataBag.TelNo': '07000 000 01'}: 500 status code"
