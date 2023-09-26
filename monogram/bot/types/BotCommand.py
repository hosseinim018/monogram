class BotCommand:
    """
    Represents a bot command.
    """

    def __new__(cls, command: str, description: str):
        """
        Initialize a BotCommand object.

        Args:
            command (str): Text of the command; 1-32 characters. Can contain only lowercase English letters, digits, and underscores.
            description (str): Description of the command; 1-256 characters.
        """
        cls.command = command
        cls.description = description

        payload = {"command": command, "description": description}
        return payload
