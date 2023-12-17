class ChatPermissions:
    """
    This class describes the actions that a non-administrator user is allowed to take in a chat.
    """

    def __init__(
        self,
        can_send_messages: bool = None,
        can_send_audios: bool = None,
        can_send_documents: bool = None,
        can_send_photos: bool = None,
        can_send_videos: bool = None,
        can_send_video_notes: bool = None,
        can_send_voice_notes: bool = None,
        can_send_polls: bool = None,
        can_send_other_messages: bool = None,
        can_add_web_page_previews: bool = None,
        can_change_info: bool = None,
        can_invite_users: bool = None,
        can_pin_messages: bool = None,
        can_manage_topics: bool = None,
    ):
        """
        Initialize a ChatPermissions object.

        Args:
            can_send_messages (bool, optional): True, if the user is allowed to send text messages, contacts,
                invoices, locations, and venues. Defaults to None.
            can_send_audios (bool, optional): True, if the user is allowed to send audios. Defaults to None.
            can_send_documents (bool, optional): True, if the user is allowed to send documents. Defaults to None.
            can_send_photos (bool, optional): True, if the user is allowed to send photos. Defaults to None.
            can_send_videos (bool, optional): True, if the user is allowed to send videos. Defaults to None.
            can_send_video_notes (bool, optional): True, if the user is allowed to send video notes. Defaults to None.
            can_send_voice_notes (bool, optional): True, if the user is allowed to send voice notes. Defaults to None.
            can_send_polls (bool, optional): True, if the user is allowed to send polls. Defaults to None.
            can_send_other_messages (bool, optional): True, if the user is allowed to send animations, games,
                stickers, and use inline bots. Defaults to None.
            can_add_web_page_previews (bool, optional): True, if the user is allowed to add web page previews to
                their messages. Defaults to None.
            can_change_info (bool, optional): True, if the user is allowed to change the chat title, photo, and
                other settings. Ignored in public supergroups. Defaults to None.
            can_invite_users (bool, optional): True, if the user is allowed to invite new users to the chat.
                Defaults to None.
            can_pin_messages (bool, optional): True, if the user is allowed to pin messages. Ignored in public
                supergroups. Defaults to None.
            can_manage_topics (bool, optional): True, if the user is allowed to create forum topics. If omitted,
                defaults to the value of can_pin_messages. Defaults to None.
        """
        self.can_send_messages = can_send_messages
        self.can_send_audios = can_send_audios
        self.can_send_documents = can_send_documents
        self.can_send_photos = can_send_photos
        self.can_send_videos = can_send_videos
        self.can_send_video_notes = can_send_video_notes
        self.can_send_voice_notes = can_send_voice_notes
        self.can_send_polls = can_send_polls
        self.can_send_other_messages = can_send_other_messages
        self.can_add_web_page_previews = can_add_web_page_previews
        self.can_change_info = can_change_info
        self.can_invite_users = can_invite_users
        self.can_pin_messages = can_pin_messages
        self.can_manage_topics = can_manage_topics
