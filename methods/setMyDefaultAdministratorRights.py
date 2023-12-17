from typing import Optional
from monogram import Monogram, validate_payload

class setMyDefaultAdministratorRights(Monogram):
    def __new__(cls, rights: Optional[dict] = None, for_channels: Optional[bool] = False) -> bool:
        """
        Use this method to change the default administrator rights requested by the bot
        when it's added as an administrator to groups or channels.
        These rights will be suggested to users, but they are free to modify the list before adding the bot.
        Returns True on success.

        :param rights: A JSON-serialized object describing new default administrator rights.
                       If not specified, the default administrator rights will be cleared.
        :param for_channels: Pass True to change the default administrator rights of the bot in channels.
                             Otherwise, the default administrator rights of the bot for groups and supergroups will be changed.
        :return: True on success
        """
        payload = validate_payload(locals().copy())
        # send post request to telegram based on method sendMessage, Construct the API endpoint URL
        response = cls.request(cls, method='setMyDefaultAdministratorRights', data=payload, res=True)
        return response.json()