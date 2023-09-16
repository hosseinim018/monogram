from telegram.bot.config import API, PROXIES
import requests
import socks
import logging


session = requests.Session()

def telegram(method: str, data: dict) -> None:
    """
    send POST request to telegram based on telegram methods API.

    Args:
        method (str): method name of telegram api
        data (dict): data is data we want send to telegram.
        it can be contain text message and keyboard

    Returns:
        None

    Raises:
        requests.exceptions.HTTPError: If there is an HTTP error during the request.
        requests.exceptions.RequestException: If there is a general request exception.
    """

    try:
        # Send the request to telegram based on method
        # in config.py if you set PROXY to True session post with PROXIES that you set in config.py
        response = session.post(API[method], json=data, proxies=PROXIES)
        response.raise_for_status()  # Raise an exception for non-2xx status codes

    except requests.exceptions.HTTPError as e:
        error_message = str(e)
        logging.exception(f'Failed to edited message. Error message: {error_message}')

    except requests.exceptions.RequestException as e:
        error_message = str(e)
        logging.exception(f'Failed to edited message. Error message: {error_message}')
