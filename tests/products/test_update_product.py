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
            assert updated_price == regular_price_payload, \
                "\nActual result:" \
                "\n\t'price' parameter has not been updated " \
                f"with {regular_price_payload}" \
                f"\n\tActual price: {updated_price}" \
                "\nExpected result:" \
                "\n\t'price' parameter should be updated " \
                f"with {regular_price_payload}"

    @allure.title(
        "Verify that the update 'sale_price > 0' sets 'on_sale'=True"
    )
    @allure.severity(
        severity_level=allure.severity_level.CRITICAL
    )
    @pytest.mark.tcid58
    def test_update_product_sale_price(
        self,
        simple_product
    ):
        with allure.step(
          f"Get the product id: {simple_product['id']}"
        ):
            product_id = simple_product["id"]

        payload = {
            "sale_price": "1"
        }

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
            "Get the on_sale status from updated product "
            f"with id {product_id}: {updated_product['on_sale']}"
        ):
            product_on_sale = updated_product['on_sale']

        with allure.step(
            "Verify that the on_sale status is True"
        ):
            assert product_on_sale, \
                "\nActual result:" \
                "\n\t'on_sale' parameter is not True " \
                "after updating with 'sale_price > 0'" \
                f"\n\tActual 'on_sale' status: {product_on_sale}" \
                f"\n\tPayload: {payload}" \
                f"\nExpected result:" \
                f"\n\t'on_sale' parameter should ne equaled to true " \
                f"after updating with 'sale_price > 0'"
