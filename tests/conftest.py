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
    return "OPN2101A"