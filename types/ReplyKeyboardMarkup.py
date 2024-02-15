from typing import Optional, List
from .KeyboardButton import KeyboardButton
from monogram.core import validate_payload


class ReplyKeyboardMarkup:
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
