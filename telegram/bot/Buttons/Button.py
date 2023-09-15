from typing import Optional

class Inline:
    """
    This object represents one button of an inline keyboard.
    """

    def __init__(self, text: str, pay: Optional[bool] = None):
        """
        Initialize an InlineKeyboardButton object.

        :param text: The label text on the button.
        :param pay: Optional. Boolean indicating if the button is for a payment.
        """
        self.text = text
        self.pay = pay


    def url(self, url: str) -> dict:
        """
        this mehtod initialize a inline url button
        :param url: str. The URL to open when the button is pressed.
        :return btn: dict.
        """
        btn = {
            'text': self.text,
            'url': url
        }
        return btn

    def callback_data(self, callback_data: str) -> dict:
        """
        this mehtod initialize a inline callback-data button
        :param callback_data: str. The callback data to be sent when the button is pressed.
        :return btn: dict.
        """
        btn = {
            'text': self.text,
            'callback_data': callback_data
        }
        return btn

    def web_app(self, url:str) -> dict:
        """
        this mehtod initialize a inline web app button
        :param url: str. Information about the web app to be opened when the button is pressed.
        :return btn: dict.
        """
        btn = {
            'text': self.text,
            'web_app': url
        }
        return btn

    def login_url(self, url: str) -> dict:
        """
        this mehtod initialize a inline login button
        :param url: str. The login URL to authenticate the user when the button is pressed.
        :return btn: dict.
        """
        btn = {
            'text': self.text,
            'login_url': url
        }
        return btn

    def switch_inline_query(self, query: str, current_chat: bool = False, chosen_chat: bool = False) -> dict:
        """
        :param query: Optional. The inline query string to be sent when the button is pressed.
        :param switch_inline_query_current_chat: Optional. The inline query string to be sent when the button is pressed in the current chat.
        :param switch_inline_query_chosen_chat: Optional. The inline query string to be sent when the button is pressed in a chosen chat.

        :return btn: dict
        """
        btn = {
            'text': self.text,
        }
        if current_chat:
            btn['switch_inline_query_current_chat'] = query
        elif chosen_chat:
            btn['switch_inline_query_chosen_chat'] = query
        else:
            btn['switch_inline_query'] = query

        return btn

    def callback_game(self, callback_game: str) -> dict:
        """
        this mehtod initialize a inline callback-data button
        :param callback_game: Optional. Information about the callback game to be played when the button is pressed.
        :return btn: dict.
        """
        btn = {
            'text': self.text,
            'callback_game': callback_game
        }
        return btn



