# Each bot is given a unique authentication token when it is created.
# The token looks something like 123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11
# Replace 'YOUR_BOT_TOKEN' with your actual bot token obtained from @BotFather in Telegram
TOKEN: str = '968534296:AAG6OR6RNnBKhwLk8DR1b6SjIoSVUpTxu6Y'

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
# note: use socks5h if you using anaconda and install PySocks.
PROXY_URL = 'socks5h://127.0.0.1:10808'
PROXIES: dict = {
    'http': PROXY_URL,
    'https': PROXY_URL
}

# Set PROXIES to the PROXIES dictionary if PROXY is True, otherwise set it to None
PROXIES = PROXIES if PROXY else None

# list methods of telegram api
METHODS = [
    'sendMessage',
    'editMessageText',
]
# create telegram api based on METHODS and API_ENDPOINT
API = {method: API_ENDPOINT + method for method in METHODS}
