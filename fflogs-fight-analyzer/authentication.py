import os
import requests
import sys


def _get_api_key():
    api_key = os.getenv("FFLOGS_API_KEY")
    if not api_key:
        api_key = input("Enter your FF Logs API public key (https://www.fflogs.com/profile): ")
    return api_key


def _validate_api_key(api_key):
    try:
        response = requests.get("https://www.fflogs.com:443/v1/classes", {"api_key": api_key})
        if response.status_code != 200:
            print("Unable to authenticate with FF Logs. Please check your API key and try again.")
            sys.exit(1)
        else:
            print("Authentication successful!")
    except requests.exceptions.Timeout:
        print("Authentication request timed out. Is FF Logs down?")
    except requests.exceptions.RequestException as error:
        print(error)
        print("A fatal error has occurred attempting to authenticate to FF Logs.")
        sys.exit(1)


if __name__ == "__main__":
    _validate_api_key(_get_api_key())
