from app.controllers.order import OrderController
from app.repositories.models import Beverage, Ingredient, Size
from app.test.utils.functions import get_random_sequence, get_random_string
from faker import Faker
from app.plugins import db
import random

fake = Faker()


def __create_ingredients():
    ingredients = ['ham', 'sausage', 'mushrooms', 'peperonni', 'cheese']
    for i in range(5):
        name = ingredients[i]
        price = random.randint(1, 5)
        ingredient = Ingredient(_id=i, name=name, price=price)
        db.session.add(ingredient)
    db.session.commit()


def __create_beverages():
    beverages = ['coke', 'sprite', 'pepsi', 'fanta', 'fiora']
    for i in range(5):
        name = beverages[i]
        price = random.randint(1, 5)
        beverage = Beverage(_id=i, name=name, price=price)
        db.session.add(beverage)
    db.session.commit()


def __create_size():
    for i in range(3):
        sizes = ['smoll', 'medium', 'large']
        name = sizes[i]
        price = random.randint(10, 25)
        size = Size(_id=i, name=name, price=price)
        db.session.add(size)
    db.session.commit()


def __create_customers():
    customer_info = []
    for _ in range(20):
        customer_info.append(
            {
                'client_address': get_random_string(),
                'client_dni': get_random_sequence(),
                'client_name': get_random_string(),
                'client_phone': get_random_sequence()
            })
    return customer_info


def __create_orders():
    customer_info = __create_customers()
    for _ in range(100):
        # as we mock 5 ingredients and 5 beverages and 3 sizes
        random_customer = customer_info[random.randint(0, 19)]
        random_quantity_beverages = random.randint(1, 5)
        random_quantity_ingredients = random.randint(1, 5)
        random_size = random.randint(1, 3)
        ingredients = [random.randint(1, 5) for _ in range(random_quantity_ingredients)]
        beverages = [random.randint(1, 5) for _ in range(random_quantity_beverages)]
        order = {
            **random_customer,
            "ingredients": ingredients,
            "beverages": beverages,
            "size_id": random_size,
        }
        order, error = OrderController.create(order)


def seed_data():
    # Drop existing tables (optional)
    db.drop_all()
    db.create_all()

    # Generate fake data and populate the database
    __create_ingredients()
    __create_beverages()
    __create_size()
    __create_orders()

    return 'Database seeded successfully!'
