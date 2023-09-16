from typing import List
from .Button import Inline


class Markup:
    def __init__(self):
        pass

    def Inline(self, inline_keyboard: List[List[dict]]) -> dict:
        """
        This mehtod represents an inline keyboard that appears right next to the message it belongs to.
        Initialize an InlineKeyboardMarkup object.

        :param inline_keyboard: The list of button rows in the inline keyboard.
        :return Markup: dict.
        """
        Markup = {
            'inline_keyboard': inline_keyboard
        }
        return Markup
