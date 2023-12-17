from typing import Optional
from monogram import Monogram, validate_payload



class setMyName(Monogram):
    def __new__(cls, name: Optional[str] = None, language_code: Optional[str] = None) -> bool:
        """
        Use this method to change the bot's name.
        Returns True on success.

        :param name: New bot name; 0-64 characters.
                     Pass an empty string to remove the dedicated name for the given language.
        :param language_code: A two-letter ISO 639-1 language code.
                              If empty, the name will be shown to all users for whose language
                              there is no dedicated name.
        :return: True on success
        """
        payload = validate_payload(locals().copy())
        # send post request to telegram based on method sendMessage, Construct the API endpoint URL
        response = cls.request(cls, method='setMyName', data=payload, res=True)
        return response.json()