import pytest
from app.controllers import OrderController
from app.test.utils.functions import get_random_choice, shuffle_list


def __order(ingredients: list, beverages: list, size: dict, client_data: dict):
    ingredients = [ingredient.get('_id') for ingredient in ingredients]
    beverages = [beverage.get('_id') for beverage in beverages]
    size_id = size.get('_id')
    return {
        **client_data,
        'ingredients': ingredients,
        'beverages': beverages,
        'size_id': size_id
    }


def test_create(app, order):
    created_order, error = OrderController.create(order)
    size_id = order.pop('size_id', None)
    ingredient_ids = order.pop('ingredients', [])
    beverages_ids = order.pop('beverages', [])
    pytest.assume(error is None)
    for param, value in order.items():
        assert(param in created_order)
        assert(value == created_order[param])

    ingredients_in_detail = set(item['ingredient']['_id'] for item in created_order['detail'] if item['ingredient'] is not None)
    beverages_in_order = set(item['beverage']['_id'] for item in created_order['detail'] if item['beverage'] is not None)
    assert(not ingredients_in_detail.difference(ingredient_ids))
    assert(not beverages_in_order.difference(beverages_ids))
    assert(created_order['_id'])
    assert(size_id == created_order['size']['_id'])


def test_calculate_order_price(app, create_size, create_ingredients, create_beverages, client_data):
    created_size = create_size.json
    order = __order(create_ingredients, create_beverages, created_size, client_data)
    created_order, _ = OrderController.create(order)
    assert(created_order['total_price'] == round(
            created_size['price'] + sum(ingredient['price'] for ingredient in create_ingredients) +
            sum(beverage['price'] for beverage in create_beverages), 2))


def test_get_by_id(app, order):
    created_order, _ = OrderController.create(order)
    order_from_db, error = OrderController.get_by_id(created_order['_id'])
    size_id = order.pop('size_id', None)
    ingredient_ids = order.pop('ingredients', [])
    beverages_ids = order.pop('beverages', [])
    pytest.assume(error is None)
    for param, value in created_order.items():
        assert(order_from_db[param] == value)

    ingredients_in_detail = set(item['ingredient']['_id'] for item in created_order['detail'] if item['ingredient'] is not None)
    beverages_in_detail = set(item['beverage']['_id'] for item in created_order['detail'] if item['beverage'] is not None)
    assert(not ingredients_in_detail.difference(ingredient_ids))
    assert(not beverages_in_detail.difference(beverages_ids))
    assert(size_id == created_order['size']['_id'])


def test_get_all(app, create_sizes, create_ingredients, create_beverages, client_data):
    created_orders = []
    for _ in range(5):
        order = __order(shuffle_list(create_ingredients)[:3], create_beverages, get_random_choice(create_sizes), client_data)
        created_order, _ = OrderController.create(order)
        created_orders.append(created_order)

    orders_from_db, error = OrderController.get_all()
    searchable_orders = {db_order['_id']: db_order for db_order in orders_from_db}
    pytest.assume(error is None)
    for created_order in created_orders:
        current_id = created_order['_id']
        assert current_id in searchable_orders
        for param, value in created_order.items():
            assert(searchable_orders[current_id][param] == value)
