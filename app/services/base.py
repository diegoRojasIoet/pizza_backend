from typing import Any, Callable

from flask import jsonify

from app.controllers.base import BaseController


def __handle_request(controller_func: Callable, *args: Any, **kwargs: Any) -> tuple:
    response, error = controller_func(*args, **kwargs)
    response_data = response if not error else {'error': error}
    status_code = 200 if response else 404 if not error else 400
    return jsonify(response_data), status_code


def handler_create(controller: BaseController, request: dict) -> tuple:
    return __handle_request(controller.create, request)


def handler_update(controller: BaseController, request: dict) -> tuple:
    return __handle_request(controller.update, request)


def handler_get_by_id(controller: BaseController, id: int) -> tuple:
    return __handle_request(controller.get_by_id, id)


def handler_get_all(controller: BaseController) -> tuple:
    return __handle_request(controller.get_all)
