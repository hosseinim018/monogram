from typing import List
from .User import User


class VideoChatParticipantsInvited:
    """
    This class represents a service message about new members invited to a video chat.
    """

    def __init__(self, users: List[User]):
        """
        Initialize a VideoChatParticipantsInvited object.

        Args:
            users (List[User]): New members that were invited to the video chat.
        """
        self.users = users
