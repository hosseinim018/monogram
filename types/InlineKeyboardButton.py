from typing import Optional
from monogram import validate_payload
from .WebAppInfo import WebAppInfo
from .LoginUrl import LoginUrl
from .SwitchInlineQueryChosenChat import SwitchInlineQueryChosenChat


class CallbackGame:
    pass


class InlineKeyboardButton:
    """
        This object represents one button of an inline keyboard.
        """

    def __new__(
        cls,
        text: str,
        url: Optional[str] = None,
        callback_data: Optional[str] = None,
        web_app: Optional[WebAppInfo] = None,
        login_url: Optional[LoginUrl] = None,
        switch_inline_query: Optional[str] = None,
        switch_inline_query_current_chat: Optional[str] = None,
        switch_inline_query_chosen_chat: Optional[SwitchInlineQueryChosenChat] = None,
        callback_game: Optional[CallbackGame] = None,
        pay: Optional[bool] = None,
    ) -> dict:
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
        payload = validate_payload(locals().copy())
        return payload
