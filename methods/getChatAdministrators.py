from typing import Union
from monogram import Monogram, validate_payload

class getChatAdministrators(Monogram):
    def __new__(cls, chat_id: Union[int, str]) -> list:
        """
        Use this method to get a list of administrators in a chat, which aren't bots.
        Returns an array of ChatMember objects.

        :param chat_id: Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername)
        :return: Array of ChatMember objects
        """
        payload = validate_payload(locals().copy())
        # send post request to telegram based on method sendMessage, Construct the API endpoint URL
        response = cls.request(cls, method='getChatAdministrators', data=payload, res=True)
        return response.json()