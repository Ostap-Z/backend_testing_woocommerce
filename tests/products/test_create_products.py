import allure
import pytest

from src.utilities.generator_utility import generate_random_string
from src.helpers.products_helper import ProductsHelper
from src.dao.products_dao import ProductsDAO


@allure.suite("Products endpoint")
@allure.feature("Create products")
@pytest.mark.products
class TestCreateProducts:
    products_helper = ProductsHelper()
    products_dao = ProductsDAO()

    @allure.title(
        "Verify that the user can create a simple product"
    )
    @allure.severity(
        severity_level=allure.severity_level.CRITICAL
    )
    @pytest.mark.tcid35
    def test_create_simple_product(self):
        payload = {
            "name": generate_random_string(20),
            "type": "simple",
            "regular_price": "9.99"
        }

        with allure.step(
          f"Create a simple product with data: {payload}"
        ):
            product_response = self.products_helper.create_product(payload)

        with allure.step(
            "Get a product name in API response: "
            f"{product_response['name']}"
        ):
            product_response_name = product_response["name"]

        payload_name = payload["name"]

        with allure.step(
          "Verify that product response is not empty"
        ):
            assert product_response, \
                f"Create product API response is empty. Payload: {payload}"

        with allure.step(
          "Verify that product name in API response "
          "is equal to the name in payload: "
          f"{product_response_name=}, {payload_name=}"
        ):
            assert product_response_name == payload_name, \
                "\nActual result: " \
                "\n\tCreate product name in the response has invalid name: " \
                f"{product_response_name}" \
                "\nExpected result: " \
                f"\n\tCreate product name in the response should be: " \
                f"{payload_name}"

    @allure.title(
        "Verify that created simple product exists in the database"
    )
    @allure.severity(
        severity_level=allure.severity_level.CRITICAL
    )
    @pytest.mark.tcid36
    def test_created_simple_product_exists_in_db(self):
        payload = {
            "name": generate_random_string(20),
            "type": "simple",
            "regular_price": "9.99"
        }

        with allure.step(
          f"Create a simple product with data: {payload}"
        ):
            product = self.products_helper.create_product(payload)

        with allure.step(
            "Get a simple product 'id' from API response: "
            f"{product['id']}"
        ):
            product_id = product["id"]

        with allure.step(
          f"Get a product name with '{product_id}' id from API response: "
          f"{product['name']}"
        ):
            product_api_name = product["name"]

        with allure.step(
          f"Get a simple product with '{product_id}' id from DB"
        ):
            product_db = self.products_dao.get_product_by_id(product_id)

        with allure.step(
          f"Get a product post_title with '{product_id}' id from DB: "
          f"{product_db[0]['post_title']}"
        ):
            product_db_name = product_db[0]["post_title"]

        with allure.step(
            f"Verify that the product api name '{product_api_name}' "
            f"equals to the post_title '{product_db_name}' in DB"
        ):
            assert product_api_name == product_db_name, \
                "\nActual result: " \
                "\n\tCreate product has invalid name in the database: " \
                f"{product_db_name}" \
                "\nExpected result: " \
                f"\n\tCreate product name in the database should be: " \
                f"{product_api_name}"
