class BotCommandScopeAllPrivateChats:
    """
    Represents the scope of bot commands, covering all private chats.
    """

    def __init__(self, type: str):
        """
        Initialize a BotCommandScopeAllPrivateChats object.

        Args:
            type (str): Scope type, must be "all_private_chats".
        """
        self.type = type
