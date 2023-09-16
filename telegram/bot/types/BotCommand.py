class BotCommand:
    """
    Represents a bot command.
    """

    def __init__(self, command: str, description: str):
        """
        Initialize a BotCommand object.

        Args:
            command (str): Text of the command; 1-32 characters. Can contain only lowercase English letters, digits, and underscores.
            description (str): Description of the command; 1-256 characters.
        """
        self.command = command
        self.description = description
