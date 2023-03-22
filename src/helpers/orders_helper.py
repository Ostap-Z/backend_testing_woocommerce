import json
import os

import allure

from src.utilities.requests_utility import RequestsUtility


class OrdersHelper:
    request_utility = RequestsUtility()

    def __init__(self):
        self._current_file_dir = os.path.dirname(os.path.realpath(__file__))

    def create_order(
            self,
            additional_args=None
    ):
        payload_template = os.path.join(
            self._current_file_dir,
            "..",
            "data",
            "create_order_payload.json"
        )

        with allure.step(
            f"Open a file {payload_template} and deserialize it"
        ):
            with open(payload_template) as file:
                payload = json.load(file)

        with allure.step(
          "Check if additional_args included into payload"
        ):
            if additional_args:
                self.check_object_type(additional_args, dict)

                with allure.step(
                    "Add additional_args to the payload: "
                    f"{additional_args=}"
                ):
                    payload.update(additional_args)

        with allure.step(
            f"Create an order with payload: {payload}"
        ):
            return self.request_utility.post(
                "orders",
                payload=payload,
                expected_status_code=201
            )

    def update_order(
        self,
        order_id,
        payload
    ):
        with allure.step(
            f"Update an order {order_id} with payload: {payload}"
        ):
            return self.request_utility.put(
                endpoint=f"orders/{order_id}",
                payload=payload
            )

    def retrieve_order_by_order_id(
        self,
        order_id
    ):
        with allure.step(
          f"Get a specific order with order_id: {order_id}"
        ):
            return self.request_utility.get(
                endpoint=f"orders/{order_id}"
            )

    @staticmethod
    def check_object_type(
            obj,
            expected_type
    ):
        with allure.step(
          f"Check if object type equals to {expected_type}"
        ):
            if not isinstance(obj, expected_type):
                raise TypeError(
                    "Invalid type for object. "
                    f"Expected type is {expected_type}"
                )
