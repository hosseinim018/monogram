from typing import Optional
from .User import User


class ChatInviteLink:
    """
    This class represents an invite link for a chat.
    """

    def __init__(
        self,
        invite_link: str,
        creator: "User",
        creates_join_request: bool,
        is_primary: bool,
        is_revoked: bool,
        name: Optional[str] = None,
        expire_date: Optional[int] = None,
        member_limit: Optional[int] = None,
        pending_join_request_count: Optional[int] = None,
    ):
        """
        Initialize a ChatInviteLink object.

        Args:
            invite_link (str): The invite link. If the link was created by another chat administrator,
                then the second part of the link will be replaced with “…”.
            creator (User): Creator of the link.
            creates_join_request (bool): True, if users joining the chat via the link need to be approved by chat administrators.
            is_primary (bool): True, if the link is primary.
            is_revoked (bool): True, if the link is revoked.
            name (str, optional): Invite link name. This field is optional.
            expire_date (int, optional): Point in time (Unix timestamp) when the link will expire or has been expired.
                This field is optional.
            member_limit (int, optional): The maximum number of users that can be members of the chat simultaneously
                after joining the chat via this invite link; 1-99999. This field is optional.
            pending_join_request_count (int, optional): Number of pending join requests created using this link.
                This field is optional.
        """
        self.invite_link = invite_link
        self.creator = creator
        self.creates_join_request = creates_join_request
        self.is_primary = is_primary
        self.is_revoked = is_revoked
        self.name = name
        self.expire_date = expire_date
        self.member_limit = member_limit
        self.pending_join_request_count = pending_join_request_count
