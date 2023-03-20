import random

import pytest
import allure

from src.dao.products_dao import ProductsDAO
from src.helpers.orders_helper import OrdersHelper
from src.dao.orders_dao import OrdersDAO


@allure.suite("Orders endpoint")
@allure.feature("Create orders")
@pytest.mark.orders
class TestCreateOrder:
    product_dao = ProductsDAO()
    orders_dao = OrdersDAO()
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

    @allure.title(
        "Verify that the created order exists in DB"
    )
    @allure.severity(
        severity_level=allure.severity_level.CRITICAL
    )
    @pytest.mark.tcid50
    def test_verify_created_order_exist_db(self):
        with allure.step("Get random product from DB"):
            product_db = self.product_dao.get_random_product()

        with allure.step(
            f"Get a product id from random product: {product_db['ID']}"
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
            f"Get a 'id' from API response: {order['id']}"
        ):
            order_id = order['id']

        with allure.step(
            "Get a general info about an order "
            f"with 'order_id' {order_id} from DB"
        ):
            line_info = \
                self.orders_dao.get_order_items_by_order_id(order_id)

        with allure.step(
          "Get the 'line_items' from an order "
          f"with 'order_id' {order_id}"
        ):
            line_items = [
                i for i in line_info
                if i["order_item_type"] == "line_item"
            ]

        with allure.step(
            f"Get an order line id: {line_items[0]['order_item_id']}"
        ):
            line_id = line_items[0]['order_item_id']

        with allure.step(
          f"Get an order details for the 'line_id' {line_id}"
        ):
            line_details = self.orders_dao.get_order_items_details(line_id)

        with allure.step(
          f"Get a product id from DB: {line_details['_product_id']}"
        ):
            product_id_db = int(line_details["_product_id"])

        with allure.step(
          "Verify that the 'product_id' in DB "
          "equals to the sent 'product_id' by API: "
          f"{product_id_db=}, {product_id=}"
        ):
            assert product_id_db == product_id, \
                "\nActual result:" \
                "\n\tProduct_id in DB doesn't match a product_id in API: " \
                f"{product_id_db=}, {product_id=}" \
                "\nExpected result:" \
                f"\n\tProduct_id in DB should be equaled to {product_id}"
