from typing import Optional
class KeyboardButtonRequestChat:
    """
    This object defines the criteria used to request a suitable chat.
    """
    def __init__(self, request_id: int, chat_is_channel: bool, chat_is_forum: Optional[bool] = None,
                 chat_has_username: Optional[bool] = None, chat_is_created: Optional[bool] = None,
                 user_administrator_rights: Optional['ChatAdministratorRights'] = None,
                 bot_administrator_rights: Optional['ChatAdministratorRights'] = None,
                 bot_is_member: Optional[bool] = None):
        """
        Initialize a KeyboardButtonRequestChat object.

        :param request_id: Signed 32-bit identifier of the request, which will be received back in the ChatShared object. Must be unique within the message.
        :param chat_is_channel: Boolean indicating if the chat should be a channel.
        :param chat_is_forum: Optional. Boolean indicating if the chat should be a forum.
        :param chat_has_username: Optional. Boolean indicating if the chat should have a username.
        :param chat_is_created: Optional. Boolean indicating if the chat should be created.
        :param user_administrator_rights: Optional. The administrator rights required for a user in the chat.
        :param bot_administrator_rights: Optional. The administrator rights required for the bot in the chat.
        :param bot_is_member: Optional. Boolean indicating if the bot should be a member of the chat.
        """
        self.request_id = request_id
        self.chat_is_channel = chat_is_channel
        self.chat_is_forum = chat_is_forum
        self.chat_has_username = chat_has_username
        self.chat_is_created = chat_is_created
        self.user_administrator_rights = user_administrator_rights
        self.bot_administrator_rights = bot_administrator_rights
        self.bot_is_member = bot_is_member
