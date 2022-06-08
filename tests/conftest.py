import pytest

from blaise_restapi.client import Client


@pytest.fixture
def client():
    return Client("http://localhost")


@pytest.fixture
def server_park():
    return "gusty"


@pytest.fixture
def questionnaire_name():
    return "DST2106Y"


@pytest.fixture
def questionnaire_id():
    return "12345-12345-12345-12345-YYYYY"


@pytest.fixture
def data_fields():
    return [
        "QID.Serial_Number",
        "QHAdmin.HOut"
    ]


@pytest.fixture
def questionnaire_file():
    return f"{questionnaire_name}.bpkg"


@pytest.fixture
def case_id():
    return "1000001"


@pytest.fixture
def field_data():
    return {
        "QID.Serial_Number": "QHAdmin.HOut"
        }

@pytest.fixture
def update_telephone_data_fields():
    return {
        "qDataBag.TelNo": "07000 000 01"
    }
