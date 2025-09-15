from typing import Optional
from . import User, Message
from .baseType import BaseType

class CallbackQuery(BaseType):
    """
    This object represents an incoming callback query from a callback button in an inline keyboard.
    """

    def __init__(
        self,
        bot,
        *args,
        **kwargs
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
        super().__init__(**kwargs)
        self.bot = bot
        self.from_user = User(**self.from_user)

    def answerCallbackQuery(self):
        self.bot.answerCallbackQuery(self.id)
