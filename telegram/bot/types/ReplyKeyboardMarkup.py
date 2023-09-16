from typing import Optional, List
from .KeyboardButton import KeyboardButton
from telegram.bot.core import validate_parameters


class ReplyKeyboardMarkup:
    """
    This object represents a custom keyboard with reply options.
    """

    @validate_parameters
    def __new__(self, keyboard: List[List[KeyboardButton]], payload, is_persistent: Optional[bool] = False,
                 resize_keyboard: Optional[bool] = False, one_time_keyboard: Optional[bool] = False,
                 input_field_placeholder: Optional[str] = None, selective: Optional[bool] = None):
        """
        Initialize a ReplyKeyboardMarkup object.

        :param keyboard: The list of button rows in the keyboard.
        :param is_persistent: Optional. Boolean indicating if the keyboard is persistent.
        :param resize_keyboard: Optional. Boolean indicating if the keyboard should be resized.
        :param one_time_keyboard: Optional. Boolean indicating if the keyboard should be shown only once.
        :param input_field_placeholder: Optional. The placeholder text to display in the input field.
        :param selective: Optional. Boolean indicating if the keyboard should be selective.
        """
        # self.keyboard = keyboard
        # self.is_persistent = is_persistent
        # self.resize_keyboard = resize_keyboard
        # self.one_time_keyboard = one_time_keyboard
        # self.input_field_placeholder = input_field_placeholder
        # self.selective = selective
        self.data = payload
        return payload