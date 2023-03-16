import allure
import pymysql.cursors

from .credentials_utility import CredentialsUtility


class DatabaseUtility:

    def __init__(
            self,
            host,
            port,
            timeout=20
    ):
        self.__host = host
        self.__port = port
        self.timeout = timeout
        self.__credentials_helper = CredentialsUtility()
        self.__credentials = self.__credentials_helper.get_db_credentials()

    def create_connection(self):
        with allure.step(
            "Create connection with DB: "
            f"db_host={self.__host}, "
            f"db_port={self.__port}, "
            f"db_connection_timeout={self.timeout}"
        ):
            return pymysql.connect(
                host=self.__host,
                port=self.__port,
                user=self.__credentials["db_user"],
                password=self.__credentials["db_password"],
                cursorclass=pymysql.cursors.DictCursor,
                connect_timeout=self.timeout
            )

    def execute_select(
            self,
            sql_query,
            *args
    ):
        connection = self.create_connection()

        with connection:
            with connection.cursor() as cursor:

                with allure.step(
                        f"Execute sql query: {sql_query=}, {args=}"
                ):
                    cursor.execute(sql_query, args)
                result = cursor.fetchall()

        return result
