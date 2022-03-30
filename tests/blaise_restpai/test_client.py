import responses

from blaise_restapi.stubs.instrument_stubs import api_instruments_with_cati_data_stub_response, \
    api_instruments_stub_response, api_instrument_stub_response, api_instrument_with_cati_data_stub_response, \
    api_instrument_data_response


@responses.activate
def test_get_all_instruments_with_cati_data(client):
    responses.add(
        responses.GET,
        f"http://localhost/api/v1/cati/instruments",
        json=api_instruments_with_cati_data_stub_response())

    result = client.get_all_instruments_with_cati_data()
    assert result == api_instruments_with_cati_data_stub_response()
    assert len(result) == 2


@responses.activate
def test_get_all_instruments_with_cati_data_for_server_park(client, server_park):
    responses.add(
        responses.GET,
        f"http://localhost/api/v1/cati/serverparks/{server_park}/instruments",
        json=api_instruments_with_cati_data_stub_response())

    result = client.get_all_instruments_with_cati_data_for_server_park(server_park)
    assert result == api_instruments_with_cati_data_stub_response()
    assert len(result) == 2


@responses.activate
def test_get_instrument_with_cati_data_for_server_park(client, server_park, instrument_name):
    responses.add(
        responses.GET,
        f"http://localhost/api/v1/cati/serverparks/{server_park}/instruments/{instrument_name}",
        json=api_instrument_with_cati_data_stub_response())

    result = client.get_instrument_with_cati_data_for_server_park(server_park, instrument_name)
    assert result == api_instrument_with_cati_data_stub_response()


@responses.activate
def test_get_all_instruments_for_server_park(client, server_park):
    responses.add(
        responses.GET,
        f"http://localhost/api/v1/serverparks/{server_park}/instruments",
        json=api_instruments_stub_response())

    result = client.get_all_instruments_for_server_park(server_park)
    assert result == api_instruments_stub_response()
    assert len(result) == 3


@responses.activate
def test_get_instrument_for_server_park(client, server_park, instrument_name):
    responses.add(
        responses.GET,
        f"http://localhost/api/v1/serverparks/{server_park}/instruments/{instrument_name}",
        json=api_instrument_stub_response())

    result = client.get_instrument_for_server_park(server_park, instrument_name)
    assert result == api_instrument_stub_response()


@responses.activate
def test_instrument_exists_on_server_park_returns_true_if_exists(client, server_park, instrument_name):
    responses.add(
        responses.GET,
        f"http://localhost/api/v1/serverparks/{server_park}/instruments/{instrument_name}/exists",
        json=True)

    result = client.instrument_exists_on_server_park(server_park, instrument_name)
    assert result is True


@responses.activate
def test_instrument_exists_on_server_park_returns_false_if_it_does_not_exist(client, server_park):
    responses.add(
        responses.GET,
        f"http://localhost/api/v1/serverparks/{server_park}/instruments/notfound/exists",
        json=False)

    result = client.instrument_exists_on_server_park(server_park, "notfound")
    assert result is False


@responses.activate
def test_get_instrument_name_from_id(client, server_park, instrument_id, instrument_name):
    responses.add(
        responses.GET,
        f"http://localhost/api/v1/serverparks/{server_park}/instruments",
        json=api_instruments_stub_response())

    result = client.get_instrument_name_from_id(server_park, instrument_id)
    assert result == instrument_name


@responses.activate
def test_get_instrument_data(client, server_park, instrument_name, data_fields):
    responses.add(
        responses.GET,
        f"http://localhost/api/v1/serverparks/{server_park}/instruments/{instrument_name}/report",
        json=api_instrument_data_response())

    result = client.get_instrument_data(server_park, instrument_name, data_fields)
    assert result == api_instrument_data_response()


@responses.activate
def test_patch_case_data(client, server_park, instrument_name, case_id):
    responses.add(
        responses.PATCH,
        f"http://localhost/api/v1/serverparks/{server_park}/instruments/{instrument_name}/cases/{case_id}")

    telephone_data = {
        "qDataBag.TelNo": "07000 000 01"
    }

    assert client.patch_case_data(server_park, instrument_name, case_id, telephone_data) is None
