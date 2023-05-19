import pytest
from app.common.constants import NUMBERITEMS

from app.controllers.beverage import BeverageController

from ..utils.functions import create_items, get_random_price, get_random_string


def beverage_mock() -> dict:
    return {
        'name': get_random_string(),
        'price': get_random_price(10, 20),
    }


@pytest.fixture
def beverage_uri():
    return '/beverage/'


@pytest.fixture
def beverage():
    return beverage_mock()


@pytest.fixture
def beverages():
    return [beverage_mock() for _ in range(NUMBERITEMS)]


@pytest.fixture
def create_beverage(client, beverage, beverage_uri) -> dict:
    response = client.post(beverage_uri, json=beverage)
    return response


@pytest.fixture
def create_beverages(beverages) -> list:
    created_beverages = create_items(beverages, BeverageController)
    return created_beverages
