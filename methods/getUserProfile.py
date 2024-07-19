from typing import Optional
from monogram import Monogram, validate_payload
from monogram.types import UserProfilePhotos


class getUserProfile(Monogram):
    def __new__(
        cls, user_id: int, offset: Optional[int] = None, limit: Optional[int] = 100
    ) -> UserProfilePhotos:
        """
        Use this method to get a list of profile pictures for a user. Returns a UserProfilePhotos object.

        :param user_id: Unique identifier of the target user
        :param offset: Sequential number of the first photo to be returned. By default, all photos are returned.
        :param limit: Limits the number of photos to be retrieved. Values between 1-100 are accepted. Defaults to 100.
        :return: A UserProfilePhotos object containing the user's profile photos
        """
        payload = validate_payload(locals().copy())
        # send post request to telegram based on method sendMessage, Construct the API endpoint URL
        response = cls.request(cls, method="getUserProfilePhotos", data=payload, res=True)
        return response.json()
