import pytest

from blaise_restapi.client import Client


@pytest.fixture
def client():
    return Client("http://localhost")


@pytest.fixture
def server_park():
    return "gusty"


@pytest.fixture
def instrument_name():
    return "DST2106Y"


@pytest.fixture
def instrument_id():
    return "12345-12345-12345-12345-YYYYY"