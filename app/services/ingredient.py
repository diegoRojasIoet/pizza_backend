from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, jsonify, request

from app.services.base import handler_create, handler_get_all, handler_get_by_id, handler_update

from ..controllers import IngredientController

ingredient = Blueprint('ingredient', __name__)


@ingredient.route('/', methods=POST)
def create_ingredient():
    return handler_create(IngredientController, request.json)


@ingredient.route('/', methods=PUT)
def update_ingredient():
    return handler_update(IngredientController, request.json)



@ingredient.route('/id/<_id>', methods=GET)
def get_ingredient_by_id(_id: int):
    return handler_get_by_id(IngredientController, _id)



@ingredient.route('/', methods=GET)
def get_ingredients():
    return handler_get_all(IngredientController)
