from typing import Union

def pin_chat_message(
    chat_id: Union[int, str],
    message_id: int,
    disable_notification: bool = False
) -> bool:
    """
    Use this method to add a message to the list of pinned messages in a chat.
    If the chat is not a private chat, the bot must be an administrator in the chat for this to work and must have the
    'can_pin_messages' administrator right in a supergroup or 'can_edit_messages' administrator right in a channel.
    Returns True on success.

    :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    :param message_id: Identifier of a message to pin
    :param disable_notification: Pass True if it is not necessary to send a notification to all chat members about the new pinned message.
                                 Notifications are always disabled in channels and private chats.
    :return: True on success
    """
    # Your implementation here
    pass