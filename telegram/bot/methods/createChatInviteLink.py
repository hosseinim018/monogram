from typing import Union

def create_chat_invite_link(
    chat_id: Union[int, str],
    name: str = None,
    expire_date: int = None,
    member_limit: int = None,
    creates_join_request: bool = False
) -> dict:
    """
    Use this method to create an additional invite link for a chat.
    The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights.
    The link can be revoked using the method revokeChatInviteLink.
    Returns the new invite link as a dictionary object.

    :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    :param name: Invite link name; 0-32 characters (optional)
    :param expire_date: Point in time (Unix timestamp) when the link will expire (optional)
    :param member_limit: The maximum number of users that can be members of the chat simultaneously
                         after joining the chat via this invite link; 1-99999 (optional)
    :param creates_join_request: True, if users joining the chat via the link need to be approved by chat administrators.
                                 If True, member_limit can't be specified (optional)
    :return: The new invite link as a dictionary object
    """
    # Your implementation here
    pass