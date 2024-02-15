from typing import Union, Optional
from monogram import Monogram, validate_payload


class banChatMember(Monogram):
    def __new__(
        cls,
        chat_id: Union[int, str],
        user_id: int,
        until_date: Optional[int] = None,
        revoke_messages: Optional[bool] = False,
    ) -> bool:
        """
        Use this method to ban a user in a group, a supergroup, or a channel.
        In the case of supergroups and channels, the user will not be able to return to the chat on their own using invite links, etc., unless unbanned first.
        The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights.
        Returns True on success.

        :param chat_id: Unique identifier for the target group or username of the target supergroup or channel (in the format @channelusername)
        :param user_id: Unique identifier of the target user
        :param until_date: Date when the user will be unbanned; Unix time.
                           If the user is banned for more than 366 days or less than 30 seconds from the current time,
                           they are considered to be banned forever. Applied for supergroups and channels only.
        :param revoke_messages: Pass True to delete all messages from the chat for the user that is being removed.
                                If False, the user will be able to see messages in the group that were sent before the user was removed.
                                Always True for supergroups and channels.
        :return: True on success
        """
        # Your implementation here
        payload = validate_payload(locals().copy())
        # send post request to telegram based on method sendMessage, Construct the API endpoint URL
        response = cls.request(cls, method="banChatMember", data=payload, res=True)
        return response.json()
