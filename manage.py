import pytest
from flask.cli import FlaskGroup
from flask_migrate import Migrate


from app import flask_app
from app.plugins import db
# flake8: noqa
from app.repositories.models import Ingredient, Order, OrderDetail, Size, Beverage
from app.seeds.seeders import seed_data


manager = FlaskGroup(flask_app)

migrate = Migrate()
migrate.init_app(flask_app, db, render_as_batch=True)


@manager.command('test', with_appcontext=False)
def test():
    return pytest.main(['-v', './app/test'])

@manager.command('seeder', with_appcontext=True)
def seeder():
    return seed_data()
    


if __name__ == '__main__':
    manager()
