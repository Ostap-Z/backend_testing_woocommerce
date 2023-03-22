import allure
import pytest

from src.helpers.orders_helper import OrdersHelper
from src.utilities.requests_utility import RequestsUtility


@allure.suite("Orders endpoint")
@allure.feature("Get orders")
@pytest.mark.orders
class TestGetOrders:
    orders_helper = OrdersHelper()
    request_utility = RequestsUtility()

    @allure.title(
        "Verify that the user can get a list of orders"
    )
    @allure.severity(
        severity_level=allure.severity_level.NORMAL
    )
    @pytest.mark.tcid53
    def test_get_all_orders(self):
        with allure.step(
                "Get the order list"
        ):
            orders = self.request_utility.get("orders")

        with allure.step(
            "Verify that API response is not empty"
        ):
            assert orders, \
                "\nActual result:" \
                "\n\tAn API doesn't return all orders" \
                f"\n\tActual orders: {orders}" \
                "\nExpected result:" \
                "\n\tA list of all orders should be returned"

    @allure.title(
        "Verify that the user can get "
        "a created order by specific id"
    )
    @allure.severity(
        severity_level=allure.severity_level.NORMAL
    )
    @pytest.mark.tcid54
    def test_get_order_by_order_id(
        self,
        order
    ):
        with allure.step(
            f"Get an order id: {order['id']}"
        ):
            order_id = order["id"]

        with allure.step(
            f"Get an order with id: {order_id}"
        ):
            retrieved_order = \
                self.orders_helper\
                    .retrieve_order_by_order_id(
                        order_id=order_id
                    )

        with allure.step(
            f"Get a retrieved order id: {retrieved_order['id']}"
        ):
            retrieved_order_id = retrieved_order["id"]

        with allure.step(
            "Verify that the retrieved order id "
            "equals to the created order id: "
            f"{retrieved_order_id=}, {order_id=}"
        ):
            assert retrieved_order_id == order_id, \
                "\nActual result:" \
                "\n\tAn API returned a wrong order " \
                f"with id {retrieved_order_id}" \
                "\nExpected result:" \
                f"\n\tAn API should return an order with id {order_id}"
