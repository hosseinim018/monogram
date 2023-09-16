from typing import List
from .InlineKeyboardButton import InlineKeyboardButton


class InlineKeyboardMarkup:
    """
    This object represents an inline keyboard that appears right next to the message it belongs to.
    """
    def __new__(cls, inline_keyboard: List[List[InlineKeyboardButton]]) -> dict:
        """
        Initialize an InlineKeyboardMarkup object.

        :param inline_keyboard: The list of button rows in the inline keyboard.
        """

        markup = {
            'inline_keyboard': inline_keyboard
        }
        return markup
