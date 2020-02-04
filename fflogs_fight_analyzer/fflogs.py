from typing import Optional
import logging
import os
import sys
import requests

FF_LOGS_BASE_URL = "https://www.fflogs.com/"
FF_LOGS_API_URL = FF_LOGS_BASE_URL + "v1/"
FF_LOGS_CLASSES_URL = FF_LOGS_API_URL + "classes"


def _get_api_key() -> str:
    api_key = os.getenv("FF_LOGS_API_KEY")
    if not api_key:
        api_key = input("Enter your FF Logs API public key (https://www.fflogs.com/profile): ")
    return api_key


class Client:
    logger = logging.getLogger(__name__)

    def __init__(self, api_key: str = None):
        self.logger.debug("Attempting to connect to FF Logs...")
        if not self._establish_connection():
            self.logger.error("Unable to establish connection with FF Logs... Exiting.")
            sys.exit(1)
        self.logger.debug("Successfully established connection.")

        if not api_key:
            api_key = _get_api_key()

        self.logger.debug("Validating API key...")
        if not self._validate_api_key(api_key):
            self.logger.error("Unable to authenticate. Please check your API key and try again.")
            sys.exit(1)
        self.logger.debug("Successfully validated FF Logs API key.")
        self.api_key = api_key

    def _get(self, url: str, params: dict = None) -> Optional[requests.Response]:
        try:
            response = requests.get(url, params)
            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError:
            self.logger.error("HTTP request error.", exc_info=True)
        except requests.exceptions.Timeout:
            self.logger.error("HTTP request timeout.", exc_info=True)
        except requests.exceptions.RequestException:
            self.logger.error("A fatal error has occurred.", exc_info=True)
        return None

    def _establish_connection(self) -> Optional[requests.Response]:
        return self._get(FF_LOGS_BASE_URL)

    def _validate_api_key(self, api_key: str) -> Optional[requests.Response]:
        return self._get(FF_LOGS_CLASSES_URL, {"api_key": api_key})

    def get(self, api_endpoint: str, parameters: dict = None) -> Optional[requests.Response]:
        request_url = FF_LOGS_API_URL + api_endpoint
        if not parameters:
            parameters = {}
        parameters["api_key"] = self.api_key
        return self._get(request_url, parameters)
