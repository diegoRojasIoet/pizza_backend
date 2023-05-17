from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, jsonify, request

from app.services.base import handler_create, handler_get_all, handler_get_by_id, handler_update

from ..controllers import SizeController

size = Blueprint('size', __name__)


@size.route('/', methods=GET)
def get_sizes():
    return handler_get_all(SizeController)


@size.route('/', methods=POST)
def create_size():
    return handler_create(SizeController, request.json)



@size.route('/', methods=PUT)
def update_size():
    return handler_update(SizeController, request.json)


@size.route('/id/<_id>', methods=GET)
def get_size_by_id(_id: int):
    return handler_get_by_id(SizeController, _id)

