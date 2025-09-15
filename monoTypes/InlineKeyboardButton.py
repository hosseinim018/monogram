from typing import Optional
from .baseType import BaseType
from .WebAppInfo import WebAppInfo
from .LoginUrl import LoginUrl
from .SwitchInlineQueryChosenChat import SwitchInlineQueryChosenChat
from .CallbackGame import CallbackGame

def validate_payload(_locals):
    _locals = _locals  # Create a copy of locals()
    # Remove the key cls ir self from _locals
    if 'self' in _locals:
        _locals.pop('self')
    if 'cls' in _locals:
        _locals.pop('cls')
    payload = {k: v for k, v in _locals.items() if v}  # Remove None values from payload
    return payload

class InlineKeyboardButton(BaseType):
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
        **kwargs
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
