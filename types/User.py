from typing import Optional


class User:
    """Represents a Telegram user or bot."""

    def __init__(
            self,
            id: int,
            is_bot: bool,
            first_name: str,
            last_name: Optional[str] = None,
            username: Optional[str] = None,
            language_code: Optional[str] = None,
            is_premium: Optional[bool] = None,
            added_to_attachment_menu: Optional[bool] = None,
            can_join_groups: Optional[bool] = None,
            can_read_all_group_messages: Optional[bool] = None,
            supports_inline_queries: Optional[bool] = None
    ):
        """
        Initialize the User object.

        Args:
            id (int): Unique identifier for this user or bot.
            is_bot (bool): True, if this user is a bot.
            first_name (str): User's or bot's first name.
            last_name (str, optional): User's or bot's last name.
            username (str, optional): User's or bot's username.
            language_code (str, optional): IETF language tag of the user's language.
            is_premium (bool, optional): True, if this user is a Telegram Premium user.
            added_to_attachment_menu (bool, optional): True, if this user added the bot to the attachment menu.
            can_join_groups (bool, optional): True, if the bot can be invited to groups. Returned only in getMe.
            can_read_all_group_messages (bool, optional): True, if privacy mode is disabled for the bot. Returned only in getMe.
            supports_inline_queries (bool, optional): True, if the bot supports inline queries. Returned only in getMe.
        """
        self.id = id
        self.is_bot = is_bot
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.language_code = language_code
        self.is_premium = is_premium
        self.added_to_attachment_menu = added_to_attachment_menu
        self.can_join_groups = can_join_groups
        self.can_read_all_group_messages = can_read_all_group_messages
        self.supports_inline_queries = supports_inline_queries

        payload = {
            'id': self.id,
            'is_bot': self.is_bot,
            'first_name': self.first_name
        }

        if self.last_name is not None:
            payload['last_name'] = self.last_name
        if self.username is not None:
            payload['username'] = self.username
        if self.language_code is not None:
            payload['language_code'] = self.language_code
        if self.is_premium is not None:
            payload['is_premium'] = self.is_premium
        if self.added_to_attachment_menu is not None:
            payload['added_to_attachment_menu'] = self.added_to_attachment_menu
        if self.can_join_groups is not None:
            payload['can_join_groups'] = self.can_join_groups
        if self.can_read_all_group_messages is not None:
            payload['can_read_all_group_messages'] = self.can_read_all_group_messages
        if self.supports_inline_queries is not None:
            payload['supports_inline_queries'] = self.supports_inline_queries


