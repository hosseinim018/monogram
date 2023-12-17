from typing import Optional
from monogram import Monogram, validate_payload

class setChatMenuButton(Monogram):
    def __new__(cls, chat_id: Optional[int] = None, menu_button: Optional[dict] = None) -> bool:
        """
        Use this method to change the bot's menu button in a private chat, or the default menu button.
        Returns True on success.

        :param chat_id: Unique identifier for the target private chat.
                        If not specified, the default bot's menu button will be changed.
        :param menu_button: A JSON-serialized object for the bot's new menu button.
                            Defaults to MenuButtonDefault.
        :return: True on success
        """
        payload = validate_payload(locals().copy())
        # send post request to telegram based on method sendMessage, Construct the API endpoint URL
        response = cls.request(cls, method='setChatMenuButton', data=payload, res=True)
        return response.json()