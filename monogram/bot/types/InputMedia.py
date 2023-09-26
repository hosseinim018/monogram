class InputMedia:
    """
    Base class for representing the content of a media message to be sent.
    """

    def __init__(self, media: str):
        """
        Initialize an InputMedia object.

        Args:
            media (str): The media file to be sent.
        """
        self.media = media
