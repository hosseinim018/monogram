class BotCommandScopeDefault:
    """
    Represents the default scope of bot commands.
    """

    def __init__(self, type: str):
        """
        Initialize a BotCommandScopeDefault object.

        Args:
            type (str): Scope type, must be "default".
        """
        self.type = type
