from monogram.bot.config import PROXIES, API_ENDPOINT
import requests
import socks
import logging


session = requests.Session()


def telegram(method: str, data: dict) -> None:
    """
    send POST request to monogram based on monogram methods API.

    Args:
        method (str): method name of monogram api
        data (dict): data is data we want send to monogram.
        it can be contain text message and keyboard

    Returns:
        None

    Raises:
        requests.exceptions.HTTPError: If there is an HTTP error during the request.
        requests.exceptions.RequestException: If there is a general request exception.
    """

    try:
        # Send the request to monogram based on method
        # in config.py if you set PROXY to True session post with PROXIES that you set in config.py
        response = session.post(API_ENDPOINT + method, json=data, proxies=PROXIES)
        response.raise_for_status()  # Raise an exception for non-2xx status codes

    except requests.exceptions.HTTPError as e:
        error_message = str(e)
        logging.exception(f'Failed to edited message. Error message: {error_message}')

    except requests.exceptions.RequestException as e:
        error_message = str(e)
        logging.exception(f'Failed to edited message. Error message: {error_message}')
