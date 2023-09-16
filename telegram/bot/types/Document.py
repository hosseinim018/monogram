from typing import Optional

class Document:
    """
    This class represents a general file (as opposed to photos, voice messages, and audio files).
    """

    def __init__(
        self,
        file_id: str,
        file_unique_id: str,
        thumbnail: Optional['PhotoSize'] = None,
        file_name: Optional[str] = None,
        mime_type: Optional[str] = None,
        file_size: Optional[int] = None
    ):
        """
        Initialize a Document object.

        Args:
            file_id (str): Identifier for this file, which can be used to download or reuse the file.
            file_unique_id (str): Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
            thumbnail (PhotoSize, optional): Document thumbnail as defined by the sender.
            file_name (str, optional): Original filename as defined by the sender.
            mime_type (str, optional): MIME type of the file as defined by the sender.
            file_size (int, optional): File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value.
        """
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.thumbnail = thumbnail
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size
