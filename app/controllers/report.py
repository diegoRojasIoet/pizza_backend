from collections import Counter
from typing import List, Tuple
import pandas as pd
from app.repositories.models import Order
from ..repositories.managers import OrderManager


class ReportController():

    @classmethod
    def _fill_list_data(cls, value: dict, list_to_fill: list):
        if value is not None:
            list_to_fill.append(value['name'])

    @classmethod
    def _count_items(cls, list_to_count: List[str]) -> str:
        counter = Counter(list_to_count)
        most_common_item = counter.most_common(1)

        return most_common_item[0][0]

    @classmethod
    def _get_detail_data(cls, row) -> Tuple[int, int]:
        detail = row['detail']
        ingredients = []
        beverages = []
        for detail_data in detail:
            cls._fill_list_data(detail_data['beverage'], beverages)
            cls._fill_list_data(detail_data['ingredient'], ingredients)

        most_beverage = cls._count_items(beverages) if len(beverages)>0 else ''

        return ingredients, most_beverage

    @classmethod
    def _generate_data_frame_orders(cls, orders: List[Order]) -> pd.DataFrame:
        df = pd.DataFrame(orders)
        df[["ingredients", "most_beverage"]] = df.apply(lambda row: cls._get_detail_data(row), axis=1, result_type="expand")
        return df

    @classmethod
    def _get_most_ingredient(cls, df: pd.DataFrame) -> str:
        ingredients = sum(list(df["ingredients"]), [])
        return cls._count_items(ingredients)

    @classmethod
    def _get_most_revenue_month(cls, df: pd.DataFrame) -> int:
        df['date'] = pd.to_datetime(df['date'])
        revenue_df = df.groupby(pd.Grouper(key='date', freq='M'))['total_price'].sum()
        revenue_df = revenue_df.reset_index()
        revenue_df = revenue_df.sort_values(by="total_price", ascending=False)
        revenue_df = revenue_df.reset_index(drop=True)
        return revenue_df['date'][0].month

    @classmethod
    def _get_top_3_clients(cls, df: pd.DataFrame) -> List[str]:
        df_clients_gb = df.groupby("client_name")['total_price'].sum()
        df_clients_gb = df_clients_gb.reset_index()
        df_clients_gb = df_clients_gb.sort_values(by="total_price", ascending=False)
        df_clients_gb = df_clients_gb.reset_index(drop=True)
        return [df_clients_gb['client_name'][0], df_clients_gb['client_name'][1], df_clients_gb['client_name'][2]]

    @classmethod
    def get_all(cls) -> dict:
        orders = OrderManager.get_all()
        df_order = cls._generate_data_frame_orders(orders)
        return {
            "most_requested_ingredient": cls._get_most_ingredient(df_order),
            "month_with_more_revenue": cls._get_most_revenue_month(df_order),
            "top_3_clients": cls._get_top_3_clients(df_order)
        }, None
