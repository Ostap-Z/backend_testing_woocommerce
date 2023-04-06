import allure

from src.utilities.requests_utility import RequestsUtility


class CouponsHelper:

    def __init__(self):
        self.request_utility = RequestsUtility()

    def create_coupon(
        self,
        code,
        **kwargs
    ):
        payload = {
            "code": code
        } | kwargs
        with allure.step(
            f"Create a coupon with data: {payload=}"
        ):
            return self.request_utility.post(
                "coupons",
                payload=payload,
                expected_status_code=201
            )

    def get_coupon_by_id(
        self,
        coupon_id
    ):
        with allure.step(
            f"Get a specific coupon with id: {coupon_id}"
        ):
            return self.request_utility.get(
                f"coupons/{coupon_id}",
            )
