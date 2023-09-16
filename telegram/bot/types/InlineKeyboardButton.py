from typing import Optional
from telegram.bot.core import validate_parameters

from telegram.bot.types import *

class InlineKeyboardButton:
    """
        This object represents one button of an inline keyboard.
        """

    def __new__(self, text: str, url: Optional[str] = None, callback_data: Optional[str] = None,
                web_app: Optional[WebAppInfo] = None, login_url: Optional[LoginUrl] = None,
                switch_inline_query: Optional[str] = None, switch_inline_query_current_chat: Optional[str] = None,
                switch_inline_query_chosen_chat: Optional[SwitchInlineQueryChosenChat] = None,
                callback_game: Optional[CallbackGame] = None, pay: Optional[bool] = None):
        """
            Initialize an InlineKeyboardButton object.

            :param text: The label text on the button.
            :param url: Optional. The URL to open when the button is pressed.
            :param callback_data: Optional. The callback data to be sent when the button is pressed.
            :param web_app: Optional. Information about the web app to be opened when the button is pressed.
            :param login_url: Optional. The login URL to authenticate the user when the button is pressed.
            :param switch_inline_query: Optional. The inline query string to be sent when the button is pressed.
            :param switch_inline_query_current_chat: Optional. The inline query string to be sent when the button is pressed in the current chat.
            :param switch_inline_query_chosen_chat: Optional. The inline query string to be sent when the button is pressed in a chosen chat.
            :param callback_game: Optional. Information about the callback game to be played when the button is pressed.
            :param pay: Optional. Boolean indicating if the button is for a payment.
            """
        self.text = text
        self.url = url
        self.callback_data = callback_data
        self.web_app = web_app
        self.login_url = login_url
        self.switch_inline_query = switch_inline_query
        self.switch_inline_query_current_chat = switch_inline_query_current_chat
        self.switch_inline_query_chosen_chat = switch_inline_query_chosen_chat
        self.callback_game = callback_game
        self.pay = pay

        payload = {
            'text': text
        }
        if url:
            payload['url'] = url
        if callback_data:
            payload['callback_data'] = callback_data
        if web_app:
            payload['web_app'] = web_app
        if login_url:
            payload['login_url'] = login_url
        if switch_inline_query:
            payload['switch_inline_query'] = switch_inline_query
        if switch_inline_query_current_chat:
            payload['switch_inline_query_current_chat'] = switch_inline_query_current_chat
        if switch_inline_query_chosen_chat:
            payload['switch_inline_query_chosen_chat'] = switch_inline_query_chosen_chat
        if callback_game:
            payload['callback_game'] = callback_game
        if pay:
            payload['pay'] = pay
