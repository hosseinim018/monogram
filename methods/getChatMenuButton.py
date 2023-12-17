from typing import Optional
from monogram import Monogram, validate_payload

class getChatMenuButton(Monogram):
    def __new__(cls ,chat_id: Optional[int] = None) -> dict:
        """
        Use this method to get the current value of the bot's menu button in a private chat, or the default menu button.
        Returns MenuButton on success.

        :param chat_id: Unique identifier for the target private chat.
                        If not specified, the default bot's menu button will be returned.
        :return: The current value of the bot's menu button
        """
        payload = validate_payload(locals().copy())
        # send post request to telegram based on method sendMessage, Construct the API endpoint URL
        response = cls.request(cls, method='getChatMenuButton', data=payload, res=True)
        return response.json()