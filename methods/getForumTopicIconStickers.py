from monogram import Monogram, validate_payload

class getForumTopicIconStickers(Monogram):
    def __new__(cls):
        """
        Use this method to get custom emoji stickers that can be used as a forum topic icon by any user.
        Requires no parameters.
        Returns an array of Sticker objects.

        :return: Array of Sticker objects
        """
        payload = validate_payload(locals().copy())
        # send post request to telegram based on method sendMessage, Construct the API endpoint URL
        response = cls.request(cls, method='getForumTopicIconStickers', data=payload, res=True)
        return response.json()