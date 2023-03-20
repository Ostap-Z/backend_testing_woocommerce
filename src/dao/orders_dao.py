import allure

from src.utilities.database_utility import DatabaseUtility


class OrdersDAO:

    def __init__(self):
        self.__db_helper = DatabaseUtility(
            host="localhost",
            port=10006
        )

    def get_order_items_by_order_id(
            self,
            order_id
    ):
        sql_query = """
        SELECT *
        FROM local.wp_woocommerce_order_items
        WHERE order_id = %s;
        """
        with allure.step(
            f"Get an order item with order id {order_id}"
        ):
            return self.__db_helper.execute_select(
                sql_query,
                order_id
            )
