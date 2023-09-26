from typing import List, Optional


def set_my_commands(commands: List[BotCommand], scope: Optional[BotCommandScope] = None, language_code: Optional[str] = None) -> bool:
    """
    Use this method to change the list of the bot's commands.
    Returns True on success.

    :param commands: A list of BotCommand objects to be set as the list of the bot's commands.
                     At most 100 commands can be specified.
    :param scope: An object describing the scope of users for which the commands are relevant.
                  Defaults to BotCommandScopeDefault.
    :param language_code: A two-letter ISO 639-1 language code.
                          If empty, commands will be applied to all users from the given scope,
                          for whose language there are no dedicated commands.
    :return: True on success
    """
    # Your implementation here
    pass