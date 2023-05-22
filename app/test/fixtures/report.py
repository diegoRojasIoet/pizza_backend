import pytest
import pandas as pd


def orders_data_frame_row_mock() -> dict:
    return {'_id': 1,
            'client_address': 'vpqkwenjrz',
            'client_dni': '2877374003',
            'client_name': 'nhweotpqkz',
            'client_phone': '5447470741',
            'date': '2023-05-20T17:59:41.824299',
            'detail': [
                {'beverage': None, 'ingredient_price': 16.29, 'beverage_price': None, 'ingredient': {'name': 'bltivmhfyx', 'price': 15.6, '_id': 2}},
                {'beverage': None, 'ingredient_price': 15.68, 'beverage_price': None, 'ingredient': {'name': 'ingredient2', 'price': 15.6, '_id': 2}},
                {'beverage': None, 'ingredient_price': 17.86, 'beverage_price': None, 'ingredient': {'name': 'ingredient3', 'price': 15.6, '_id': 2}},
                {'beverage': None, 'ingredient_price': 17.38, 'beverage_price': None, 'ingredient': {'name': 'ingredient4', 'price': 15.6, '_id': 2}},
                {'beverage': {'name': 'beverage1', 'price': 15.6, '_id': 2}, 'ingredient_price': None, 'beverage_price': 12.25, 'ingredient': None},
                {'beverage': {'name': 'beverage1', 'price': 15.6, '_id': 2}, 'ingredient_price': None, 'beverage_price': 19.38, 'ingredient': None},
                {'beverage': {'name': 'beverage2', 'price': 15.6, '_id': 2}, 'ingredient_price': None, 'beverage_price': 16.04, 'ingredient': None}
            ],
            'size': {'name': 'bltivmhfyx', 'price': 15.6, '_id': 2},
            'total_price': 156.32}


