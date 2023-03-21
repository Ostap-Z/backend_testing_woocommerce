import random
from datetime import datetime, timedelta


import pytest

from src.helpers.products_helper import ProductsHelper
from src.utilities.generator_utility import generate_random_string


@pytest.fixture
def product_by_id_api(random_product_from_db):
    products_helper = ProductsHelper()
    product_id = random_product_from_db["ID"]

    return products_helper.get_product_by_id(product_id)


@pytest.fixture
def payload_after_parameter():
    days_from_today = 30

    _after_created_date = \
        datetime.now().replace(microsecond=0) \
        - timedelta(days=days_from_today)

    after_created_date = _after_created_date.isoformat()
    return {
        "after": after_created_date
    }


@pytest.fixture
def payload_simple_product():
    return {
        "name": generate_random_string(20),
        "type": "simple",
        "regular_price": str(random.randint(1, 999_999))
    }
