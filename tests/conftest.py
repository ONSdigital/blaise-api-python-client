import pytest

from blaise_restapi.client import Client


@pytest.fixture
def client() -> Client:
    return Client("http://localhost")


@pytest.fixture
def server_park() -> str:
    return "gusty"


@pytest.fixture
def questionnaire_name() -> str:
    return "DST2106Y"


@pytest.fixture
def questionnaire_id() -> str:
    return "12345-12345-12345-12345-YYYYY"


@pytest.fixture
def data_fields() -> list[str]:
    return ["QID.Serial_Number", "QHAdmin.HOut"]


@pytest.fixture
def questionnaire_file() -> str:
    return f"{questionnaire_name}.bpkg"


@pytest.fixture
def case_id() -> str:
    return "1000001"


@pytest.fixture
def field_data() -> dict[str, str]:
    return {"QID.Serial_Number": "QHAdmin.HOut"}


@pytest.fixture
def update_telephone_data_fields() -> dict[str, str]:
    return {"qDataBag.TelNo": "07000 000 01"}


@pytest.fixture
def key_names() -> list[str]:
    return ["MainSurveyID", "ID"]


@pytest.fixture
def key_values() -> list[str]:
    return ["12345-12345-12345-12345", "1000001"]
