from typing import Optional
from .baseType import BaseType
from .WebAppInfo import WebAppInfo
from .LoginUrl import LoginUrl
from .SwitchInlineQueryChosenChat import SwitchInlineQueryChosenChat
from .CallbackGame import CallbackGame
from monogram.text import format_text

def _prepare_payload(raw_payload):
    """
    Prepares a payload dictionary for Telegram API requests.
    Removes None values and formats text/caption fields.

    Args:
        raw_payload: The dictionary of parameters for the API method.

    Returns:
        A cleaned and formatted payload dictionary.
    """
    if raw_payload:
        # Remove None values from payload
        payload = {k: v for k, v in raw_payload.items() if v is not None}

        if 'self' in payload:
            payload.pop('self')
        if 'cls' in payload:
            payload.pop('cls')
        if 'kwargs' in payload:
            payload.pop('kwargs')
        # Apply text formatting if 'text' or 'caption' keys exist
        if 'text' in payload and payload['text'] is not None:
            payload['text'] = format_text(payload['text'])
        if 'caption' in payload and payload['caption'] is not None:
            payload['caption'] = format_text(payload['caption'])
            
        return payload
    return {}

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
        
        payload = _prepare_payload(locals().copy())
        return payload
