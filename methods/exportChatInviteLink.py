from typing import Union

def export_chat_invite_link(
    chat_id: Union[int, str]
) -> str:
    """
    Use this method to generate a new primary invite link for a chat; any previously generated primary link is revoked.
    The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights.
    Returns the new invite link as a string on success.

    :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    :return: The new invite link as a string
    """
    # Your implementation here
    pass