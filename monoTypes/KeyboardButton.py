from typing import Optional
from .KeyboardButtonPollType import KeyboardButtonPollType
from .WebAppInfo import WebAppInfo
from .KeyboardButtonRequestUser import KeyboardButtonRequestUser
from .KeyboardButtonRequestChat import KeyboardButtonRequestChat
from .baseType import BaseType

def validate_payload(_locals):
    _locals = _locals  # Create a copy of locals()
    # Remove the key cls ir self from _locals
    if 'self' in _locals:
        _locals.pop('self')
    if 'cls' in _locals:
        _locals.pop('cls')
    payload = {k: v for k, v in _locals.items() if v}  # Remove None values from payload
    return payload
    
class KeyboardButton(BaseType):
    """
    This object represents one button of the reply keyboard.
    """

    def __new__(
        cls,
        text: str,
        request_user: Optional["KeyboardButtonRequestUser"] = None,
        request_chat: Optional["KeyboardButtonRequestChat"] = None,
        request_contact: Optional[bool] = None,
        request_location: Optional[bool] = None,
        request_poll: Optional["KeyboardButtonPollType"] = None,
        web_app: Optional["WebAppInfo"] = None,
        *args,
        **kwargs
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
        # kwargs['text'] = text
        # instance = super(KeyboardButton, cls).__new__(cls)
        # instance.__init__(*args, **kwargs)
        # return instance.__dict__
