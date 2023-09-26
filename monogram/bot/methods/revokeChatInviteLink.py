from typing import Union

def revoke_chat_invite_link(
    chat_id: Union[int, str],
    invite_link: str
) -> dict:
    """
    Use this method to revoke an invite link created by the bot.
    If the primary link is revoked, a new link is automatically generated.
    The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights.
    Returns the revoked invite link as a dictionary object.

    :param chat_id: Unique identifier of the target chat or username of the target channel (in the format @channelusername)
    :param invite_link: The invite link to revoke
    :return: The revoked invite link as a dictionary object
    """
    # Your implementation here
    pass