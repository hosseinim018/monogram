from typing import Union, Optional, List
from .Message import Message
from .GameHighScore import GameHighScore
from .InlineKeyboardMarkup import InlineKeyboardMarkup
from .ReplyParameters import ReplyParameters

class GameMethods:
    """
    This class contains methods for handling Telegram game-related operations.
    """

    @staticmethod
    def send_game(
        chat_id: int,
        game_short_name: str,
        business_connection_id: Optional[str] = None,
        message_thread_id: Optional[int] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        allow_paid_broadcast: Optional[bool] = None,
        message_effect_id: Optional[str] = None,
        reply_parameters: Optional[ReplyParameters] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None
    ) -> Message:
        """
        Send a game to a chat.

        Args:
            chat_id: Unique identifier for the target chat
            game_short_name: Short name of the game
            business_connection_id: Optional. Business connection identifier
            message_thread_id: Optional. Message thread identifier
            disable_notification: Optional. Send silently
            protect_content: Optional. Protect content from forwarding
            allow_paid_broadcast: Optional. Allow paid broadcasting
            message_effect_id: Optional. Message effect identifier
            reply_parameters: Optional. Reply parameters
            reply_markup: Optional. Inline keyboard markup

        Returns:
            Message: The sent message
        """
        return Message()  # Implementation will be done in network layer

    @staticmethod
    def set_game_score(
        user_id: int,
        score: int,
        force: Optional[bool] = None,
        disable_edit_message: Optional[bool] = None,
        chat_id: Optional[int] = None,
        message_id: Optional[int] = None,
        inline_message_id: Optional[str] = None
    ) -> Union[Message, bool]:
        """
        Set the score of the specified user in a game.

        Args:
            user_id: User identifier
            score: New score (non-negative)
            force: Optional. Allow score to decrease
            disable_edit_message: Optional. Don't edit message
            chat_id: Optional. Chat identifier
            message_id: Optional. Message identifier
            inline_message_id: Optional. Inline message identifier

        Returns:
            Union[Message, bool]: Message object for regular messages, True for inline messages
        """
        return True  # Implementation will be done in network layer

    @staticmethod
    def get_game_high_scores(
        user_id: int,
        chat_id: Optional[int] = None,
        message_id: Optional[int] = None,
        inline_message_id: Optional[str] = None
    ) -> List[GameHighScore]:
        """
        Get data for high score tables.

        Args:
            user_id: Target user identifier
            chat_id: Optional. Chat identifier
            message_id: Optional. Message identifier
            inline_message_id: Optional. Inline message identifier

        Returns:
            List[GameHighScore]: List of high scores
        """
        return []  # Implementation will be done in network layer
