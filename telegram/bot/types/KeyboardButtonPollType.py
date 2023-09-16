from typing import Optional

class KeyboardButtonPollType:
    """
    This object represents the type of a poll.
    """
    def __init__(self, type: Optional[str] = None):
        """
        Initialize a KeyboardButtonPollType object.

        :param type: Optional. The type of the poll.
        """
        self.type = type
