import requests

from framework.logger.logger import Logger

logger = Logger()


class MyRequests:
    @staticmethod
    def post(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        return MyRequests._send(url, data, headers, cookies, "POST")

    @staticmethod
    def get(url: str, data: dict = None, headers: dict = {}, cookies: dict = {}):
        return MyRequests._send(url, data, headers, cookies, "GET")

    @staticmethod
    def put(url: str, data: dict = None, headers: dict = {}, cookies: dict = {}):
        return MyRequests._send(url, data, headers, cookies, "PUT")

    @staticmethod
    def delete(url: str, data: dict = None, headers: dict = {}, cookies: dict = {}):
        return MyRequests._send(url, data, headers, cookies, "DELETE")

    @staticmethod
    def patch(url: str, data: dict = None, headers: dict = {}, cookies: dict = {}):
        return MyRequests._send(url, data, headers, cookies, "PATCH")

    @staticmethod
    def _send(url: str, data: dict, headers: dict, cookies: dict, method: str):

        url = f"https://playground.learnqa.ru/api/{url}"
        if method == "GET":
            response = requests.get(url, params=data, headers=headers, cookies=cookies)
        elif method in ("POST", "PUT", "DELETE", "PATCH"):
            response = requests.request(url, method=method, params=data, headers=headers, cookies=cookies)
        else:
            raise Exception(f"Bad HTTP method '{method}' was received")
        logger.api(response)

        return response
