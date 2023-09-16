class File:
    """
    This class represents a file ready to be downloaded.
    """

    def __init__(self, file_id: str, file_unique_id: str, file_size: int = None, file_path: str = None):
        """
        Initialize a File object.

        Args:
            file_id (str): Identifier for this file, which can be used to download or reuse the file.
            file_unique_id (str): Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
            file_size (int, optional): File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value. This field is optional.
            file_path (str, optional): File path. Use https://api.telegram.org/file/bot<token>/<file_path> to get the file. This field is optional.
        """
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.file_size = file_size
        self.file_path = file_path
