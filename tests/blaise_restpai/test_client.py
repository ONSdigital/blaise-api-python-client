import responses

from blaise_restapi.stubs.instrument_stubs import api_questionnaires_with_cati_data_stub_response, \
    api_questionnaires_stub_response, api_questionnaire_stub_response, api_questionnaire_with_cati_data_stub_response


@responses.activate
def test_get_all_questionnaires_with_cati_data(client):
    responses.add(
        responses.GET,
        f"http://localhost/api/v1/cati/instruments",
        json=api_questionnaires_with_cati_data_stub_response())

    result = client.get_all_questionnaires_with_cati_data()
    assert result == api_questionnaires_with_cati_data_stub_response()
    assert len(result) == 2


@responses.activate
def test_get_all_questionnaires_with_cati_data_for_server_park(client, server_park):
    responses.add(
        responses.GET,
        f"http://localhost/api/v1/cati/serverparks/{server_park}/instruments",
        json=api_questionnaires_with_cati_data_stub_response())

    result = client.get_all_questionnaires_with_cati_data_for_server_park(server_park)
    assert result == api_questionnaires_with_cati_data_stub_response()
    assert len(result) == 2


@responses.activate
def test_get_questionnaire_with_cati_data_for_server_park(client, server_park, instrument_name):
    responses.add(
        responses.GET,
        f"http://localhost/api/v1/cati/serverparks/{server_park}/instruments/{instrument_name}",
        json=api_questionnaire_with_cati_data_stub_response())

    result = client.get_questionnaire_with_cati_data_for_server_park(server_park, instrument_name)
    assert result == api_questionnaire_with_cati_data_stub_response()


@responses.activate
def test_get_all_questionnaires_for_server_park(client, server_park):
    responses.add(
        responses.GET,
        f"http://localhost/api/v1/serverparks/{server_park}/instruments",
        json=api_questionnaires_stub_response())

    result = client.get_all_questionnaires_for_server_park(server_park)
    assert result == api_questionnaires_stub_response()
    assert len(result) == 3


@responses.activate
def test_get_questionnaire_for_server_park(client, server_park, instrument_name):
    responses.add(
        responses.GET,
        f"http://localhost/api/v1/serverparks/{server_park}/instruments/{instrument_name}",
        json=api_questionnaire_stub_response())

    result = client.get_questionnaire_for_server_park(server_park, instrument_name)
    assert result == api_questionnaire_stub_response()
