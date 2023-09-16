class SwitchInlineQueryChosenChat:
    """
    This class represents an inline button that switches the current user to inline mode in a chosen chat, with an optional default inline query.
    """

    def __init__(
        self,
        query: str = None,
        allow_user_chats: bool = False,
        allow_bot_chats: bool = False,
        allow_group_chats: bool = False,
        allow_channel_chats: bool = False
    ):
        """
        Initialize a SwitchInlineQueryChosenChat object.

        Args:
            query (str, optional): The default inline query to be inserted in the input field.
                If left empty, only the bot's username will be inserted. This field is optional.
            allow_user_chats (bool, optional): True, if private chats with users can be chosen.
                This field is optional and defaults to False.
            allow_bot_chats (bool, optional): True, if private chats with bots can be chosen.
                This field is optional and defaults to False.
            allow_group_chats (bool, optional): True, if group and supergroup chats can be chosen.
                This field is optional and defaults to False.
            allow_channel_chats (bool, optional): True, if channel chats can be chosen.
                This field is optional and defaults to False.
        """
        self.query = query
        self.allow_user_chats = allow_user_chats
        self.allow_bot_chats = allow_bot_chats
        self.allow_group_chats = allow_group_chats
        self.allow_channel_chats = allow_channel_chats

