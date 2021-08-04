from blaise_restapi.functions.instrument_functions import get_instrument_name_from_id

from blaise_restapi.stubs.instrument_stubs import api_instruments_stub_response


def test_get_questionnaire_name_from_id(instrument_id, instrument_name):
    assert get_instrument_name_from_id(instrument_id,
                                       api_instruments_stub_response()) == instrument_name


def test_get_questionnaire_name_from_id_not_found():
    assert get_instrument_name_from_id("not-found", api_instruments_stub_response()) == ""
