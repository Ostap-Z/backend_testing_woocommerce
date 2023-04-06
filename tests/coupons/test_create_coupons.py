import allure
import pytest

from src.helpers.coupons_helper import CouponsHelper
from src.utilities.generator_utility import generate_random_string
from src.utilities.requests_utility import RequestsUtility
from src.dao.coupons_dao import CouponsDAO


@allure.suite("Coupons endpoint")
@allure.feature("Create coupons")
@pytest.mark.coupons
class TestCreateCoupons:
    coupons_helper = CouponsHelper()
    requests_utility = RequestsUtility()
    coupons_dao = CouponsDAO()

    @allure.title(
        "Verify that the user can create a coupon "
        "with {discount_type} discount type"
    )
    @allure.severity(
        severity_level=allure.severity_level.CRITICAL
    )
    @pytest.mark.tcid59
    @pytest.mark.parametrize(
        "discount_type,expected",
        [
            ("percent", "percent"),
            ("fixed_cart", "fixed_cart"),
            ("fixed_product", "fixed_product")
        ]
    )
    def test_create_coupon_discount_type(
        self,
        discount_type,
        expected
    ):
        with allure.step(
            f"Create a coupon with discount_type: {discount_type}"
        ):
            coupon_response = self.coupons_helper.create_coupon(
                code=generate_random_string(10, prefix="off_"),
                discount_type=discount_type
            )

        with allure.step(
            f"Get a coupon id from API response: {coupon_response['id']}"
        ):
            coupon_id = coupon_response['id']

        with allure.step(
            f"Get a coupon with id: {coupon_id}"
        ):
            coupon = self.coupons_helper.get_coupon_by_id(coupon_id)

        with allure.step(
            f"Get a discount type from coupon with id {coupon_id}: "
            f"{coupon['discount_type']}"
        ):
            coupon_discount_type = coupon['discount_type']

        with allure.step(
            f"Verify that the discount_type of created coupon is {expected}"
        ):
            assert coupon_discount_type == expected, \
                "\nActual result:" \
                f"\n\tThe discount_type is not equals to the {expected} " \
                "when the coupon has been created " \
                f"with {discount_type} discount_type" \
                f"\n\tActual discount_type: {coupon_discount_type}" \
                "\nExpected result:" \
                "\n\tThe discount_type should be equaled " \
                f"to the {expected} when the user creates a coupon " \
                f"with {discount_type} discount_type"

    @allure.title(
        "Verify that the user can get a correct message "
        "when creates a coupon with invalid discount_type"
    )
    @allure.severity(
        severity_level=allure.severity_level.NORMAL
    )
    @pytest.mark.tcid60
    def test_create_coupon_invalid_discount_type(self):
        payload = {
            "code": generate_random_string(10, prefix="off_"),
            "discount_type": generate_random_string(5, prefix="invalid_")
        }

        with allure.step(
            "Create a coupon with invalid discount_type: "
            f"{payload['discount_type']}"
        ):
            coupon_response = self.requests_utility.post(
                "coupons",
                payload=payload,
                expected_status_code=400
            )

        with allure.step(
            "Get a error message from API response: "
            f"{coupon_response['message']}"
        ):
            error_message = coupon_response["message"]

        with allure.step(
            "Verify that the error message is "
            "'Invalid parameter(s): discount_type' "
            "when a user creates a coupon "
            f"with invalid '{payload['discount_type']}' discount_type"
        ):
            assert error_message == 'Invalid parameter(s): discount_type', \
                "\nActual result:" \
                "\n\tThe user got invalid error message " \
                "when coupon with discount_type " \
                f"{payload['discount_type']} has been created: " \
                f"{error_message}" \
                "\nExpected result:" \
                "\n\tThe error message should be: " \
                "Invalid parameter(s): discount_type"

    @allure.title(
        "Verify that the created coupon "
        "is present in DB and has the correct ID"
    )
    @allure.severity(
        severity_level=allure.severity_level.CRITICAL
    )
    @pytest.mark.tcid61
    def test_created_coupon_exists_in_db(
        self,
        coupon
    ):
        with allure.step(
            f"Get a coupon id from API response: {coupon['id']}"
        ):
            coupon_id_api = coupon["id"]

        with allure.step(
            f"Get a coupon from DB with id: {coupon_id_api}"
        ):
            coupon_db = self.coupons_dao.get_coupon_by_id(coupon_id_api)

        with allure.step(
            f"Get a coupon id from DB response: {coupon_db[0]['ID']}"
        ):
            coupon_id_db = coupon_db[0]["ID"]

        with allure.step(
            "Verify that the coupon id in DB "
            "equals to the coupon id in API: "
            f"{coupon_id_db=}, {coupon_id_api=}"
        ):
            assert coupon_id_db == coupon_id_api, \
                "\nActual result:" \
                f"\n\tCreated coupon by API with id {coupon_id_api} " \
                f"has invalid id {coupon_id_db} in DB" \
                "\nExpected result:" \
                "\n\tCreated coupon should has " \
                f"{coupon_id_api} coupon id in DB"
