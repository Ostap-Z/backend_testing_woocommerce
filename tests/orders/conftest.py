import random

import pytest
import allure

from src.helpers.orders_helper import OrdersHelper


@pytest.fixture
def additional_args(random_product_from_db):
    with allure.step(
      f"Get a product id: {random_product_from_db['ID']}"
    ):
        product_id = random_product_from_db["ID"]

    additional_args = {
        "line_items": [
            {
                "product_id": product_id,
                "quantity": random.randint(1, 10)
            }
        ]
    }

    with allure.step(
      f"Get a line_items for additional args: {additional_args}"
    ):
        return additional_args


@pytest.fixture
def order():
    orders_helper = OrdersHelper()
    return orders_helper.create_order()
