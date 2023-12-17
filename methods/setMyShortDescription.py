from typing import Optional
from monogram import Monogram, validate_payload


class setMyShortDescription(Monogram):
    def __new__(cls, short_description: Optional[str] = None, language_code: Optional[str] = None) -> bool:
        """
        Use this method to change the bot's short description, which is shown on the bot's profile page
        and is sent together with the link when users share the bot.
        Returns True on success.

        :param short_description: New short description for the bot; 0-120 characters.
                                  Pass an empty string to remove the dedicated short description for the given language.
        :param language_code: A two-letter ISO 639-1 language code.
                              If empty, the short description will be applied to all users for whose language
                              there is no dedicated short description.
        :return: True on success
        """
        payload = validate_payload(locals().copy())
        # send post request to telegram based on method sendMessage, Construct the API endpoint URL
        response = cls.request(cls, method='setMyShortDescription', data=payload, res=True)
        return response.json()