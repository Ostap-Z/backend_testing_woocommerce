import allure
import pytest

from src.utilities.requests_utility import RequestsUtility
from src.dao.products_dao import ProductsDAO
from src.helpers.products_helper import ProductsHelper


@allure.suite("Products endpoint")
@allure.feature("Get products")
@pytest.mark.products
class TestGetProducts:
    requests_helper = RequestsUtility()
    products_dao = ProductsDAO()
    products_helper = ProductsHelper()

    @allure.title(
        "Verify that the user can get a list of all products"
    )
    @allure.severity(
        severity_level=allure.severity_level.CRITICAL
    )
    @pytest.mark.tcid33
    def test_get_products_all_list(self):
        with allure.step(
            "Get all products"
        ):
            products_list = self.requests_helper.get("products")

        with allure.step(
            "Verify that a list of products has been returned by API"
        ):
            assert products_list, \
                "API has returned an empty list. " \
                f"API Response: {products_list}"

    @allure.title(
        "Verify that the user can get a specific product by ID"
    )
    @allure.severity(
        severity_level=allure.severity_level.CRITICAL
    )
    @pytest.mark.tcid34
    def test_get_product_by_id(
        self,
        random_product_from_db,
        product_by_id_api
    ):
        with allure.step(
            "Get a product 'ID' from DB: "
            f"{random_product_from_db['ID']}"
        ):
            product_id_db = random_product_from_db["ID"]

        with allure.step(
            "Get a product 'post_title' from DB: "
            f"{random_product_from_db['post_title']}"
        ):
            product_db_name = random_product_from_db["post_title"]

        with allure.step(
            "Get a product name with id "
            f"{product_id_db} from API response"
        ):
            product_api_name = product_by_id_api["name"]

        with allure.step(
            f"Verify that the product name with id {product_id_db} "
            "in API response equals to the post_title in DB: "
            f"{product_api_name=}, {product_db_name=}"
        ):
            assert product_api_name == product_db_name, \
                "\nActual result:" \
                "\n\tProduct name in the API response " \
                "doesn't match a product name in the database: " \
                f"\n\t{product_id_db=}, " \
                f"\n\t{product_db_name=}, " \
                f"\n\t{product_api_name=}" \
                "\nExpected result:" \
                "\n\tProduct name in the API response " \
                "should be matched with a product name in the database"

    @allure.title(
        "Verify that the user can get a list of products "
        "based on the filter 'after'"
    )
    @allure.severity(
        severity_level=allure.severity_level.NORMAL
    )
    @pytest.mark.tcid38
    def test_get_products_with_filter_after(
        self,
        payload_after_parameter
    ):
        with allure.step(
            "Get a products list after date from API: "
            f"{payload_after_parameter}"
        ):
            products_api = self.products_helper\
                .get_products_with_params(payload_after_parameter)

        with allure.step(
            "Get a list of products after date from DB: "
            f"{payload_after_parameter}"
        ):
            products_db = \
                self.products_dao\
                    .get_products_after_given_date(
                     payload_after_parameter["after"])

        with allure.step(
            "Sort taken IDs from API and DB in ascending order"
        ):
            api_items_ids = sorted(
                [api_item_id["id"] for api_item_id in products_api]
            )
            db_items_ids = sorted(
                [db_item_id["ID"] for db_item_id in products_db]
            )

        with allure.step(
          "Verify that API IDs in response equals to the DB IDs response: "
          f"{api_items_ids=}, {db_items_ids=}"
        ):
            assert api_items_ids == db_items_ids, \
                "\nActual result:" \
                "\n\tReturned product IDs in response mismatch in database:" \
                f"\n\t{api_items_ids=}, {db_items_ids=}" \
                "\nExpected result:" \
                "\n\tReturned product IDs in response " \
                "should be matched with IDs in database"
