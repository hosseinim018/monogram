from monogram import Monogram, validate_payload

class setChatStickerSet(Monogram):
    def __new__(cls, chat_id, sticker_set_name):
        """
        Use this method to set a new group sticker set for a supergroup.
        The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights.
        Use the field can_set_sticker_set optionally returned in getChat requests to check if the bot can use this method.
        Returns True on success.

        :param chat_id: Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
        :param sticker_set_name: Name of the sticker set to be set as the group sticker set
        :return: True on success
        """
        payload = validate_payload(locals().copy())
        # send post request to telegram based on method sendMessage, Construct the API endpoint URL
        response = cls.request(cls, method='setChatStickerSet', data=payload, res=True)
        return response.json()