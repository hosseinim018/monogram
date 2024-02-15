from monogram import Monogram, validate_payload


class deleteChatStickerSet(Monogram):
    def __new__(cls, chat_id):
        """
        Use this method to delete a group sticker set from a supergroup.
        The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights.
        Use the field can_set_sticker_set optionally returned in getChat requests to check if the bot can use this method.
        Returns True on success.

        :param chat_id: Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
        :return: True on success
        """
        payload = validate_payload(locals().copy())
        # send post request to telegram based on method sendMessage, Construct the API endpoint URL
        response = cls.request(
            cls, method="deleteChatStickerSet", data=payload, res=True
        )
        return response.json()
