import responses


@responses.activate
def test_get_all_questionnaires_from_server_park(client, server_park, api_questionnaires_response):
    responses.add(
        responses.GET,
        f"http://localhost/api/v1/serverparks/{server_park}/instruments",
        json=api_questionnaires_response,)

    result = client.get_all_questionnaires_from_server_park(server_park)
    assert result == api_questionnaires_response
    assert len(result) == 3
