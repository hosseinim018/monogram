class BotCommandScopeAllGroupChats:
    """
    Represents the scope of bot commands, covering all group and supergroup chats.
    """

    def __init__(self, type: str):
        """
        Initialize a BotCommandScopeAllGroupChats object.

        Args:
            type (str): Scope type, must be "all_group_chats".
        """
        self.type = type
