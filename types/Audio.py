from typing import Optional

class Audio:
    """
    This class represents an audio file to be treated as music by the Telegram clients.
    """

    def __init__(
        self,
        file_id: str,
        file_unique_id: str,
        duration: int,
        performer: Optional[str] = None,
        title: Optional[str] = None,
        file_name: Optional[str] = None,
        mime_type: Optional[str] = None,
        file_size: Optional[int] = None,
        thumbnail: Optional['PhotoSize'] = None
    ):
        """
        Initialize an Audio object.

        Args:
            file_id (str): Identifier for this file, which can be used to download or reuse the file.
            file_unique_id (str): Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
            duration (int): Duration of the audio in seconds as defined by the sender.
            performer (str, optional): Performer of the audio as defined by the sender or by audio tags.
            title (str, optional): Title of the audio as defined by the sender or by audio tags.
            file_name (str, optional): Original filename as defined by the sender.
            mime_type (str, optional): MIME type of the file as defined by the sender.
            file_size (int, optional): File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value.
            thumbnail (PhotoSize, optional): Thumbnail of the album cover to which the music file belongs.
        """
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.duration = duration
        self.performer = performer
        self.title = title
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size
        self.thumbnail = thumbnail
