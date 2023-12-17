class ChatPhoto:
    """
    This class represents a chat photo.
    """

    def __init__(
        self,
        small_file_id: str,
        small_file_unique_id: str,
        big_file_id: str,
        big_file_unique_id: str
    ):
        """
        Initialize a ChatPhoto object.

        Args:
            small_file_id (str): File identifier of the small (160x160) chat photo.
                This file_id can be used only for photo download and only for as long as the photo is not changed.
            small_file_unique_id (str): Unique file identifier of the small (160x160) chat photo,
                which is supposed to be the same over time and for different bots.
                This unique_id can't be used to download or reuse the file.
            big_file_id (str): File identifier of the big (640x640) chat photo.
                This file_id can be used only for photo download and only for as long as the photo is not changed.
            big_file_unique_id (str): Unique file identifier of the big (640x640) chat photo,
                which is supposed to be the same over time and for different bots.
                This unique_id can't be used to download or reuse the file.
        """
        self.small_file_id = small_file_id
        self.small_file_unique_id = small_file_unique_id
        self.big_file_id = big_file_id
        self.big_file_unique_id = big_file_unique_id

