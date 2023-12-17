class BotCommandScope:
    """
    Represents the scope to which bot commands are applied.
    """

    def __init__(self, scope: str, language_code: str = None):
        """
        Initialize a BotCommandScope object.

        Args:
            scope (str): The scope of the bot command.
            language_code (str, optional): Language code. Defaults to None.
        """
        self.scope = scope
        self.language_code = language_code
