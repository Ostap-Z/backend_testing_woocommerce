import allure
import pytest

from src.utilities.requests_utility import RequestsUtility


@allure.suite("Customers endpoint")
@allure.feature("Get customers list")
@pytest.mark.customers
class TestGetCustomers:
    requests_helper = RequestsUtility()

    @allure.title(
        "Verify that the user can get a list of all customers"
    )
    @allure.severity(
        severity_level=allure.severity_level.CRITICAL
    )
    @pytest.mark.tcid32
    def test_get_all_customers(self):
        with allure.step(
            "Get all customers"
        ):
            customers_list = self.requests_helper.get("customers")

        with allure.step(
            "Verify that a list of customers has been returned by API"
        ):
            assert customers_list, "API has returned an empty list. " \
                               f"API Response: {customers_list}"
