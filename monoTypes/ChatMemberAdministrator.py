from typing import Optional
from .User import User


class ChatMemberAdministrator:
    """
    This class represents a chat member that has some additional privileges.
    """

    def __init__(
        self,
        status: str,
        user: User,
        can_be_edited: bool,
        is_anonymous: bool,
        can_manage_chat: bool,
        can_delete_messages: bool,
        can_manage_video_chats: bool,
        can_restrict_members: bool,
        can_promote_members: bool,
        can_change_info: bool,
        can_invite_users: bool,
        can_post_messages: Optional[bool] = None,
        can_edit_messages: Optional[bool] = None,
        can_pin_messages: Optional[bool] = None,
        can_manage_topics: Optional[bool] = None,
        custom_title: Optional[str] = None,
    ):
        """
        Initialize a ChatMemberAdministrator object.

        Args:
            status (str): The member's status in the chat. It is always "administrator" for a ChatMemberAdministrator.
            user (User): Information about the user who is an administrator.
            can_be_edited (bool): True, if the bot is allowed to edit administrator privileges of that user.
            is_anonymous (bool): True, if the user's presence in the chat is hidden.
            can_manage_chat (bool): True, if the administrator has the privilege to manage the chat.
            can_delete_messages (bool): True, if the administrator can delete messages of other users.
            can_manage_video_chats (bool): True, if the administrator can manage video chats.
            can_restrict_members (bool): True, if the administrator can restrict, ban, or unban chat members.
            can_promote_members (bool): True, if the administrator can add new administrators or demote administrators.
            can_change_info (bool): True, if the user is allowed to change the chat title, photo, and other settings.
            can_invite_users (bool): True, if the user is allowed to invite new users to the chat.
            can_post_messages (bool, optional): True, if the administrator can post messages in the channel. This field is optional and applicable only for channels.
            can_edit_messages (bool, optional): True, if the administrator can edit messages of other users and pin messages. This field is optional and applicable only for channels.
            can_pin_messages (bool, optional): True, if the user is allowed to pin messages. This field is optional and applicable only for groups and supergroups.
            can_manage_topics (bool, optional): True, if the user is allowed to create, rename, close, and reopen forum topics. This field is optional and applicable only for supergroups.
            custom_title (str, optional): Custom title for this user. This field is optional.
        """
        self.status = status
        self.user = user
        self.can_be_edited = can_be_edited
        self.is_anonymous = is_anonymous
        self.can_manage_chat = can_manage_chat
        self.can_delete_messages = can_delete_messages
        self.can_manage_video_chats = can_manage_video_chats
        self.can_restrict_members = can_restrict_members
        self.can_promote_members = can_promote_members
        self.can_change_info = can_change_info
        self.can_invite_users = can_invite_users
        self.can_post_messages = can_post_messages
        self.can_edit_messages = can_edit_messages
        self.can_pin_messages = can_pin_messages
        self.can_manage_topics = can_manage_topics
        self.custom_title = custom_title
