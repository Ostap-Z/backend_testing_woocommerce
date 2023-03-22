import allure
import pytest

from src.helpers.orders_helper import OrdersHelper


@allure.suite("Orders endpoint")
@allure.feature("Update orders")
@pytest.mark.orders
class TestUpdateOrder:
    orders_helper = OrdersHelper()

    @allure.title(
        "Verify that the created order status could be updated"
    )
    @allure.severity(
        severity_level=allure.severity_level.NORMAL
    )
    @pytest.mark.tcid52
    def test_update_order_status(
        self,
        order,
        order_payload_status
    ):
        order_id = order["id"]
        status = order_payload_status["status"]

        self.orders_helper.update_order(
            order_id=order_id,
            payload=order_payload_status
        )
        updated_status = \
            self.orders_helper \
            .retrieve_order_by_order_id(order_id=order_id)["status"]

        assert updated_status == status, \
            "\nActual result:" \
            f"\n\tStatus of the order " \
            f"has not been updated with {status} status" \
            f"\n\tActual status: {updated_status}" \
            "\nExpected result:" \
            f"\n\tStatus should be updated with the {status} status"
