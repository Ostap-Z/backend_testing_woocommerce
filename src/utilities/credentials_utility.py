import os


class CredentialsUtility:

    @staticmethod
    def get_wc_api_keys():
        api_key = os.environ["WC_KEY"]
        api_secret = os.environ["WC_SECRET"]
        return {
            "api_key": api_key,
            "api_secret": api_secret
        }

    @staticmethod
    def get_db_credentials():
        db_user = os.environ["DB_USER"]
        db_password = os.environ["DB_PASSWORD"]
        return {
            "db_user": db_user,
            "db_password": db_password
        }
