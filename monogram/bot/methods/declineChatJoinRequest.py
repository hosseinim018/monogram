from typing import Union

def decline_chat_join_request(
    chat_id: Union[int, str],
    user_id: int
) -> bool:
    """
    Use this method to decline a chat join request.
    The bot must be an administrator in the chat for this to work and must have the can_invite_users administrator right.
    Returns True on success.

    :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    :param user_id: Unique identifier of the target user
    :return: True on success
    """
    # Your implementation here
    pass