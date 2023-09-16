from typing import Union

def set_chat_administrator_custom_title(
    chat_id: Union[int, str],
    user_id: int,
    custom_title: str,
) -> bool:
    """
    Use this method to set a custom title for an administrator in a supergroup promoted by the bot.
    Returns True on success.

    :param chat_id: Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
    :param user_id: Unique identifier of the target user
    :param custom_title: New custom title for the administrator; 0-16 characters, emoji are not allowed
    :return: True on success
    """
    # Your implementation here
    pass