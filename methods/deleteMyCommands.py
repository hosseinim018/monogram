from typing import Optional
from monogram import Monogram, validate_payload
from monogram.types import BotCommandScope


class deleteMyCommands(Monogram):
    def __new__(
        cls,
        scope: Optional[BotCommandScope] = None,
        language_code: Optional[str] = None,
    ) -> bool:
        """
        Use this method to delete the list of the bot's commands for the given scope and user language.
        After deletion, higher level commands will be shown to affected users.
        Returns True on success.

        :param scope: An object describing the scope of users for which the commands are relevant.
                      Defaults to BotCommandScopeDefault.
        :param language_code: A two-letter ISO 639-1 language code.
                              If empty, commands will be applied to all users from the given scope,
                              for whom there are no dedicated commands.
        :return: True on success
        """
        payload = validate_payload(locals().copy())
        # send post request to telegram based on method sendMessage, Construct the API endpoint URL
        response = cls.request(cls, method="deleteMyCommands", data=payload, res=True)
        return response.json()
