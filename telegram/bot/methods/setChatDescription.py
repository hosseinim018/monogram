from typing import Union

def set_chat_description(
    chat_id: Union[int, str],
    description: str
) -> bool:
    """
    Use this method to change the description of a group, a supergroup, or a channel.
    The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights.
    Returns True on success.

    :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    :param description: New chat description, 0-255 characters
    :return: True on success
    """
    # Your implementation here
    pass