def orders_data_frame_mock() -> dict:
    return [
        {'_id': 1,
            'client_address': 'vpqkwenjrz',
            'client_dni': '2877374003',
            'client_name': 'nhweotpqkz',
            'client_phone': '5447470741',
            'date': '2023-05-20T17:59:41.824299',
            'detail': [
                {'beverage': None, 'ingredient_price': 16.29, 'beverage_price': None, 'ingredient': {'name': 'bltivmhfyx', 'price': 15.6, '_id': 2}},
                {'beverage': None, 'ingredient_price': 15.68, 'beverage_price': None, 'ingredient': {'name': 'ingredient2', 'price': 15.6, '_id': 2}},
                {'beverage': None, 'ingredient_price': 17.86, 'beverage_price': None, 'ingredient': {'name': 'ingredient3', 'price': 15.6, '_id': 2}},
                {'beverage': None, 'ingredient_price': 17.38, 'beverage_price': None, 'ingredient': {'name': 'ingredient4', 'price': 15.6, '_id': 2}},
                {'beverage': {'name': 'beverage1', 'price': 15.6, '_id': 2}, 'ingredient_price': None, 'beverage_price': 12.25, 'ingredient': None},
                {'beverage': {'name': 'beverage1', 'price': 15.6, '_id': 2}, 'ingredient_price': None, 'beverage_price': 19.38, 'ingredient': None},
                {'beverage': {'name': 'beverage2', 'price': 15.6, '_id': 2}, 'ingredient_price': None, 'beverage_price': 16.04, 'ingredient': None}
            ],
            'size': {'name': 'bltivmhfyx', 'price': 15.6, '_id': 2},
            'total_price': 156.32,
            'most_beverage': 'beverage1',
            'ingredients': ['ingredient1', 'ingredient2', 'ingredient3']},
        {'_id': 2,
            'client_address': 'asdfds',
            'client_dni': '2877374003',
            'client_name': 'client2',
            'client_phone': '5447470741',
            'date': '2023-05-20T17:59:41.824299',
            'detail': [
                {'beverage': None, 'ingredient_price': 16.29, 'beverage_price': None, 'ingredient': {'name': 'bltivmhfyx', 'price': 15.6, '_id': 2}},
                {'beverage': None, 'ingredient_price': 15.68, 'beverage_price': None, 'ingredient': {'name': 'ingredient2', 'price': 15.6, '_id': 2}},
                {'beverage': None, 'ingredient_price': 17.86, 'beverage_price': None, 'ingredient': {'name': 'ingredient3', 'price': 15.6, '_id': 2}},
                {'beverage': None, 'ingredient_price': 17.38, 'beverage_price': None, 'ingredient': {'name': 'ingredient4', 'price': 15.6, '_id': 2}},
                {'beverage': {'name': 'beverage1', 'price': 15.6, '_id': 2}, 'ingredient_price': None, 'beverage_price': 12.25, 'ingredient': None},
                {'beverage': {'name': 'beverage1', 'price': 15.6, '_id': 2}, 'ingredient_price': None, 'beverage_price': 19.38, 'ingredient': None},
                {'beverage': {'name': 'beverage2', 'price': 15.6, '_id': 2}, 'ingredient_price': None, 'beverage_price': 16.04, 'ingredient': None}
            ],
            'size': {'name': 'bltivmhfyx', 'price': 15.6, '_id': 2},
            'total_price': 156.32,
            'most_beverage': 'beverage2',
            'ingredients': ['ingredient1']},
        {'_id': 3,
            'client_address': 'asdfds',
            'client_dni': '2877374003',
            'client_name': 'client3',
            'client_phone': '5447470741',
            'date': '2023-05-20T17:59:41.824299',
            'detail': [
                {'beverage': None, 'ingredient_price': 16.29, 'beverage_price': None, 'ingredient': {'name': 'bltivmhfyx', 'price': 15.6, '_id': 2}},
                {'beverage': None, 'ingredient_price': 15.68, 'beverage_price': None, 'ingredient': {'name': 'ingredient2', 'price': 15.6, '_id': 2}},
                {'beverage': None, 'ingredient_price': 17.86, 'beverage_price': None, 'ingredient': {'name': 'ingredient3', 'price': 15.6, '_id': 2}},
                {'beverage': None, 'ingredient_price': 17.38, 'beverage_price': None, 'ingredient': {'name': 'ingredient4', 'price': 15.6, '_id': 2}},
                {'beverage': {'name': 'beverage1', 'price': 15.6, '_id': 2}, 'ingredient_price': None, 'beverage_price': 12.25, 'ingredient': None},
                {'beverage': {'name': 'beverage1', 'price': 15.6, '_id': 2}, 'ingredient_price': None, 'beverage_price': 19.38, 'ingredient': None},
                {'beverage': {'name': 'beverage2', 'price': 15.6, '_id': 2}, 'ingredient_price': None, 'beverage_price': 16.04, 'ingredient': None}
            ],
            'size': {'name': 'bltivmhfyx', 'price': 15.6, '_id': 2},
            'total_price': 200.32,
            'most_beverage': 'beverage2',
            'ingredients': ['ingredient4']},
        {'_id': 4,
            'client_address': 'asdfds',
            'client_dni': '2877374003',
            'client_name': 'client4',
            'client_phone': '5447470741',
            'date': '2023-02-20T17:59:41.824299',
            'detail': [
                {'beverage': None, 'ingredient_price': 16.29, 'beverage_price': None, 'ingredient': {'name': 'bltivmhfyx', 'price': 15.6, '_id': 2}},
                {'beverage': None, 'ingredient_price': 15.68, 'beverage_price': None, 'ingredient': {'name': 'ingredient2', 'price': 15.6, '_id': 2}},
                {'beverage': None, 'ingredient_price': 17.86, 'beverage_price': None, 'ingredient': {'name': 'ingredient3', 'price': 15.6, '_id': 2}},
                {'beverage': None, 'ingredient_price': 17.38, 'beverage_price': None, 'ingredient': {'name': 'ingredient4', 'price': 15.6, '_id': 2}},
                {'beverage': {'name': 'beverage1', 'price': 15.6, '_id': 2}, 'ingredient_price': None, 'beverage_price': 12.25, 'ingredient': None},
                {'beverage': {'name': 'beverage1', 'price': 15.6, '_id': 2}, 'ingredient_price': None, 'beverage_price': 19.38, 'ingredient': None},
                {'beverage': {'name': 'beverage2', 'price': 15.6, '_id': 2}, 'ingredient_price': None, 'beverage_price': 16.04, 'ingredient': None}
            ],
            'size': {'name': 'bltivmhfyx', 'price': 15.6, '_id': 2},
            'total_price': 200.32,
            'most_beverage': 'beverage2',
            'ingredients': ['ingredient4']},  # flake8 noqa
        {'_id': 5,  # flake8 noqa
            'client_address': 'asdfds',
            'client_dni': '2877374003',
            'client_name': 'client3',
            'client_phone': '5447470741',
            'date': '2023-02-20T17:59:41.824299',
            'detail': [
                {'beverage': None, 'ingredient_price': 16.29, 'beverage_price': None, 'ingredient': {'name': 'bltivmhfyx', 'price': 15.6, '_id': 2}},
                {'beverage': None, 'ingredient_price': 15.68, 'beverage_price': None, 'ingredient': {'name': 'ingredient2', 'price': 15.6, '_id': 2}},
                {'beverage': None, 'ingredient_price': 17.86, 'beverage_price': None, 'ingredient': {'name': 'ingredient3', 'price': 15.6, '_id': 2}},
                {'beverage': None, 'ingredient_price': 17.38, 'beverage_price': None, 'ingredient': {'name': 'ingredient4', 'price': 15.6, '_id': 2}},
                {'beverage': {'name': 'beverage1', 'price': 15.6, '_id': 2}, 'ingredient_price': None, 'beverage_price': 12.25, 'ingredient': None},
                {'beverage': {'name': 'beverage1', 'price': 15.6, '_id': 2}, 'ingredient_price': None, 'beverage_price': 19.38, 'ingredient': None},
                {'beverage': {'name': 'beverage2', 'price': 15.6, '_id': 2}, 'ingredient_price': None, 'beverage_price': 16.04, 'ingredient': None}
            ],
            'size': {'name': 'bltivmhfyx', 'price': 15.6, '_id': 2},
            'total_price': 200.32,
            'most_beverage': 'beverage2',
            'ingredients': ['ingredient4']},
        {'_id': 6,
            'client_address': 'asdfds',
            'client_dni': '2877374003',
            'client_name': 'client3',
            'client_phone': '5447470741',
            'date': '2023-03-20T17:59:41.824299',
            'detail': [
                {'beverage': None, 'ingredient_price': 16.29, 'beverage_price': None, 'ingredient': {'name': 'bltivmhfyx', 'price': 15.6, '_id': 2}},
                {'beverage': None, 'ingredient_price': 15.68, 'beverage_price': None, 'ingredient': {'name': 'ingredient2', 'price': 15.6, '_id': 2}},
                {'beverage': None, 'ingredient_price': 17.86, 'beverage_price': None, 'ingredient': {'name': 'ingredient3', 'price': 15.6, '_id': 2}},
                {'beverage': None, 'ingredient_price': 17.38, 'beverage_price': None, 'ingredient': {'name': 'ingredient4', 'price': 15.6, '_id': 2}},
                {'beverage': {'name': 'beverage1', 'price': 15.6, '_id': 2}, 'ingredient_price': None, 'beverage_price': 12.25, 'ingredient': None},
                {'beverage': {'name': 'beverage1', 'price': 15.6, '_id': 2}, 'ingredient_price': None, 'beverage_price': 19.38, 'ingredient': None},
                {'beverage': {'name': 'beverage2', 'price': 15.6, '_id': 2}, 'ingredient_price': None, 'beverage_price': 16.04, 'ingredient': None}
            ],
            'size': {'name': 'bltivmhfyx', 'price': 15.6, '_id': 2},
            'total_price': 200.32,
            'most_beverage': 'beverage2',
            'ingredients': ['ingredient4']},
        {'_id': 7,
            'client_address': 'asdfds',
            'client_dni': '2877374003',
            'client_name': 'client5',
            'client_phone': '5447470741',
            'date': '2023-03-20T17:59:41.824299',
            'detail': [
                {'beverage': None, 'ingredient_price': 16.29, 'beverage_price': None, 'ingredient': {'name': 'bltivmhfyx', 'price': 15.6, '_id': 2}},
                {'beverage': None, 'ingredient_price': 15.68, 'beverage_price': None, 'ingredient': {'name': 'ingredient2', 'price': 15.6, '_id': 2}},
                {'beverage': None, 'ingredient_price': 17.86, 'beverage_price': None, 'ingredient': {'name': 'ingredient3', 'price': 15.6, '_id': 2}},
                {'beverage': None, 'ingredient_price': 17.38, 'beverage_price': None, 'ingredient': {'name': 'ingredient4', 'price': 15.6, '_id': 2}},
                {'beverage': {'name': 'beverage1', 'price': 15.6, '_id': 2}, 'ingredient_price': None, 'beverage_price': 12.25, 'ingredient': None},
                {'beverage': {'name': 'beverage1', 'price': 15.6, '_id': 2}, 'ingredient_price': None, 'beverage_price': 19.38, 'ingredient': None},
                {'beverage': {'name': 'beverage2', 'price': 15.6, '_id': 2}, 'ingredient_price': None, 'beverage_price': 16.04, 'ingredient': None}
            ],
            'size': {'name': 'bltivmhfyx', 'price': 15.6, '_id': 2},
            'total_price': 200.32,
            'most_beverage': 'beverage2',
            'ingredients': ['ingredient4']},
        {'_id': 8,
            'client_address': 'asdfds',
            'client_dni': '2877374003',
            'client_name': 'client1',
            'client_phone': '5447470741',
            'date': '2023-03-20T17:59:41.824299',
            'detail': [
                {'beverage': None, 'ingredient_price': 16.29, 'beverage_price': None, 'ingredient': {'name': 'bltivmhfyx', 'price': 15.6, '_id': 2}},
                {'beverage': None, 'ingredient_price': 15.68, 'beverage_price': None, 'ingredient': {'name': 'ingredient2', 'price': 15.6, '_id': 2}},
                {'beverage': None, 'ingredient_price': 17.86, 'beverage_price': None, 'ingredient': {'name': 'ingredient3', 'price': 15.6, '_id': 2}},
                {'beverage': None, 'ingredient_price': 17.38, 'beverage_price': None, 'ingredient': {'name': 'ingredient4', 'price': 15.6, '_id': 2}},
                {'beverage': {'name': 'beverage1', 'price': 15.6, '_id': 2}, 'ingredient_price': None, 'beverage_price': 12.25, 'ingredient': None},
                {'beverage': {'name': 'beverage1', 'price': 15.6, '_id': 2}, 'ingredient_price': None, 'beverage_price': 19.38, 'ingredient': None},
                {'beverage': {'name': 'beverage2', 'price': 15.6, '_id': 2}, 'ingredient_price': None, 'beverage_price': 16.04, 'ingredient': None}
            ],
            'size': {'name': 'bltivmhfyx', 'price': 15.6, '_id': 2},
            'total_price': 200.32,
            'most_beverage': 'beverage2',
            'ingredients': ['ingredient4']},
        {'_id': 9,
            'client_address': 'asdfds',
            'client_dni': '2877374003',
            'client_name': 'client2',
            'client_phone': '5447470741',
            'date': '2023-03-20T17:59:41.824299',
            'detail': [
                {'beverage': None, 'ingredient_price': 16.29, 'beverage_price': None, 'ingredient': {'name': 'bltivmhfyx', 'price': 15.6, '_id': 2}},
                {'beverage': None, 'ingredient_price': 15.68, 'beverage_price': None, 'ingredient': {'name': 'ingredient2', 'price': 15.6, '_id': 2}},
                {'beverage': None, 'ingredient_price': 17.86, 'beverage_price': None, 'ingredient': {'name': 'ingredient3', 'price': 15.6, '_id': 2}},
                {'beverage': None, 'ingredient_price': 17.38, 'beverage_price': None, 'ingredient': {'name': 'ingredient4', 'price': 15.6, '_id': 2}},
                {'beverage': {'name': 'beverage1', 'price': 15.6, '_id': 2}, 'ingredient_price': None, 'beverage_price': 12.25, 'ingredient': None},
                {'beverage': {'name': 'beverage1', 'price': 15.6, '_id': 2}, 'ingredient_price': None, 'beverage_price': 19.38, 'ingredient': None},
                {'beverage': {'name': 'beverage2', 'price': 15.6, '_id': 2}, 'ingredient_price': None, 'beverage_price': 16.04, 'ingredient': None}
            ],
            'size': {'name': 'bltivmhfyx', 'price': 15.6, '_id': 2},
            'total_price': 200.32,
            'most_beverage': 'beverage2',
            'ingredients': ['ingredient4']},
    ]


