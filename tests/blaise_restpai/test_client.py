import responses

from blaise_restapi.stubs.instrument_stubs import api_questionnaires_stub_response

@responses.activate
def test_get_all_questionnaires_from_server_park(client, server_park):
    responses.add(
        responses.GET,
        f"http://localhost/api/v1/serverparks/{server_park}/instruments",
        json=api_questionnaires_stub_response(),)

    result = client.get_all_questionnaires_from_server_park(server_park)
    assert result == api_questionnaires_stub_response()
    assert len(result) == 3
