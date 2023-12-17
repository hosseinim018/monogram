from typing import Union
from monogram import Monogram, validate_payload

class setChatDescription(Monogram):
    def __new__(cls,
        chat_id: Union[int, str],
        description: str
    ) -> bool:
        """
        Use this method to change the description of a group, a supergroup, or a channel.
        The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights.
        Returns True on success.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param description: New chat description, 0-255 characters
        :return: True on success
        """
        payload = validate_payload(locals().copy())
        # send post request to telegram based on method sendMessage, Construct the API endpoint URL
        response = cls.request(cls, method='setChatDescription', data=payload, res=True)
        return response.json()