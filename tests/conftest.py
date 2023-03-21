import pytest

from src.dao.products_dao import ProductsDAO
from src.helpers.customers_helper import CustomerHelper


@pytest.fixture
def random_product_from_db():
    product_dao = ProductsDAO()
    return product_dao.get_random_product()


@pytest.fixture
def customer():
    customer_helper = CustomerHelper()
    return customer_helper.create_customer()
