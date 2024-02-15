from typing import Union
from monogram import Monogram, validate_payload


class declineChatJoinRequest(Monogram):
    def __new__(cls, chat_id: Union[int, str], user_id: int) -> bool:
        """
        Use this method to decline a chat join request.
        The bot must be an administrator in the chat for this to work and must have the can_invite_users administrator right.
        Returns True on success.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param user_id: Unique identifier of the target user
        :return: True on success
        """
        payload = validate_payload(locals().copy())
        # send post request to telegram based on method sendMessage, Construct the API endpoint URL
        response = cls.request(
            cls, method="declineChatJoinRequest", data=payload, res=True
        )
        return response.json()
