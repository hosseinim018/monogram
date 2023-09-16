class ChatAdministratorRights:
    """
    This class represents the rights of an administrator in a chat.
    """

    def __init__(
        self,
        is_anonymous: bool,
        can_manage_chat: bool,
        can_delete_messages: bool,
        can_manage_video_chats: bool,
        can_restrict_members: bool,
        can_promote_members: bool,
        can_change_info: bool,
        can_invite_users: bool,
        can_post_messages: bool = False,
        can_edit_messages: bool = False,
        can_pin_messages: bool = False,
        can_manage_topics: bool = False
    ):
        """
        Initialize a ChatAdministratorRights object.

        Args:
            is_anonymous (bool): True, if the user's presence in the chat is hidden.
            can_manage_chat (bool): True, if the administrator can access the chat event log,
                chat statistics, message statistics in channels, see channel members,
                see anonymous administrators in supergroups, and ignore slow mode.
                Implied by any other administrator privilege.
            can_delete_messages (bool): True, if the administrator can delete messages of other users.
            can_manage_video_chats (bool): True, if the administrator can manage video chats.
            can_restrict_members (bool): True, if the administrator can restrict, ban, or unban chat members.
            can_promote_members (bool): True, if the administrator can add new administrators with a subset
                of their own privileges or demote administrators that they have promoted, directly or indirectly
                (promoted by administrators that were appointed by the user).
            can_change_info (bool): True, if the user is allowed to change the chat title, photo, and other settings.
            can_invite_users (bool): True, if the user is allowed to invite new users to the chat.
            can_post_messages (bool, optional): True, if the administrator can post in the channel. This field is optional and applicable only to channels.
            can_edit_messages (bool, optional): True, if the administrator can edit messages of other users and can pin messages. This field is optional and applicable only to channels.
            can_pin_messages (bool, optional): True, if the user is allowed to pin messages. This field is optional and applicable only to groups and supergroups.
            can_manage_topics (bool, optional): True, if the user is allowed to create, rename, close, and reopen forum topics. This field is optional and applicable only to supergroups.
        """
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
