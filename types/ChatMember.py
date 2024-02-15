from typing import Union
from .ChatMemberOwner import ChatMemberOwner


class ChatMember:
    """
    This class contains information about one member of a chat.
    """

    def __init__(
        self,
        user_id: int,
        status: Union[
            ChatMemberOwner,
            "ChatMemberAdministrator",
            "ChatMemberMember",
            "ChatMemberRestricted",
            "ChatMemberLeft",
            "ChatMemberBanned",
        ],
    ):
        """
        Initialize a ChatMember object.

        Args:
            user_id (int): The user ID of the chat member.
            status (Union[ChatMemberOwner, ChatMemberAdministrator, ChatMemberMember, ChatMemberRestricted, ChatMemberLeft, ChatMemberBanned]):
                The status of the chat member, which can be one of the following types:
                    - ChatMemberOwner: Represents a chat member with owner status.
                    - ChatMemberAdministrator: Represents a chat member with administrator status.
                    - ChatMemberMember: Represents a regular chat member.
                    - ChatMemberRestricted: Represents a restricted chat member.
                    - ChatMemberLeft: Represents a chat member who left the chat.
                    - ChatMemberBanned: Represents a chat member who was banned.
        """
        self.user_id = user_id
        self.status = status
