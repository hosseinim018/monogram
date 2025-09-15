from typing import Optional, List
from .User import User
from .Chat import Chat


class PollAnswer:
    """
    This class represents an answer of a user in a non-anonymous poll.
    """

    def __init__(
        self,
        poll_id: str,
        voter_chat: Optional[Chat] = None,
        user: Optional[User] = None,
        option_ids: List[int] = [],
    ):
        """
        Initialize a PollAnswer object.

        Args:
            poll_id (str): Unique poll identifier.
            voter_chat (Chat, optional): The chat that changed the answer to the poll, if the voter is anonymous.
            user (User, optional): The user that changed the answer to the poll, if the voter isn't anonymous.
            option_ids (List[int], optional): 0-based identifiers of chosen answer options. May be empty if the vote was retracted.
        """
        self.poll_id = poll_id
        self.voter_chat = voter_chat
        self.user = user
        self.option_ids = option_ids
