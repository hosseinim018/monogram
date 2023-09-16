from typing import Union

def set_chat_title(
    chat_id: Union[int, str],
    title: str
) -> bool:
    """
    Use this method to change the title of a chat.
    Titles can't be changed for private chats.
    The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights.
    Returns True on success.

    :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    :param title: New chat title, 1-128 characters
    :return: True on success
    """
    # Your implementation here
    pass