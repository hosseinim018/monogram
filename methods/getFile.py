from typing import Optional
from monogram import Monogram, validate_payload
from monogram.types import File


class getFile(Monogram):
    def __new__(cls, file_id: str) -> File:
        """
        Use this method to get basic information about a file and prepare it for downloading.
        For the moment, bots can download files of up to 20MB in size.
        On success, a File object is returned.
        The file can then be downloaded via the link https://api.telegram.org/file/bot<token>/<file_path>,
        where <file_path> is taken from the response.
        It is guaranteed that the link will be valid for at least 1 hour.
        When the link expires, a new one can be requested by calling getFile again.

        :param file_id: File identifier to get information about
        :return: A File object containing information about the file
        """
        payload = validate_payload(locals().copy())
        # send post request to telegram based on method sendMessage, Construct the API endpoint URL
        response = cls.request(cls, method="getFile", data=payload, res=True)
        return response.json()
