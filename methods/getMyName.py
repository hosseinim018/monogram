from typing import Optional
from monogram import Monogram, validate_payload



class getMyName(Monogram):
    def __new__(cls, language_code: Optional[str] = None) -> str:
        """
        Use this method to get the current bot name for the given user language.
        Returns BotName on success.

        :param language_code: A two-letter ISO 639-1 language code or an empty string.
        :return: The current bot name
        """
        payload = validate_payload(locals().copy())
        # send post request to telegram based on method sendMessage, Construct the API endpoint URL
        response = cls.request(cls, method='getMyName', data=payload, res=True)
        return response.json()