from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, request

from app.services.base import handler_create, handler_get_all, handler_get_by_id, handler_update

from ..controllers import BeverageController

beverage = Blueprint('beverage', __name__)


@beverage.route('/', methods=POST)
def create_beverage():
    return handler_create(BeverageController, request.json)


@beverage.route('/id/<_id>', methods=GET)
def get_beverage_by_id(_id: int):
    return handler_get_by_id(BeverageController, _id)


@beverage.route('/', methods=GET)
def get_beversages():
    return handler_get_all(BeverageController)
