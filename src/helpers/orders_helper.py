import json
import os

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
        with open(payload_template) as file:
            payload = json.load(file)

        if additional_args:
            self.check_object_type(additional_args, dict)
            payload.update(additional_args)

        return self.request_utility.post(
            "orders",
            payload=payload,
            expected_status_code=201
        )

    @staticmethod
    def check_object_type(
            obj,
            expected_type
    ):
        if not isinstance(obj, expected_type):
            raise TypeError(
                "Invalid type for object. "
                f"Expected type is {expected_type}"
            )
