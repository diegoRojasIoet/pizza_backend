import pytest
from app.controllers.beverage import BeverageController

from app.test.utils.functions import get_random_string, get_random_price


def test_create_beverage_service(app, beverage: dict):
    created_beverage, error = BeverageController.create(beverage)
    pytest.assume(error is None)
    for param, value in beverage.items():
        assert(param in created_beverage)
        assert(value == created_beverage[param])
    assert(created_beverage['_id'])