from typing import Union
from monogram import Monogram, validate_payload

class unpinChatMessage(Monogram):
    def __new__(cls,
        chat_id: Union[int, str],
        message_id: int = None
    ) -> bool:
        """
        Use this method to remove a message from the list of pinned messages in a chat.
        If the chat is not a private chat, the bot must be an administrator in the chat for this to work and must have the
        'can_pin_messages' administrator right in a supergroup or 'can_edit_messages' administrator right in a channel.
        Returns True on success.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param message_id: Identifier of a message to unpin. If not specified, the most recent pinned message (by sending date) will be unpinned.
        :return: True on success
        """
        payload = validate_payload(locals().copy())
        # send post request to telegram based on method sendMessage, Construct the API endpoint URL
        response = cls.request(cls, method='unpinChatMessage', data=payload, res=True)
        return response.json()