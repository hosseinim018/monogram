from .User import User


class ChatMemberRestricted:
    """
    This class represents a chat member with certain restrictions in the chat. Only applicable to supergroups.
    """

    def __init__(
        self,
        status: str,
        user: User,
        is_member: bool,
        can_send_messages: bool,
        can_send_audios: bool,
        can_send_documents: bool,
        can_send_photos: bool,
        can_send_videos: bool,
        can_send_video_notes: bool,
        can_send_voice_notes: bool,
        can_send_polls: bool,
        can_send_other_messages: bool,
        can_add_web_page_previews: bool,
        can_change_info: bool,
        can_invite_users: bool,
        can_pin_messages: bool,
        can_manage_topics: bool,
        until_date: int,
    ):
        """
        Initialize a ChatMemberRestricted object.

        Args:
            status (str): The member's status in the chat. It is always "restricted" for a ChatMemberRestricted.
            user (User): Information about the user who is a member.
            is_member (bool): True if the user is a member of the chat at the moment of the request.
            can_send_messages (bool): True if the user is allowed to send text messages, contacts, invoices,
                locations, and venues.
            can_send_audios (bool): True if the user is allowed to send audios.
            can_send_documents (bool): True if the user is allowed to send documents.
            can_send_photos (bool): True if the user is allowed to send photos.
            can_send_videos (bool): True if the user is allowed to send videos.
            can_send_video_notes (bool): True if the user is allowed to send video notes.
            can_send_voice_notes (bool): True if the user is allowed to send voice notes.
            can_send_polls (bool): True if the user is allowed to send polls.
            can_send_other_messages (bool): True if the user is allowed to send animations, games, stickers,
                and use inline bots.
            can_add_web_page_previews (bool): True if the user is allowed to add web page previews to their messages.
            can_change_info (bool): True if the user is allowed to change the chat title, photo, and other settings.
            can_invite_users (bool): True if the user is allowed to invite new users to the chat.
            can_pin_messages (bool): True if the user is allowed to pin messages.
            can_manage_topics (bool): True if the user is allowed to create forum topics.
            until_date (int): Date when restrictions will be lifted for this user, in Unix time. If 0, the user is
                restricted forever.
        """
        self.status = status
        self.user = user
        self.is_member = is_member
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
        self.until_date = until_date
