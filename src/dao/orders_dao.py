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

    def get_order_items_details(
            self,
            line_id
    ):
        sql_query = """
        SELECT *
        FROM local.wp_woocommerce_order_itemmeta
        WHERE order_item_id = %s;
        """
        sql_response = self.__db_helper.execute_select(
                sql_query,
                line_id
            )

        line_details = dict()
        for meta in sql_response:
            line_details[meta["meta_key"]] = meta["meta_value"]

        with allure.step(
                f"Get an order line details with 'line_id' {line_id}: "
                f"{line_details}"
        ):
            return line_details
