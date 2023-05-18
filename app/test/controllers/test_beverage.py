import pytest
from app.controllers.beverage import BeverageController

from app.test.utils.functions import get_random_string, get_random_price


def test_create_beverage(app, beverage: dict):
    created_beverage, error = BeverageController.create(beverage)
    pytest.assume(error is None)
    for param, value in beverage.items():
        assert(param in created_beverage)
        assert(value == created_beverage[param])
    assert(created_beverage['_id'])


def test_get_by_id(app, beverage: dict):
    created_beverage, _ = BeverageController.create(beverage)
    beverage_from_db, error = BeverageController.get_by_id(created_beverage['_id'])
    pytest.assume(error is None)
    for param, value in created_beverage.items():
        assert(beverage_from_db[param] == value)


def test_get_all(app, beverages: list):
    created_beverages = []
    for beverage in beverages:
        created_beverage, _ = BeverageController.create(beverage)
        created_beverages.append(created_beverage)

    beverages_from_db, error = BeverageController.get_all()
    searchable_beverages = {db_beverage['_id']: db_beverage for db_beverage in beverages_from_db}
    pytest.assume(error is None)
    for created_beverage in created_beverages:
        current_id = created_beverage['_id']
        assert current_id in searchable_beverages
        for param, value in created_beverage.items():
            pytest.assume(searchable_beverages[current_id][param] == value)
