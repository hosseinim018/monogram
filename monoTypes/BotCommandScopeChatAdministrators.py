class BotCommandScopeChatAdministrators:
    """
    Represents the scope of bot commands, covering all administrators of a specific group or supergroup chat.
    """

    def __init__(self, type: str, chat_id: int):
        """
        Initialize a BotCommandScopeChatAdministrators object.

        Args:
            type (str): Scope type, must be "chat_administrators".
            chat_id (int or str): Unique identifier for the target chat or username of the target supergroup.
        """
        self.type = type
        self.chat_id = chat_id

