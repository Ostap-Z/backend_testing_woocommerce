import os

import allure
import pymysql.cursors

from .credentials_utility import CredentialsUtility
from src.configs.hosts_config import DB_HOST


class DatabaseUtility:
    _credentials_helper = CredentialsUtility()

    def __init__(self, timeout=15):
        self.timeout = timeout

        if not (
                os.environ["MACHINE"],
                os.environ["WP_HOST"]
        ):
            raise Exception(
                "Environment variable 'MACHINE' "
                "and 'WP_HOST' should be set"
            )
        self.__machine = os.environ["MACHINE"]
        self.__wp_host = os.environ["WP_HOST"]

        if self.__machine == "docker" and self.__wp_host == "local":
            raise Exception(
                "Can't run tests in docker when 'WP_HOST'=local"
            )

        self.__env = os.environ.get("ENV", "dev")
        self.__host = \
            DB_HOST[self.__machine][self.__env]["host"]
        self.__socket = \
            DB_HOST[self.__machine][self.__env]["socket"]
        self.__port = \
            DB_HOST[self.__machine][self.__env]["port"]
        self.__database = \
            DB_HOST[self.__machine][self.__env]["database"]
        self.__table_prefix = \
            DB_HOST[self.__machine][self.__env]["table_prefix"]
        self.__user = \
            self._credentials_helper.get_db_credentials()["db_user"]
        self.__password = \
            self._credentials_helper.get_db_credentials()["db_password"]

    def create_connection(self):
        if self.__wp_host == "local":
            connection = pymysql.connect(
                host=self.__host,
                unix_socket=self.__socket,
                user=self.__user,
                password=self.__password,
                connect_timeout=self.timeout,
                cursorclass=pymysql.cursors.DictCursor
            )
        elif self.__wp_host == "ampps":
            connection = pymysql.connect(
                host=self.__host,
                port=self.__port,
                user=self.__user,
                password=self.__password,
                connect_timeout=self.timeout,
                cursorclass=pymysql.cursors.DictCursor
            )
        else:
            raise Exception(
                f"Unknown 'WP_HOST': {os.environ['WP_HOST']}. "
                "Available hosts: local, ampps"
            )

        with allure.step(
            "Create a connection to the DB: "
            f"{self.__host=}, {self.__port=}, {self.__socket=}"
        ):
            return connection

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
