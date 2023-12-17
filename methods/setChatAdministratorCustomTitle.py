from typing import Union
from monogram import Monogram, validate_payload

class setChatAdministratorCustomTitle(Monogram):
    def __new__(cls,
        chat_id: Union[int, str],
        user_id: int,
        custom_title: str,
    ) -> bool:
        """
        Use this method to set a custom title for an administrator in a supergroup promoted by the bot.
        Returns True on success.

        :param chat_id: Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
        :param user_id: Unique identifier of the target user
        :param custom_title: New custom title for the administrator; 0-16 characters, emoji are not allowed
        :return: True on success
        """
        payload = validate_payload(locals().copy())
        # send post request to telegram based on method sendMessage, Construct the API endpoint URL
        response = cls.request(cls, method='setChatAdministratorCustomTitle', data=payload, res=True)
        return response.json()