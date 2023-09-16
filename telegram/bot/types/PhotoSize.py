from typing import Optional

class PhotoSize:
    """
    This class represents one size of a photo or a file/sticker thumbnail.
    """

    def __init__(
        self,
        file_id: str,
        file_unique_id: str,
        width: int,
        height: int,
        file_size: Optional[int] = None
    ):
        """
        Initialize a PhotoSize object.

        Args:
            file_id (str): Identifier for this file, which can be used to download or reuse the file.
            file_unique_id (str): Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
            width (int): Photo width.
            height (int): Photo height.
            file_size (int, optional): File size in bytes.
        """
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.width = width
        self.height = height
        self.file_size = file_size
