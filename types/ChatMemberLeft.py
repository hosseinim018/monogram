from .User import User


class ChatMemberLeft:
    """
    This class represents a chat member who is not currently a member of the chat but may join it themselves.
    """

    def __init__(self, status: str, user: User):
        """
        Initialize a ChatMemberLeft object.

        Args:
            status (str): The member's status in the chat. It is always "left" for a ChatMemberLeft.
            user (User): Information about the user who is not currently a member.
        """
        self.status = status
        self.user = user
