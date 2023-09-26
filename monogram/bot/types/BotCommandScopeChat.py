class BotCommandScopeChat:
    """
    Represents the scope of bot commands, covering a specific chat.
    """

    def __init__(self, type: str, chat_id: int):
        """
        Initialize a BotCommandScopeChat object.

        Args:
            type (str): Scope type, must be "chat".
            chat_id (int or str): Unique identifier for the target chat or username of the target supergroup.
        """
        self.type = type
        self.chat_id = chat_id

