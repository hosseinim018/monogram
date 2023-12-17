import requests
import socks
import logging
import re
from functools import wraps
from django.http import HttpResponse

class Monogram:
    def __new__(cls, token, secret_token, endpoint, api_endpoint, proxy, proxy_url,*args, **kwargs):
        cls.token = token
        cls.secret_token = secret_token
        cls.endpoint = endpoint
        cls.api_endpoint = api_endpoint
        cls.proxy = bool(proxy)
        cls.proxy_url = proxy_url
        cls.session = requests.Session()

        return super().__new__(cls)

    def newMessage(self, pattern):
        def decorator(func):
            @wraps(func)
            def wrapper(Message, *args, **kwargs):
                if re.match(pattern, Message.text):
                    return func(Message, *args, **kwargs)
                return HttpResponse("Hello, world!")
            return wrapper
        return decorator


    def request(self, method: str, data: dict, res:bool = False) -> None:
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
        # By default, use SOCKS5 protocol for the proxy
        PROXIES: dict = {
            'http': self.proxy_url,
            'https': self.proxy_url
        }

        # Set PROXIES to the PROXIES dictionary if PROXY is True, otherwise set it to None
        PROXIES = PROXIES if self.proxy else None

        try:
            # Send the request to monogram based on method
            # in config.py if you set PROXY to True session post with PROXIES that you set in config.py
            url = self.api_endpoint + method
            response = self.session.post(url, json=data, proxies=PROXIES)
            response.raise_for_status()  # Raise an exception for non-2xx status codes

        except requests.exceptions.HTTPError as e:
            error_message = str(e)
            logging.exception(f'Failed to edited message. Error message: {error_message}')

        except requests.exceptions.RequestException as e:
            error_message = str(e)
            logging.exception(f'Failed to edited message. Error message: {error_message}')
        if res:
            return response






from cryptography.fernet import Fernet

class TokenEncryptor(Monogram):
    """
    Utility class for encrypting and decrypting tokens using the Fernet encryption algorithm.
    """
    def __new__(cls, *args, **kwargs):
        """
               Encrypts a token string.
        """
        cls.token: str = cls.token
        cls.secret_key: bytes = Fernet.generate_key()  # Generates a random secret key for encryption.
        cls.cipher_suite = Fernet(cls.secret_key)  # Sets up the cipher suite for encryption and decryption.
        # Encrypts a token string:
        cls.encrypted_token: str = cls.cipher_suite.encrypt(cls.token.encode('utf-8')).decode()
    @classmethod
    def decrypt(cls, encrypted_token: bytes) -> str:
        """
        Decrypts an encrypted token.

        Args:
            encrypted_token (bytes): The encrypted token to be decrypted.

        Returns:
            str: The decrypted token.
        """
        decrypted_token = cls.cipher_suite.decrypt(encrypted_token).decode()
        return decrypted_token


def validate_payload(_locals):
    _locals = _locals  # Create a copy of locals()
    # Remove the key cls ir self from _locals
    if 'self' in _locals:
        _locals.pop('self')
    if 'cls' in _locals:
        _locals.pop('cls')
    payload = {k: v for k, v in _locals.items() if v}  # Remove None values from payload
    return payload



from configparser import ConfigParser
from django.conf import settings

def configs(appname, section='monogram'):

    config_path = settings.BASE_DIR / appname / 'config.ini'
    # config_path = os.path.join(settings.BASE_DIR, f"{appname}\config.ini")
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(config_path)
    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, appname))
    return db
