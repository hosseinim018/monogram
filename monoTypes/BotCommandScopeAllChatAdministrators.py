class BotCommandScopeAllChatAdministrators:
    """
    Represents the scope of bot commands, covering all group and supergroup chat administrators.
    """

    def __init__(self, type: str):
        """
        Initialize a BotCommandScopeAllChatAdministrators object.

        Args:
            type (str): Scope type, must be "all_chat_administrators".
        """
        self.type = type

