from typing import Union
from monogram import Monogram, validate_payload

class unbanChatSenderChat(Monogram):
    def __new__(cls,
        chat_id: Union[int, str],
        sender_chat_id: int
    ) -> bool:
        """
        Use this method to unban a previously banned channel chat in a supergroup or channel.
        The bot must be an administrator for this to work and must have the appropriate administrator rights.
        Returns True on success.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param sender_chat_id: Unique identifier of the target sender chat
        :return: True on success
        """
        payload = validate_payload(locals().copy())
        # send post request to telegram based on method sendMessage, Construct the API endpoint URL
        response = cls.request(cls, method='unbanChatSenderChat', data=payload, res=True)
        return response.json()