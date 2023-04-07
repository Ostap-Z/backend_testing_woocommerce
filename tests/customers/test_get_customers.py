from unittest.mock import Mock, patch

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

    @allure.title(
        "Verify that the API returns an empty list"
        " when no customers has been created"
    )
    @allure.severity(
        severity_level=allure.severity_level.NORMAL
    )
    @pytest.mark.tcid62
    @patch(
        target="src.utilities.requests_utility.RequestsUtility.get"
    )
    def test_get_empty_list_of_customers(
        self,
        _mock: Mock
    ):
        _mock.return_value = Mock(
            **{
                "status_code": 200,
                "json.return_value": []
            }
        )
        with allure.step(
            "Do call to the mocked customers object"
        ):
            customers_mock = self.requests_helper.get("customers")

        with allure.step(
            f"Get a customer status code: {customers_mock.status_code}"
        ):
            customers_status_code = customers_mock.status_code

        with allure.step(
            f"Get a customer response: {customers_mock.json()}"
        ):
            customers_response = customers_mock.json()

        with allure.step(
            "Verify that the customers API response status code is 200"
        ):
            assert customers_status_code == 200, \
                f"Got invalid status code " \
                f"{customers_status_code} instead of 200"

        with allure.step(
            "Verify that the customers API response is empty array"
        ):
            assert customers_response == [], \
                "\nActual result:" \
                "\n\tGot invalid response " \
                "when no customers have been created: " \
                f"{customers_response}" \
                "\nExpected result:" \
                f"\n\tResponse should be empty array: []"
