from typing import Union
from monogram import Monogram, validate_payload


class deleteChatPhoto(Monogram):
    def __new__(cls, chat_id: Union[int, str]) -> bool:
        """
        Use this method to delete a chat photo.
        Photos can't be changed for private chats.
        The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights.
        Returns True on success.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :return: True on success
        """
        # Your implementation here
        payload = validate_payload(locals().copy())
        # send post request to telegram based on method sendMessage, Construct the API endpoint URL
        response = cls.request(cls, method="deleteChatPhoto", data=payload, res=True)
        return response.json()
