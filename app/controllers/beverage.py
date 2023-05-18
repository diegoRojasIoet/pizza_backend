from sqlalchemy.exc import SQLAlchemyError

from ..repositories.managers import BeverageManager
from .base import BaseController



class BeverageController(BaseController):
    manager = BeverageManager
