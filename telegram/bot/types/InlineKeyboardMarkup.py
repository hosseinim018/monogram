from typing import List
from .InlineKeyboardButton import InlineKeyboardButton


class InlineKeyboardMarkup:
    """
    This object represents an inline keyboard that appears right next to the message it belongs to.
    """
    def __init__(self, inline_keyboard: List[List[InlineKeyboardButton]]):
        """
        Initialize an InlineKeyboardMarkup object.

        :param inline_keyboard: The list of button rows in the inline keyboard.
        """
        self.inline_keyboard = inline_keyboard

    def call(self) -> dict:
        markup = {
            'inline_keyboard': self.inline_keyboard
        }
        return markup
