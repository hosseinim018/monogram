from typing import Union
from monogram import Monogram, validate_payload

class getChat(Monogram):
    def __new__(cls, chat_id: Union[int, str]) -> dict:
        """
        Use this method to get up-to-date information about the chat (current name of the user for one-on-one conversations,
        current username of a user, group or channel, etc.).
        Returns a Chat object on success.

        :param chat_id: Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername)
        :return: Chat object on success
        """
        payload = validate_payload(locals().copy())
        # send post request to telegram based on method sendMessage, Construct the API endpoint URL
        response = cls.request(cls, method='getChat', data=payload, res=True)
        return response.json()