from typing import Optional
from monogram.types import User, Message


class CallbackQuery:
    """
    This object represents an incoming callback query from a callback button in an inline keyboard.
    """

    def __init__(
        self,
        id: str,
        from_user: dict,
        message: dict = None,
        inline_message_id: Optional[str] = None,
        chat_instance: str = None,
        data: Optional[str] = None,
        game_short_name: Optional[str] = None,
    ):
        """
        Initialize a CallbackQuery object.

        :param id: Unique identifier for this query.
        :param from_user: The sender of the query.
        :param message: Optional. Message with the callback button that originated the query.
                        Note that message content and message date will not be available if the message is too old.
        :param inline_message_id: Optional. Identifier of the message sent via the bot in inline mode, that originated the query.
        :param chat_instance: Global identifier, uniquely corresponding to the chat to which the message with the callback button was sent.
                              Useful for high scores in games.
        :param data: Optional. Data associated with the callback button.
                     Be aware that the message originated the query can contain no callback buttons with this data.
        :param game_short_name: Optional. Short name of a Game to be returned, serves as the unique identifier for the game.
        """
        self.id = id
        self.from_user = User(**from_user)
        if message:
            message["from_user"] = message.pop("from")
            self.message = Message(**message)

        self.inline_message_id = inline_message_id
        self.chat_instance = chat_instance
        self.data = data
        self.game_short_name = game_short_name
