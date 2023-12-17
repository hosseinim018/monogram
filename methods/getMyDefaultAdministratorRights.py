from typing import Optional
from monogram import Monogram, validate_payload

class getMyDefaultAdministratorRights(Monogram):
    def __new__(cls, for_channels: Optional[bool] = False) -> dict:
        """
        Use this method to get the current default administrator rights of the bot.
        Returns ChatAdministratorRights on success.

        :param for_channels: Pass True to get default administrator rights of the bot in channels.
                             Otherwise, default administrator rights of the bot for groups and supergroups will be returned.
        :return: The current default administrator rights of the bot
        """
        payload = validate_payload(locals().copy())
        # send post request to telegram based on method sendMessage, Construct the API endpoint URL
        response = cls.request(cls, method='getMyDefaultAdministratorRights', data=payload, res=True)
        return response.json()