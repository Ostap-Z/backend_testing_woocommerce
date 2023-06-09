import allure
import pytest

from src.helpers.orders_helper import OrdersHelper
from src.utilities.requests_utility import RequestsUtility
from src.utilities.generator_utility import generate_random_string


@allure.suite("Orders endpoint")
@allure.feature("Update orders")
@pytest.mark.orders
class TestUpdateOrder:
    orders_helper = OrdersHelper()
    request_utility = RequestsUtility()

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
        with allure.step(
          f"Get an order id: {order['id']}"
        ):
            order_id = order["id"]

        with allure.step(
          "Get an order expected status: "
          f"{order_payload_status['status']}"
        ):
            status = order_payload_status["status"]

        with allure.step(
            f"Update an order {order_id} "
            f"with payload: {order_payload_status}"
        ):
            self.orders_helper.update_order(
                order_id=order_id,
                payload=order_payload_status
            )

        with allure.step(
          "Get an order updated status"
        ):
            updated_status = \
                self.orders_helper \
                .retrieve_order_by_order_id(
                    order_id=order_id
                )["status"]

        with allure.step(
            "Verify that the status of an order "
            f"has been updated with {status} status: "
            f"{updated_status=}, {status=}"
        ):
            assert updated_status == status, \
                "\nActual result:" \
                f"\n\tStatus of the order " \
                f"has not been updated with {status} status" \
                f"\n\tActual status: {updated_status}" \
                "\nExpected result:" \
                f"\n\tStatus should be updated with the {status} status"

    @allure.title(
        "Verify that the API returns a correct message "
        "when the user set invalid status parameter "
        "while updating an order"
    )
    @allure.severity(
        severity_level=allure.severity_level.NORMAL
    )
    @pytest.mark.tcid55
    def test_update_order_status_with_invalid_data(
        self,
        order
    ):
        with allure.step(
          f"Get an order id: {order['id']}"
        ):
            order_id = order["id"]

        with allure.step(
            "Generate a random invalid status"
        ):
            invalid_status = generate_random_string()

        payload = {
            "status": invalid_status
        }
        expected_response_message = "Invalid parameter(s): status"

        with allure.step(
            "Update an order with invalid status: "
            f"{payload['status']}"
        ):
            response = self.request_utility.put(
                endpoint=f"orders/{order_id}",
                payload=payload,
                expected_status_code=400
            )

        with allure.step(
            "Take a message from the API response: "
            f"{response['message']}"
        ):
            response_message = response["message"]

        with allure.step(
            "Verify that a message in the API response "
            f"equals to the {expected_response_message}"
        ):
            assert response_message == expected_response_message, \
                "\nActual result:" \
                "\n\tUpdate order status to random string " \
                "has invalid message in API response" \
                f"\n\tActual response code: {response_message}" \
                f"\n\tActual response: {response}" \
                "\nExpected result:" \
                "\n\tMessage in API response " \
                f"should be {expected_response_message}"

    @allure.title(
        "Verify that the user has an opportunity "
        "to update the order customer note"
    )
    @allure.severity(
        severity_level=allure.severity_level.NORMAL
    )
    @pytest.mark.tcid56
    def test_update_order_customer_note(
        self,
        order
    ):
        with allure.step(
            "Generate a random customer note"
        ):
            random_customer_note = generate_random_string(150)

        with allure.step(
          f"Get an order id: {order['id']}"
        ):
            order_id = order["id"]

        payload = {
            "customer_note": random_customer_note
        }

        with allure.step(
            "Update an order with customer note: "
            f"{payload['customer_note']}"
        ):
            self.orders_helper.update_order(
                order_id=order_id,
                payload=payload
            )

        with allure.step(
          f"Retrieve an order with id {order_id}"
        ):
            updated_order = \
                self\
                .orders_helper\
                .retrieve_order_by_order_id(
                    order_id
                )

        with allure.step(
            f"Get a customer note from the order {order_id}: "
            f"{updated_order['customer_note']}"
        ):
            updated_customer_note = updated_order["customer_note"]

        with allure.step(
            f"Verify that the customer note "
            f"has been updated with {random_customer_note}"
        ):
            assert updated_customer_note == random_customer_note, \
                "\nActual result:" \
                f"\n\tCustomer note for the order {order_id} " \
                f"has not been updated" \
                f"\n\tActual customer note: {updated_customer_note}" \
                "\nExpected result:" \
                f"\n\tCustomer note for the order {order_id} " \
                f"should be updated with {random_customer_note}"
