import pytest

from src.dao.customers_dao import CustomersDAO
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


@pytest.fixture
def random_customer_from_db():
    customer_dao = CustomersDAO()
    return customer_dao.get_random_customer()
