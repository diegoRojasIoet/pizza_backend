import pytest
from app.controllers import OrderController
from app.test.utils.functions import get_random_choice, shuffle_list


def __order(ingredients: list, size: dict, client_data: dict):
    ingredients = [ingredient.get('_id') for ingredient in ingredients]
    size_id = size.get('_id')
    return {
        **client_data,
        'ingredients': ingredients,
        'size_id': size_id
    }


def test_create(app, order):
    created_order, error = OrderController.create(order)
    size_id = order.pop('size_id', None)
    ingredient_ids = order.pop('ingredients', [])
    pytest.assume(error is None)
    for param, value in order.items():
        pytest.assume(param in created_order)
        pytest.assume(value == created_order[param])
        pytest.assume(created_order['_id'])
        pytest.assume(size_id == created_order['size']['_id'])

        ingredients_in_detail = set(item['ingredient']['_id'] for item in created_order['detail'])
        pytest.assume(not ingredients_in_detail.difference(ingredient_ids))


def test_calculate_order_price(app, create_size, create_ingredients, client_data):
    created_size = create_size.json
    created_ingredients = create_ingredients
    order = __order(created_ingredients, created_size, client_data)
    created_order, _ = OrderController.create(order)
    pytest.assume(created_order['total_price'] == round(created_size['price'] + sum(ingredient['price'] for ingredient in created_ingredients), 2))


def test_get_by_id(app, order):
    created_order, _ = OrderController.create(order)
    order_from_db, error = OrderController.get_by_id(created_order['_id'])
    size_id = order.pop('size_id', None)
    ingredient_ids = order.pop('ingredients', [])
    pytest.assume(error is None)
    for param, value in created_order.items():
        pytest.assume(order_from_db[param] == value)
        pytest.assume(size_id == created_order['size']['_id'])

        ingredients_in_detail = set(item['ingredient']['_id'] for item in created_order['detail'])
        pytest.assume(not ingredients_in_detail.difference(ingredient_ids))


def test_get_all(app, create_sizes, create_ingredients, client_data):
    created_sizes = create_sizes
    created_ingredients = create_ingredients
    created_orders = []
    for _ in range(5):
        order = __order(shuffle_list(created_ingredients)[:3], get_random_choice(created_sizes), client_data)
        created_order, _ = OrderController.create(order)
        created_orders.append(created_order)

    orders_from_db, error = OrderController.get_all()
    searchable_orders = {db_order['_id']: db_order for db_order in orders_from_db}
    pytest.assume(error is None)
    for created_order in created_orders:
        current_id = created_order['_id']
        assert current_id in searchable_orders
        for param, value in created_order.items():
            pytest.assume(searchable_orders[current_id][param] == value)
