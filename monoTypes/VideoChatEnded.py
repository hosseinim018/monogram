class VideoChatEnded:
    """
    This class represents a service message about a video chat ended in the chat.
    """

    def __init__(self, duration: int):
        """
        Initialize a VideoChatEnded object.

        Args:
            duration (int): Video chat duration in seconds.
        """
        self.duration = duration

