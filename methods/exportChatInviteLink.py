from typing import Union

from monogram import Monogram, validate_payload


class exportChatInviteLink(Monogram):
    def __new__(cls, chat_id: Union[int, str]) -> str:
        """
        Use this method to generate a new primary invite link for a chat; any previously generated primary link is revoked.
        The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights.
        Returns the new invite link as a string on success.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :return: The new invite link as a string
        """
        payload = validate_payload(locals().copy())
        # send post request to telegram based on method sendMessage, Construct the API endpoint URL
        response = cls.request(
            cls, method="exportChatInviteLink", data=payload, res=True
        )
        return response.json()
