import os
import json

import allure
import requests
from requests_oauthlib import OAuth1

from src.configs.hosts_config import API_HOST
from .credentials_utility import CredentialsUtility


class RequestsUtility:

    def __init__(self):
        self.__env = os.environ.get("ENV", "dev")
        self.__base_url = API_HOST[self.__env]
        self.__auth = OAuth1(
            CredentialsUtility.get_wc_api_keys()["api_key"],
            CredentialsUtility.get_wc_api_keys()["api_secret"]
        )

    def post(
        self,
        endpoint,
        payload=None,
        headers=None,
        expected_status_code=200
    ):
        url = f"{self.__base_url}{endpoint}"
        if not headers:
            headers = {
                "Content-Type": "application/json"
            }

            with allure.step(
                "Do POST call with data: "
                f"{url=}, {payload=}, {headers=}"
            ):
                response = requests.post(
                    url=url,
                    data=json.dumps(payload),
                    headers=headers,
                    auth=self.__auth
                )
        self.assert_status_code(response, expected_status_code)
        return response.json()

    def get(
        self,
        endpoint,
        payload=None,
        headers=None,
        expected_status_code=200
    ):
        url = f"{self.__base_url}{endpoint}"
        if not headers:
            headers = {
                "Content-Type": "application/json"
            }

        with allure.step(
            "Do GET call with data: "
            f"{url=}, {payload=}, {headers=}"
        ):
            response = requests.get(
                url=url,
                data=json.dumps(payload),
                headers=headers,
                auth=self.__auth
            )

        self.assert_status_code(response, expected_status_code)
        return response.json()

    def put(
        self,
        endpoint,
        payload=None,
        headers=None,
        expected_status_code=200
    ):
        url = f"{self.__base_url}{endpoint}"
        if not headers:
            headers = {
                "Content-Type": "application/json"
            }

        with allure.step(
            "Do PUT call with data: "
            f"{url=}, {payload=}, {headers=}"
        ):
            response = requests.put(
                url=url,
                data=json.dumps(payload),
                headers=headers,
                auth=self.__auth
            )

        self.assert_status_code(response, expected_status_code)
        return response.json()

    def delete(
        self,
        endpoint,
        payload=None,
        headers=None,
        expected_status_code=200
    ):
        url = f"{self.__base_url}{endpoint}"
        if not headers:
            headers = {
                "Content-Type": "application/json"
            }

        with allure.step(
            "Do DELETE call with data: "
            f"{url=}, {payload=}, {headers=}"
        ):
            response = requests.delete(
                url=url,
                data=json.dumps(payload),
                headers=headers,
                auth=self.__auth
            )

        self.assert_status_code(response, expected_status_code)
        return response.json()

    @staticmethod
    def assert_status_code(
            response,
            expected_status_code
    ):
        with allure.step(
                "Verify that expected status code of response is "
                f"{expected_status_code}"
        ):
            assert response.status_code == expected_status_code, \
                f"\nActual status code: {response.status_code}" \
                f"\nActual response: {response.json()}" \
                f"\nExpected status code: {expected_status_code}"
