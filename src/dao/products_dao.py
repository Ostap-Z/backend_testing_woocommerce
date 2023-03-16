import random

import allure

from src.utilities.database_utility import DatabaseUtility


class ProductsDAO:

    def __init__(self):
        self.__db_helper = DatabaseUtility(
            host="localhost",
            port=10006
        )

    def get_random_product(self):
        sql_query = """
        SELECT * FROM local.wp_posts
        WHERE post_type=%s;
        """
        random_product = self.__db_helper.execute_select(sql_query, "product")
        return random_product[
            random.randint(
                1,
                len(random_product)
            )
        ]

    def get_product_by_id(self, product_id):
        sql_query = """
        SELECT * FROM local.wp_posts
        WHERE post_type = %s
        AND ID = %s;
        """
        with allure.step(
          f"Get a product with '{product_id}' id from DB"
        ):
            return self.__db_helper.execute_select(
                sql_query,
                "product",
                product_id
            )

    def get_products_after_given_date(self, _date):
        sql_query = """
        SELECT * FROM local.wp_posts
        WHERE post_type = %s
        AND post_date > %s
        LIMIT 100;
        """

        with allure.step(
            f"Get a products list after date from DB: {_date}"
        ):
            return self.__db_helper.execute_select(
                sql_query,
                "product",
                _date
            )
