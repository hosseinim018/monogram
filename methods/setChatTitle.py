from typing import Union
from monogram import Monogram, validate_payload

class setChatTitle(Monogram):
    def __new__(cls,
        chat_id: Union[int, str],
        title: str
    ) -> bool:
        """
        Use this method to change the title of a chat.
        Titles can't be changed for private chats.
        The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights.
        Returns True on success.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param title: New chat title, 1-128 characters
        :return: True on success
        """
        payload = validate_payload(locals().copy())
        # send post request to telegram based on method sendMessage, Construct the API endpoint URL
        response = cls.request(cls, method='setChatTitle', data=payload, res=True)
        return response.json()