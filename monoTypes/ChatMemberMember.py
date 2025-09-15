from .User import User


class ChatMemberMember:
    """
    This class represents a chat member with no additional privileges or restrictions.
    """

    def __init__(self, status: str, user: User):
        """
        Initialize a ChatMemberMember object.

        Args:
            status (str): The member's status in the chat. It is always "member" for a ChatMemberMember.
            user (User): Information about the user who is a member.
        """
        self.status = status
        self.user = user
