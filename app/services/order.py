from app.common.http_methods import GET, POST
from flask import Blueprint, jsonify, request

from app.services.base import handler_create, handler_get_all, handler_get_by_id

from ..controllers import OrderController

order = Blueprint('order', __name__)


@order.route('/', methods=POST)
def create_order():
    return handler_create(OrderController, request.json)


@order.route('/id/<_id>', methods=GET)
def get_order_by_id(_id: int):
    return handler_get_by_id(OrderController, _id)


@order.route('/', methods=GET)
def get_orders():
    return handler_get_all(OrderController)

