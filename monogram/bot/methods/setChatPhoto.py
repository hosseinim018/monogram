from typing import Union

def set_chat_photo(
    chat_id: Union[int, str],
    photo: "InputFile"
) -> bool:
    """
    Use this method to set a new profile photo for the chat.
    Photos can't be changed for private chats.
    The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights.
    Returns True on success.

    :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    :param photo: New chat photo, uploaded using multipart/form-data
    :return: True on success
    """
    # Your implementation here
    pass