import allure

from src.utilities.database_utility import DatabaseUtility


class CouponsDAO:

    def __init__(self):
        self.__db_helper = DatabaseUtility()

    def get_coupon_by_id(self, coupon_id):
        sql_query = """
        SELECT * FROM local.wp_posts 
        WHERE post_type = %s
        AND ID = %s;
        """

        with allure.step(f"Get a coupon with '{coupon_id}' id from DB"):
            return self.__db_helper.execute_select(
                sql_query,
                "shop_coupon",
                coupon_id
            )
