import random

import allure

from src.utilities.database_utility import DatabaseUtility


class CustomersDAO:

    def __init__(self):
        # self.__db_helper = DatabaseUtility(
        #     host="localhost",
        #     port=10006
        # )
        self.__db_helper = DatabaseUtility()

    def get_customer_by_email(self, email):
        sql_query = """
        SELECT * FROM local.wp_users
        WHERE user_email=%s;
        """

        with allure.step(f"Get a customer with '{email}' email from DB"):
            return self.__db_helper.execute_select(
                sql_query,
                email
            )

    def get_random_customer(self):
        sql_query = """
        SELECT * FROM local.wp_users
        ORDER BY id DESC
        LIMIT 100;
        """
        customers = self.__db_helper.execute_select(sql_query)
        random_customer = customers[
            random.randint(
                1,
                len(customers)
            )
        ]

        with allure.step(f"Get a random customer from DB: {random_customer}"):
            return random_customer
