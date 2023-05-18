import pytest

from app.common.constants import NUMBERORDERS

from ..utils.functions import get_random_price, get_random_string


def size_mock() -> dict:
    return {
        'name': get_random_string(),
        'price': get_random_price(10, 20)
    }


@pytest.fixture
def size_uri():
    return '/size/'


@pytest.fixture
def size():
    return size_mock()


@pytest.fixture
def sizes():
    return [size_mock() for _ in range(5)]


@pytest.fixture
def create_size(client, size, size_uri) -> dict:
    response = client.post(size_uri, json=size)
    return response


@pytest.fixture
def get_sizes(client, size_uri) -> list:
    response = client.get(size_uri)
    return response


@pytest.fixture
def create_sizes(client, size_uri) -> list:
    sizes = []
    for _ in range(NUMBERORDERS):
        new_size = client.post(size_uri, json=size_mock())
        sizes.append(new_size.json)
    return sizes
