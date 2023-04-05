import allure

from src.utilities.generator_utility import \
    generate_random_email, \
    generate_random_password
from src.utilities.requests_utility import RequestsUtility


class CustomerHelper:
    def __init__(self):
        self.request_utility = RequestsUtility()

    def create_customer(
        self,
        email=None,
        password=None,
        **kwargs
    ):
        if not email:
            email = generate_random_email()
        if not password:
            password = generate_random_password()

        payload = {
            "email": email,
            "password": password
        } | kwargs

        with allure.step(f"Create a customer with email: {payload['email']}"):
            return self.request_utility.post(
                endpoint="customers",
                payload=payload,
                expected_status_code=201
            )

    def delete_customer(
        self,
        customer_id,
        payload
    ):
        if "force" not in payload.keys():
            payload.set_default("force", True)

        with allure.step(f"Delete a customer with id: {customer_id}"):
            return self.request_utility.delete(
                endpoint=f"customers/{customer_id}",
                payload=payload
            )
