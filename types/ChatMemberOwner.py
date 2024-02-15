from typing import Optional
from .User import User


class ChatMemberOwner:
    """
    This class represents a chat member that owns the chat and has all administrator privileges.
    """

    def __init__(
        self,
        status: str,
        user: User,
        is_anonymous: bool,
        custom_title: Optional[str] = None,
    ):
        """
        Initialize a ChatMemberOwner object.

        Args:
            status (str): The member's status in the chat. It is always "creator" for a ChatMemberOwner.
            user (User): Information about the user who owns the chat.
            is_anonymous (bool): True, if the user's presence in the chat is hidden.
            custom_title (str, optional): Custom title for this user. This field is optional.
        """
        self.status = status
        self.user = user
        self.is_anonymous = is_anonymous
        self.custom_title = custom_title


class User:
    """
    This class represents information about a user.
    """

    def __init__(self, user_id: int, username: str):
        """
        Initialize a User object.

        Args:
            user_id (int): The unique identifier of the user.
            username (str): The username of the user.
        """
        self.user_id = user_id
        self.username = username
