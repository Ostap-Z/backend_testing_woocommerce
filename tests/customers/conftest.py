import pytest

from src.utilities.generator_utility import \
    generate_random_email, \
    generate_random_password


@pytest.fixture
def customer_credentials():
    return {
        "email": generate_random_email(),
        "password": generate_random_password()
    }


@pytest.fixture
def customer_existing_credentials(random_customer_from_db):
    return {
        "email": random_customer_from_db["user_email"],
        "password": generate_random_password()
    }
