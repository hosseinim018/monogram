from .Chat import Chat
from .User import User
from .ChatInviteLink import ChatInviteLink


class ChatJoinRequest:
    """
    This class represents a join request sent to a chat.
    """

    def __init__(
        self,
        chat: Chat,
        from_user: User,
        user_chat_id: int,
        date: int,
        bio: str = None,
        invite_link: ChatInviteLink = None,
    ):
        """
        Initialize a ChatJoinRequest object.

        Args:
            chat (Chat): The chat to which the request was sent.
            from_user (User): The user that sent the join request.
            user_chat_id (int): Identifier of a private chat with the user who sent the join request. This number may
                have more than 32 significant bits, so a 64-bit integer or double-precision float type is safe for
                storing this identifier.
            date (int): The date the request was sent in Unix time.
            bio (str, optional): The bio of the user. Defaults to None.
            invite_link (ChatInviteLink, optional): The chat invite link that was used by the user to send the join
                request. Defaults to None.
        """
        self.chat = chat
        self.from_user = from_user
        self.user_chat_id = user_chat_id
        self.date = date
        self.bio = bio
        self.invite_link = invite_link
