import allure

from src.utilities.requests_utility import RequestsUtility


class CouponsHelper:

    def __init__(self):
        self.request_utility = RequestsUtility()

    def create_coupon(
        self,
        payload
    ):
        with allure.step(
            "Create coupon with data: "
            f"endpoint='coupons', {payload=}"
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
