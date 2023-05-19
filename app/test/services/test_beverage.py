import pytest


def test_create_beverage_service(create_beverage):
    beverage = create_beverage.json
    pytest.assume(create_beverage.status.startswith('200'))
    assert(beverage['_id'])
    assert(beverage['name'])
    assert(beverage['price'])


def test_get_beverage_by_id_service(client, create_beverage, beverage_uri):
    current_beverage = create_beverage.json
    response = client.get(f'{beverage_uri}id/{current_beverage["_id"]}')
    pytest.assume(response.status.startswith('200'))
    returned_beverage = response.json
    for param, value in current_beverage.items():
        assert(returned_beverage[param] == value)


def test_get_beverage_service(client, create_beverages, beverage_uri):
    response = client.get(beverage_uri)
    pytest.assume(response.status.startswith('200'))
    returned_beverages = {beverage['_id']: beverage for beverage in response.json}
    for ingredient in create_beverages:
        assert(ingredient['_id'] in returned_beverages)
