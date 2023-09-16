from typing import List

class GameHighScore:
    def __init__(self, position: int, user_id: int, score: int):
        """
        Represents a user's high score in a game.

        :param position: The position of the user in the high score table
        :param user_id: The identifier of the user
        :param score: The score achieved by the user
        """
        self.position = position
        self.user_id = user_id
        self.score = score

def getGameHighScores(
    user_id: int,
    chat_id: int = None,
    message_id: int = None,
    inline_message_id: str = None
) -> List[GameHighScore]:
    """
    Use this method to get data for high score tables.

    Returns the score of the specified user and several of their neighbors in a game.
    Returns an Array of GameHighScore objects.

    This method will currently return scores for the target user, plus two of their closest neighbors on each side.
    It will also return the top three users if the user and their neighbors are not among them.
    Please note that this behavior is subject to change.

    :param user_id: The target user id
    :param chat_id: Optional. Required if inline_message_id is not specified. Unique identifier for the target chat.
    :param message_id: Optional. Required if inline_message_id is not specified. Identifier of the sent message.
    :param inline_message_id: Optional. Required if chat_id and message_id are not specified. Identifier of the inline message.

    :return: An array of GameHighScore objects representing the high scores.
    """
    pass