from typing import Optional
from monogram import Monogram, validate_payload


class setMyDescription(Monogram):
    def __new__(cls, description: Optional[str] = None, language_code: Optional[str] = None) -> bool:
        """
        Use this method to change the bot's description, which is shown in the chat with the bot if the chat is empty.
        Returns True on success.

        :param description: New bot description; 0-512 characters.
                            Pass an empty string to remove the dedicated description for the given language.
        :param language_code: A two-letter ISO 639-1 language code.
                              If empty, the description will be applied to all users for whose language
                              there is no dedicated description.
        :return: True on success
        """
        payload = validate_payload(locals().copy())
        # send post request to telegram based on method sendMessage, Construct the API endpoint URL
        response = cls.request(cls, method='setMyDescription', data=payload, res=True)
        return response.json()