from typing import Optional


class VideoNote:
    """
    This class represents a video message (available in Telegram apps as of v.4.0).
    """

    def __init__(
            self,
            file_id: str,
            file_unique_id: str,
            length: int,
            duration: int,
            thumbnail: Optional[dict] = None,
            file_size: Optional[int] = None
    ):
        """
        Initialize a VideoNote object.

        Args:
            file_id (str): Identifier for this file, which can be used to download or reuse the file.
            file_unique_id (str): Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
            length (int): Video width and height (diameter of the video message) as defined by the sender.
            duration (int): Duration of the video in seconds as defined by the sender.
            thumbnail (PhotoSize, optional): Video thumbnail.
            file_size (int, optional): File size in bytes.
        """
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.length = length
        self.duration = duration
        # TODO: thumbnail = Photoseze(**thumbnail)
        self.thumbnail = thumbnail
        self.file_size = file_size
