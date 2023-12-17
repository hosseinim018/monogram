from typing import Union, Optional
from monogram import Monogram, validate_payload

class unbanChatMember(Monogram):
    def __new__(cls,
        chat_id: Union[int, str],
        user_id: int,
        only_if_banned: Optional[bool] = False
    ) -> bool:
        """
        Use this method to unban a previously banned user in a supergroup or channel.
        The user will not return to the group or channel automatically, but will be able to join via link, etc.
        The bot must be an administrator for this to work.
        By default, this method guarantees that after the call the user is not a member of the chat, but will be able to join it.
        So if the user is a member of the chat they will also be removed from the chat.
        If you don't want this, use the parameter only_if_banned.
        Returns True on success.

        :param chat_id: Unique identifier for the target group or username of the target supergroup or channel (in the format @channelusername)
        :param user_id: Unique identifier of the target user
        :param only_if_banned: Do nothing if the user is not banned
        :return: True on success
        """
        payload = validate_payload(locals().copy())
        # send post request to telegram based on method sendMessage, Construct the API endpoint URL
        response = cls.request(cls, method='unbanChatMember', data=payload, res=True)
        return response.json()