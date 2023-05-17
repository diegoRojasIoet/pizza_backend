import pytest

from app.test.utils.functions import get_random_string, get_random_price


def test_get_size_service(create_sizes, get_sizes):
    pytest.assume(get_sizes.status.startswith('200'))
    returned_sizes = {size['_id']: size for size in get_sizes.json}
    for size in create_sizes:
        assert(size['_id'] in returned_sizes)


def test_create_size_service(create_size):
    size = create_size.json
    pytest.assume(create_size.status.startswith('200'))
    assert(size['_id'])
    assert(size['name'])
    assert(size['price'])


def test_update_size_service(client, create_size, size_uri):
    current_size = create_size.json
    update_data = {**current_size, 'name': get_random_string(), 'price': get_random_price(1, 5)}
    response = client.put(size_uri, json=update_data)
    pytest.assume(response.status.startswith('200'))
    updated_ingredient = response.json
    for param, value in update_data.items():
        assert(updated_ingredient[param] == value)


def test_get__by_id_service(client, create_size, size_uri):
    current_size = create_size.json
    response = client.get(f'{size_uri}id/{current_size["_id"]}')
    pytest.assume(response.status.startswith('200'))
    returned_ingredient = response.json
    for param, value in current_size.items():
        assert(returned_ingredient[param] == value)
