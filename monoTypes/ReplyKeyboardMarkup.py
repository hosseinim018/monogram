from typing import Optional, List
from .KeyboardButton import KeyboardButton
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

class ReplyKeyboardMarkup(BaseType):
    """
    This object represents a custom keyboard with reply options.
    """

    def __new__(
        cls,
        keyboard: List[List[KeyboardButton]],
        is_persistent: Optional[bool] = False,
        resize_keyboard: Optional[bool] = False,
        one_time_keyboard: Optional[bool] = False,
        input_field_placeholder: Optional[str] = None,
        selective: Optional[bool] = None,
        *args,
        **kwargs
    ):
        """
        Initialize a ReplyKeyboardMarkup object.

        :param keyboard: The list of button rows in the keyboard.
        :param is_persistent: Optional. Boolean indicating if the keyboard is persistent.
        :param resize_keyboard: Optional. Boolean indicating if the keyboard should be resized.
        :param one_time_keyboard: Optional. Boolean indicating if the keyboard should be shown only once.
        :param input_field_placeholder: Optional. The placeholder text to display in the input field.
        :param selective: Optional. Boolean indicating if the keyboard should be selective.
        """
        payload = validate_payload(locals().copy())
        return payload
        # kwargs['keyboard'] = keyboard
        # instance = super(ReplyKeyboardMarkup, cls).__new__(cls)
        # instance.__init__(*args, **kwargs)
        # return instance.__dict__
