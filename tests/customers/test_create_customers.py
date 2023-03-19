import pytest
import allure

from src.utilities.generator_utility import \
    generate_random_email, \
    generate_random_password
from src.helpers.customers_helper import CustomerHelper
from src.dao.customers_dao import CustomersDAO
from src.utilities.requests_utility import RequestsUtility


@allure.suite("Customers endpoint")
@allure.feature("Create customers")
@pytest.mark.customers
class TestCreateCustomers:
    customer_helper = CustomerHelper()
    customer_dao = CustomersDAO()
    requests_helper = RequestsUtility()

    @allure.title(
        "Create customer and verify API Response email"
    )
    @allure.severity(
        severity_level=allure.severity_level.CRITICAL
    )
    @pytest.mark.tcid29
    def test_create_customer_email(self):
        email = generate_random_email()
        password = generate_random_password()
        customer_api_info = self.customer_helper.create_customer(
            email=email,
            password=password
        )

        with allure.step(
            f"Verify that API response email equals to the '{email}'"
        ):
            assert customer_api_info["email"] == email, \
                f"\nActual email: {customer_api_info['email']}" \
                f"\nExpected email: {email}"

    @allure.title(
        "Create customer and verify API Response username"
    )
    @allure.severity(
        severity_level=allure.severity_level.CRITICAL
    )
    @pytest.mark.tcid30
    def test_create_customer_username(self):
        email = generate_random_email()
        password = generate_random_password()
        customer_api_info = self.customer_helper.create_customer(
            email=email,
            password=password
        )

        with allure.step(
                "Verify that API response username "
                f"equals to the '{email.split('@')[0]}'"
        ):
            assert customer_api_info["username"] == \
                   email.split("@")[0], \
                   f"\nActual username: {customer_api_info['username']}" \
                   f"\nExpected username: " \
                   f"{customer_api_info['email'].split('@')[0]}"

    @allure.title(
        "Verify that created customer exists in the database"
    )
    @allure.severity(
        severity_level=allure.severity_level.CRITICAL
    )
    @pytest.mark.tcid31
    def test_created_customer_exists_in_db(self):
        email = generate_random_email()
        password = generate_random_password()

        customer_api_info = self.customer_helper.create_customer(
            email=email,
            password=password
        )
        customer_db_info = self.customer_dao.get_customer_by_email(email)

        with allure.step(
            f"Get a '{email}' customer ID returned by DB"
        ):
            customer_db_id = customer_db_info[0]["ID"]

        with allure.step(
            f"Get a '{email}' customer ID returned by API"
        ):
            customer_api_id = customer_api_info["id"]

        with allure.step(
            f"Verify that the {customer_api_id=} "
            f"equals to the {customer_db_id=}"
        ):
            assert customer_api_id == customer_db_id, \
                "\nActual result:" \
                "\n\tCustomer api id not equals to the customer db id" \
                f"\n\tActual data: {customer_api_id=}, {customer_db_id=}" \
                f"\nExpected result:" \
                f"\n\tCustomer api id should be equaled to the customer db id"

    @allure.title(
        "Verify that an error message appears "
        "when a user creates an account with email "
        "that has already exists in the database"
    )
    @allure.severity(
        severity_level=allure.severity_level.NORMAL
    )
    @pytest.mark.tcid47
    def test_create_customer_with_existing_email(self):
        with allure.step(
            "Get the existing customer email from DB"
        ):
            existing_customer_email = \
                self.customer_dao.get_random_customer()["user_email"]

        payload = {
            "email": existing_customer_email,
            "password": generate_random_password()
        }

        with allure.step(
            f"Create a customer with existing '{payload['email']}' email"
        ):
            customer_api_info = self.requests_helper.post(
                endpoint="customers",
                payload=payload,
                expected_status_code=400
            )

        with allure.step(
            "Verify that the message in API response is correct"
        ):
            assert customer_api_info["message"] == \
                'An account is already registered with your email address. ' \
                '<a href="#" class="showlogin">Please log in.</a>', \
                "\nActual result:" \
                f"\n\tActual response 'message' is not correct: " \
                f"{customer_api_info['message']}" \
                "\nExpected result:" \
                "\n\tExpected response 'message' should be equaled to: " \
                "'An account is already registered with your email address. " \
                "<a href='#' class='showlogin'>Please log in.</a>'"
