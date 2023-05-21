from app.common.http_methods import GET
from flask import Blueprint

from app.services.base import handler_get_all

from ..controllers import ReportController

report = Blueprint('report', __name__)
@report.route('/', methods=GET)
def get_report():
    return handler_get_all(ReportController)