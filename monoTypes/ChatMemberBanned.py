from .User import User


class ChatMemberBanned:
    """
    This class represents a chat member who was banned in the chat and can't return or view chat messages.
    """

    def __init__(self, status: str, user: User, until_date: int):
        """
        Initialize a ChatMemberBanned object.

        Args:
            status (str): The member's status in the chat. It is always "kicked" for a ChatMemberBanned.
            user (User): Information about the user who was banned.
            until_date (int): Date when restrictions will be lifted for this user, in Unix time. If 0, the user is
                banned forever.
        """
        self.status = status
        self.user = user
        self.until_date = until_date
