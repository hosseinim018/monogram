import hashlib
from configparser import ConfigParser
from django.conf import settings
import os

config_path = os.path.join(settings.BASE_DIR, "telegram/bot/config.ini")
config = ConfigParser()
config.read(config_path)
def configs(filename='config.ini', section='admins'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db
configs = configs(filename=config_path, section='telegram')

class monogram:
    def __init__(self, token, secret_token, endpoint, proxy, proxy_url):
        self.token = token
        self.secret_token = secret_token
        self.endpoint = endpoint
        self.proxy = proxy
        self.proxy_url = proxy_url


print(config)
# Each bot is given a unique authentication token when it is created.
# The token looks something like 123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11
# Replace 'YOUR_BOT_TOKEN' with your actual bot token obtained from @BotFather in Telegram
# TOKEN: str = config.get('telegram', 'token')
TOKEN: str = '968534296:AAG6OR6RNnBKhwLk8DR1b6SjIoSVUpTxu6Y'

# Hash TOKEN with hashlib.sha256
# SECRET_TOKEN = hashlib.sha256(TOKEN.encode('utf-8')).hexdigest()

# Use the default API endpoint of Telegram. If you want to use a local Bot API server,
# replace it with the URL of your local server
ENDPOINT: str = "api.telegram.org"

# API_ENDPOINT is the URL for the Telegram API based on the TOKEN and ENDPOINT
API_ENDPOINT: str = "https://" + ENDPOINT + f"/bot{TOKEN}/"

# If you want to use a proxy, change the PROXY variable to True; otherwise, set it to False.
# By default, it is set to True because Telegram is filtered in Iran.
# After deploying on the server, make sure to set it to False.
PROXY: bool = True

# By default, use SOCKS5 protocol for the proxy
PROXIES: dict = {
    'http': 'socks5h://127.0.0.1:10808',
    'https': 'socks5h://127.0.0.1:10808'
}

# Set PROXIES to the PROXIES dictionary if PROXY is True, otherwise set it to None
PROXIES = PROXIES if PROXY else None


# in this dictionary add function
from telegram.Updates import Callback_Queries, Messages

UPDATE_HANDLER = {
    'callback_query': [
        Callback_Queries.cq1
    ],
    'message': [
        Messages.nm,
        Messages.start,
        Messages.conv
    ],
}
