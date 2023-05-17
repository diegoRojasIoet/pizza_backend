import pytest


def test_create_order_service(create_order):
    created_order = create_order.json
    pytest.assume(create_order.status.startswith('200'))
    assert(created_order['_id'])
    assert(created_order['client_name'])
    assert(created_order['client_dni'])
    assert(created_order['client_address'])
    assert(created_order['client_phone'])
    assert(created_order['date'])
    assert(created_order['total_price'])
    assert(created_order['size'])
    assert(created_order['detail'])


def test_get_order_by_id_service(client, create_order, order_uri):
    created_order = create_order.json
    response = client.get(f'{order_uri}id/{created_order["_id"]}')
    pytest.assume(response.status.startswith('200'))
    returned_order = response.json
    for param, value in created_order.items():
        assert(returned_order[param] == value)


def test_get_order_service(client, create_orders, order_uri):
    response = client.get(order_uri)
    pytest.assume(response.status.startswith('200'))
    returned_orders = {order['_id']: order for order in response.json}
    for order in create_orders:
        assert(order['_id'] in returned_orders)
