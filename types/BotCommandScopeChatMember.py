class BotCommandScopeChatMember:
    """
    Represents the scope of bot commands, covering a specific member of a group or supergroup chat.
    """

    def __init__(self, type: str, chat_id: int, user_id: int):
        """
        Initialize a BotCommandScopeChatMember object.

        Args:
            type (str): Scope type, must be "chat_member".
            chat_id (int or str): Unique identifier for the target chat or username of the target supergroup.
            user_id (int): Unique identifier of the target user.
        """
        self.type = type
        self.chat_id = chat_id
        self.user_id = user_id
