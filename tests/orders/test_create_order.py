import random

import pytest
import allure

from src.dao.products_dao import ProductsDAO
from src.helpers.orders_helper import OrdersHelper


@allure.suite("Orders endpoint")
@allure.feature("Create orders")
@pytest.mark.orders
class TestCreateOrder:
    product_dao = ProductsDAO()
    orders_helper = OrdersHelper()

    @allure.title(
        "Verify that the guest user has an opportunity to create an order"
    )
    @allure.severity(
        severity_level=allure.severity_level.CRITICAL
    )
    @pytest.mark.tcid48
    def test_create_order_guest_user(self):
        with allure.step("Get random product from DB"):
            product_db = self.product_dao.get_random_product()

        with allure.step(
            f"Get a product id: {product_db['ID']}"
        ):
            product_id = product_db["ID"]

        product_info = {
            "line_items": [
                {
                    "product_id": product_id,
                    "quantity": random.randint(1, 10)
                }
            ]
        }

        with allure.step(
          f"Create an order with additional args: {product_info}"
        ):
            order = self.orders_helper.create_order(
                additional_args=product_info
            )

        with allure.step(
            "Get a 'customer_id' from API response: "
            f"{order['customer_id']}"
        ):
            customer_id_response = order['customer_id']

        with allure.step(
            "Verify that the 'customer_id' in API response equals to 0"
        ):
            assert customer_id_response == 0, \
                "\nActual result:" \
                "\n\tOrder was not be created by the guest user. " \
                f"\n\tActual customer id is {customer_id_response}" \
                "\nExpected result:" \
                "\n\tCustomer id should be equaled to 0. " \
                "So, an order was created by the guest user"

    @allure.title(
        "Verify the quantity of the bought products"
    )
    @allure.severity(
        severity_level=allure.severity_level.CRITICAL
    )
    @pytest.mark.tcid49
    def test_create_order_products_quantity(self):
        with allure.step("Get random product from DB"):
            product_db = self.product_dao.get_random_product()

        with allure.step(
            f"Get a product id: {product_db['ID']}"
        ):
            product_id = product_db["ID"]

        product_info = {
            "line_items": [
                {
                    "product_id": product_id,
                    "quantity": random.randint(1, 10)
                }
            ]
        }

        with allure.step(
            "Get a 'line_items' length based on the prepared data: "
            f"{len(product_info['line_items'])}"
        ):
            product_amount = len(product_info['line_items'])

        with allure.step(
          f"Create an order with additional args: {product_info}"
        ):
            order = self.orders_helper.create_order(
                additional_args=product_info
            )

        with allure.step(
            "Get a 'line_items' length based on the API response: "
            f"{len(product_info['line_items'])}"
        ):
            product_amount_response = len(order['line_items'])

        with allure.step(
          "Verify that products amount in API response the same as sent"
        ):
            assert product_amount_response == product_amount, \
                "\nActual result:" \
                "\n\tAmount of bought items is not equals to expected. " \
                f"Actual amount of products is {product_amount_response} " \
                "\nExpected result:" \
                "\n\tExpected amount of bought items " \
                f"should be {product_amount}"
