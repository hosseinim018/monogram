from typing import Optional
from .KeyboardButtonPollType import KeyboardButtonPollType
from .WebAppInfo import WebAppInfo
from .KeyboardButtonRequestUser import KeyboardButtonRequestUser
from .KeyboardButtonRequestChat import KeyboardButtonRequestChat
from monogram import validate_payload


class KeyboardButton:
    """
    This object represents one button of the reply keyboard.
    """

    def __new__(
        self,
        text: str,
        request_user: Optional[KeyboardButtonRequestUser] = None,
        request_chat: Optional[KeyboardButtonRequestChat] = None,
        request_contact: Optional[bool] = None,
        request_location: Optional[bool] = None,
        request_poll: Optional[KeyboardButtonPollType] = None,
        web_app: Optional[WebAppInfo] = None,
    ):
        """
        Initialize a KeyboardButton object.

        :param text: The label text on the button.
        :param request_user: Optional. The criteria used to request a user when the button is pressed.
        :param request_chat: Optional. The criteria used to request a chat when the button is pressed.
        :param request_contact: Optional. Boolean indicating if the user's contact information should be requested.
        :param request_location: Optional. Boolean indicating if the user's location should be requested.
        :param request_poll: Optional. The type of poll to be created when the button is pressed.
        :param web_app: Optional. Information about the web app to be opened when the button is pressed.
        """
        payload = validate_payload(locals().copy())
        return payload
