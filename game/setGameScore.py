from typing import Union

def setGameScore(
    user_id: int,
    score: int,
    force: bool = None,
    disable_edit_message: bool = None,
    chat_id: int = None,
    message_id: int = None,
    inline_message_id: str = None
) -> Union[bool, Message]:
    """
    Use this method to set the score of the specified user in a game message.

    On success, if the message is not an inline message, the Message is returned, otherwise True is returned.
    Returns an error if the new score is not greater than the user's current score in the chat and force is False.

    :param user_id: The identifier of the user for whom the score is being set.
    :param score: The new score to be set. Must be a non-negative value.
    :param force: Optional. Pass True if the high score is allowed to decrease. This can be useful when fixing mistakes or banning cheaters.
    :param disable_edit_message: Optional. Pass True if the game message should not be automatically edited to include the current scoreboard.
    :param chat_id: Optional. Required if inline_message_id is not specified. Unique identifier for the target chat.
    :param message_id: Optional. Required if inline_message_id is not specified. Identifier of the sent message.
    :param inline_message_id: Optional. Required if chat_id and message_id are not specified. Identifier of the inline message.

    :return: If the message is not an inline message, returns the Message object. If the message is an inline message, returns True.
             Returns an error if the new score is not greater than the user's current score in the chat and force is False.
    """
    pass