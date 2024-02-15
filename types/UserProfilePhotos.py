from typing import List
from .PhotoSize import PhotoSize


class UserProfilePhotos:
    """
    This class represents a user's profile pictures.
    """

    def __init__(self, total_count: int, photos: List[List[PhotoSize]]):
        """
        Initialize a UserProfilePhotos object.

        Args:
            total_count (int): Total number of profile pictures the target user has.
            photos (List[List[PhotoSize]]): Requested profile pictures (in up to 4 sizes each).
        """
        self.total_count = total_count
        self.photos = photos
