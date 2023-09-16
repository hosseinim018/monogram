class VideoChatScheduled:
    """
    This class represents a service message about a video chat scheduled in the chat.
    """

    def __init__(self, start_date: int):
        """
        Initialize a VideoChatScheduled object.

        Args:
            start_date (int): Point in time (Unix timestamp) when the video chat is supposed to be started by a chat administrator.
        """
        self.start_date = start_date
