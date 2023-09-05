from typing import Optional, Union

def stop_message_live_location(
    chat_id: Optional[Union[int, str]] = None,
    message_id: Optional[int] = None,
    inline_message_id: Optional[str] = None,
    reply_markup: Optional[dict] = None,
) -> Union[bool, dict]:
    """
    Use this method to stop updating a live location message before live_period expires.
    On success, if the message is not an inline message, the edited Message is returned, otherwise True is returned.

    :param chat_id: Required if inline_message_id is not specified.
                    Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    :param message_id: Required if inline_message_id is not specified.
                       Identifier of the message with live location to stop
    :param inline_message_id: Required if chat_id and message_id are not specified.
                              Identifier of the inline message
    :param reply_markup: A JSON-serialized object for a new inline keyboard.
    :return: If the message is not an inline message, the edited Message is returned,
             otherwise True is returned.
    """
    # Your implementation here
    pass