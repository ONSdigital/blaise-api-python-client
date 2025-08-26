from blaise_restapi.functions.questionnaire_functions import (
    get_questionnaire_name_from_id,
)
from blaise_restapi.stubs.questionnaire_stubs import api_questionnaires_stub_response


def test_get_questionnaire_name_from_id(questionnaire_id, questionnaire_name):
    assert (
        get_questionnaire_name_from_id(
            questionnaire_id, api_questionnaires_stub_response()
        )
        == questionnaire_name
    )


def test_get_questionnaire_name_from_id_not_found():
    assert (
        get_questionnaire_name_from_id("not-found", api_questionnaires_stub_response())
        == ""
    )
