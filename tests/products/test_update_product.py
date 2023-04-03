import random

import allure
import pytest

from src.helpers.products_helper import ProductsHelper


class TestUpdateProduct:
    products_helper = ProductsHelper()

    @allure.title(
        "Verify that the user has an opportunity "
        "to update the product price"
    )
    @allure.severity(
        severity_level=allure.severity_level.CRITICAL
    )
    @pytest.mark.tcid57
    def test_update_product_price(
        self,
        product_by_id_api
    ):
        with allure.step(
          f"Get the product id: {product_by_id_api['id']}"
        ):
            product_id = product_by_id_api['id']

        payload = {
            "regular_price": str(random.randint(1, 999_999))
        }

        with allure.step(
            "Get the regular_price from payload: "
            f"{payload['regular_price']}"
        ):
            regular_price_payload = payload["regular_price"]

        with allure.step(
          "Update the product with data: "
          f"{product_id=}, {payload=}"
        ):
            self.products_helper.update_product(
                product_id,
                payload
            )

        with allure.step(
            f"Get the updated product with id: {product_id}"
        ):
            updated_product = self.products_helper.get_product_by_id(product_id)

        with allure.step(
            f"Get the price from updated product with id {product_id}: "
            f"{updated_product['price']}"
        ):
            updated_price = updated_product["price"]

        with allure.step(
          "Verify that the price has been updated "
          f"with {regular_price_payload}"
        ):
            assert updated_price == regular_price_payload