def orders_data_mock() -> dict:
    return [
        {'_id': 1,
            'client_address': 'vpqkwenjrz',
            'client_dni': '2877374003',
            'client_name': 'nhweotpqkz',
            'client_phone': '5447470741',
            'date': '2023-05-20T17:59:41.824299',
            'detail': [
                {'beverage': None, 'ingredient_price': 16.29, 'beverage_price': None, 'ingredient': {'name': 'bltivmhfyx', 'price': 15.6, '_id': 2}},
                {'beverage': None, 'ingredient_price': 15.68, 'beverage_price': None, 'ingredient': {'name': 'bltivmhfyx', 'price': 15.6, '_id': 2}},
                {'beverage': None, 'ingredient_price': 17.86, 'beverage_price': None, 'ingredient': {'name': 'bltivmhfyx', 'price': 15.6, '_id': 2}},
                {'beverage': None, 'ingredient_price': 17.38, 'beverage_price': None, 'ingredient': {'name': 'bltivmhfyx', 'price': 15.6, '_id': 2}},
                {'beverage': {'name': 'bltivmhfyx', 'price': 15.6, '_id': 2}, 'ingredient_price': None, 'beverage_price': 12.25, 'ingredient': None},
                {'beverage': {'name': 'bltivmhfyx', 'price': 15.6, '_id': 2}, 'ingredient_price': None, 'beverage_price': 19.38, 'ingredient': None},
                {'beverage': {'name': 'bltivmhfyx', 'price': 15.6, '_id': 2}, 'ingredient_price': None, 'beverage_price': 16.04, 'ingredient': None}
            ],
            'size': {'name': 'bltivmhfyx', 'price': 15.6, '_id': 2},
            'total_price': 156.32},
        {'_id': 2,
            'client_address': 'vpqkwenjrz',
            'client_dni': '2877374003',
            'client_name': 'nhweotpqkz',
            'client_phone': '5447470741',
            'date': '2023-05-20T17:59:42.109109',
            'detail': [
                {'beverage': None, 'ingredient_price': 16.29, 'beverage_price': None, 'ingredient': {'name': 'bltivmhfyx', 'price': 15.6, '_id': 2}},
                {'beverage': None, 'ingredient_price': 15.68, 'beverage_price': None, 'ingredient': {'name': 'bltivmhfyx', 'price': 15.6, '_id': 2}},
                {'beverage': None, 'ingredient_price': 17.86, 'beverage_price': None, 'ingredient': {'name': 'bltivmhfyx', 'price': 15.6, '_id': 2}},
                {'beverage': None, 'ingredient_price': 17.38, 'beverage_price': None, 'ingredient': {'name': 'bltivmhfyx', 'price': 15.6, '_id': 2}},
                {'beverage': {'name': 'bltivmhfyx', 'price': 15.6, '_id': 2}, 'ingredient_price': None, 'beverage_price': 12.25, 'ingredient': None},
                {'beverage': {'name': 'bltivmhfyx', 'price': 15.6, '_id': 2}, 'ingredient_price': None, 'beverage_price': 19.38, 'ingredient': None},
                {'beverage': {'name': 'bltivmhfyx', 'price': 15.6, '_id': 2}, 'ingredient_price': None, 'beverage_price': 16.04, 'ingredient': None}
            ],
            'size': {'name': 'bltivmhfyx', 'price': 15.6, '_id': 2},
            'total_price': 162.62},
        {'_id': 3,
            'client_address': 'vpqkwenjrz',
            'client_dni': '2877374003',
            'client_name': 'nhweotpqkz',
            'client_phone': '5447470741',
            'date': '2023-05-20T17:59:42.109109',
            'detail': [
                {'beverage': None, 'ingredient_price': 16.29, 'beverage_price': None, 'ingredient': {'name': 'bltivmhfyx', 'price': 15.6, '_id': 2}},
                {'beverage': None, 'ingredient_price': 15.68, 'beverage_price': None, 'ingredient': {'name': 'bltivmhfyx', 'price': 15.6, '_id': 2}},
                {'beverage': None, 'ingredient_price': 17.86, 'beverage_price': None, 'ingredient': {'name': 'bltivmhfyx', 'price': 15.6, '_id': 2}},
                {'beverage': None, 'ingredient_price': 17.38, 'beverage_price': None, 'ingredient': {'name': 'bltivmhfyx', 'price': 15.6, '_id': 2}}
            ],
            'size': {'name': 'bltivmhfyx', 'price': 15.6, '_id': 2},
            'total_price': 162.62},
        ]


@pytest.fixture
def report_uri():
    return '/report/'


@pytest.fixture
def list_to_fill():
    return ['item1']


@pytest.fixture
def list_to_count():
    return ['item1', 'item1', 'item1', 'item1', 'item2', 'item2', 'item2']


@pytest.fixture
def data_frame_orders():
    return pd.DataFrame(orders_data_frame_mock())


@pytest.fixture
def report_orders_data():
    return orders_data_mock()


@pytest.fixture
def orders_data_frame_row():
    return orders_data_frame_row_mock()
