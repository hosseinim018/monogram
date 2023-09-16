from typing import Optional, Union

def send_game(
    chat_id: int,
    game_short_name: str,
    message_thread_id: Optional[int] = None,
    disable_notification: Optional[bool] = None,
    protect_content: Optional[bool] = None,
    reply_to_message_id: Optional[int] = None,
    allow_sending_without_reply: Optional[bool] = None,
    reply_markup: Optional[dict] = None
) -> dict:
    """
    Use this method to send a game.
    On success, the sent Message is returned.

    :param chat_id: Unique identifier for the target chat
    :param game_short_name: Short name of the game, serves as the unique identifier for the game.
                            Set up your games via @BotFather.
    :param message_thread_id: Unique identifier for the target message thread (topic) of the forum; for forum supergroups only
    :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
    :param protect_content: Protects the contents of the sent message from forwarding and saving
    :param reply_to_message_id: If the message is a reply, ID of the original message
    :param allow_sending_without_reply: Pass True if the message should be sent even if the specified replied-to message is not found
    :param reply_markup: A JSON-serialized object for an inline keyboard.
                         If empty, one 'Play game_title' button will be shown.
                         If not empty, the first button must launch the game.
    :return: The sent Message.
    """
    # Your implementation here
    pass