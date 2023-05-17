import pytest

from app.controllers.base import BaseController
from app.controllers.ingredient import IngredientController

from ..utils.functions import create_items, get_random_price, get_random_string


def ingredient_mock() -> dict:
    return {
        'name': get_random_string(),
        'price': get_random_price(10, 20)
    }

@pytest.fixture
def ingredient_uri():
    return '/ingredient/'


@pytest.fixture
def ingredient():
    return ingredient_mock()


@pytest.fixture
def ingredients():
    return [ingredient_mock() for _ in range(5)]


@pytest.fixture
def create_ingredient(client, ingredient_uri) -> dict:
    response = client.post(ingredient_uri, json=ingredient_mock())
    return response

@pytest.fixture
def create_ingredients(ingredients: list):
    created_ingredients = create_items(ingredients, IngredientController)
    return created_ingredients
