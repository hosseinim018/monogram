from typing import Union
from monogram import Monogram, validate_payload

class leaveChat(Monogram):
    def __new__(cls, chat_id: Union[int, str]) -> bool:
        """
        Use this method for your bot to leave a group, supergroup, or channel.
        Returns True on success.

        :param chat_id: Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername)
        :return: True on success
        """
        payload = validate_payload(locals().copy())
        # send post request to telegram based on method sendMessage, Construct the API endpoint URL
        response = cls.request(cls, method='leaveChat', data=payload, res=True)
        return response.json()