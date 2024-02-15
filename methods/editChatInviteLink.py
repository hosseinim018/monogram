from typing import Union
from monogram import Monogram, validate_payload


class editChatInviteLink(Monogram):
    def __new__(
        cls,
        chat_id: Union[int, str],
        invite_link: str,
        name: str = None,
        expire_date: int = None,
        member_limit: int = None,
        creates_join_request: bool = False,
    ) -> dict:
        """
        Use this method to edit a non-primary invite link created by the bot.
        The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights.
        Returns the edited invite link as a dictionary object.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param invite_link: The invite link to edit
        :param name: Invite link name; 0-32 characters (optional)
        :param expire_date: Point in time (Unix timestamp) when the link will expire (optional)
        :param member_limit: The maximum number of users that can be members of the chat simultaneously
                             after joining the chat via this invite link; 1-99999 (optional)
        :param creates_join_request: True, if users joining the chat via the link need to be approved by chat administrators.
                                     If True, member_limit can't be specified (optional)
        :return: The edited invite link as a dictionary object
        """
        payload = validate_payload(locals().copy())
        # send post request to telegram based on method sendMessage, Construct the API endpoint URL
        response = cls.request(cls, method="editChatInviteLink", data=payload, res=True)
        return response.json()
