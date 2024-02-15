from typing import Union
from monogram import Monogram, validate_payload


class banChatSenderChat(Monogram):
    def __new__(cls, chat_id: Union[int, str], sender_chat_id: int) -> bool:
        """
        Use this method to ban a channel chat in a supergroup or a channel.
        Until the chat is unbanned, the owner of the banned chat won't be able to send messages on behalf of any of their channels.
        The bot must be an administrator in the supergroup or channel for this to work and must have the appropriate administrator rights.
        Returns True on success.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param sender_chat_id: Unique identifier of the target sender chat
        :return: True on success
        """
        payload = validate_payload(locals().copy())
        # send post request to telegram based on method sendMessage, Construct the API endpoint URL
        response = cls.request(cls, method="sendVideo", data=payload, res=True)
        return response.json()
