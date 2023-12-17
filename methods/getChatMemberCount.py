from typing import Union
from monogram import Monogram, validate_payload

class getChatMemberCount(Monogram):
    def __new__(cls ,chat_id: Union[int, str]) -> int:
        """
        Use this method to get the number of members in a chat.
        Returns an int on success.

        :param chat_id: Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername)
        :return: Number of members in the chat (int)
        """
        payload = validate_payload(locals().copy())
        # send post request to telegram based on method sendMessage, Construct the API endpoint URL
        response = cls.request(cls, method='getChatMemberCount', data=payload, res=True)
        return response.json()