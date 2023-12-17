from typing import Union, Optional

def stop_poll(
    chat_id: Union[int, str],
    message_id: int,
    reply_markup: Optional[dict] = None
) -> dict:
    """
    Use this method to stop a poll which was sent by the bot.
    On success, the stopped Poll is returned.

    :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    :param message_id: Identifier of the original message with the poll
    :param reply_markup: A JSON-serialized object for a new message inline keyboard.
    :return: The stopped Poll.
    """
    # Your implementation here
    pass