import allure
import pytest

from src.helpers.coupons_helper import CouponsHelper
from src.utilities.generator_utility import generate_random_string


@pytest.fixture
def coupon():
    payload = {
        "force": True
    }
    coupons_helper = CouponsHelper()
    coupon = coupons_helper.create_coupon(
        code=generate_random_string(5, prefix="off_")
    )
    coupon_id = coupon["id"]
    yield coupon
    coupons_helper.delete_coupon(
        coupon_id=coupon_id,
        payload=payload
    )
