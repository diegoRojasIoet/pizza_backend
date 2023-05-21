import pytest

from app.controllers.report import ReportController
import pandas as pd

controller = ReportController()

def test_get_report(app, create_orders):
    created_report = ReportController.get_report()
    expected_keys = [
        "most_requested_ingredient",
        "month_with_more_revenue",
        "top_3_clients",
    ]
    assert(type(created_report) == dict)
    assert(key in expected_keys for key in created_report)



def test_fill_list_data(app, list_to_fill):
    controller._fill_list_data({'name':'item2'}, list_to_fill)
    assert(len(list_to_fill) == 2)


def test_count_items(app, list_to_count):
    name = controller._count_items(list_to_count)
    assert(type(name) == str)
    assert(name == 'item1')


def test_get_detail_data(app, orders_data_frame_row):
    ingredients, most_beverage = controller._get_detail_data(orders_data_frame_row)
    assert(type(ingredients) == list)
    assert(most_beverage == 'beverage1')


def test_generate_data_frame_orders(app, report_orders_data):
    df = controller._generate_data_frame_orders(report_orders_data)
    assert(type(df) == pd.DataFrame)
    assert("ingredients" in df.columns)
    assert("most_beverage" in df.columns)
    assert(len(df.columns) == 11)


def test_get_more_asked_ingredient(app, data_frame_orders):
    ingredient = controller._get_most_ingredient(data_frame_orders)
    assert(type(ingredient) == str)
    assert(ingredient == 'ingredient4')


def test_get_more_revenue_month(app, data_frame_orders):
    month = controller._get_most_revenue_month(data_frame_orders)
    assert(type(month) == int)
    assert(month == 3 )


def test_get_top_3_clients(app, data_frame_orders):
    top_3_clients = controller._get_top_3_clients(data_frame_orders)
    assert(type(top_3_clients) == list)
    assert(len(top_3_clients) == 3)
    assert(type(name)== str for name in top_3_clients)
