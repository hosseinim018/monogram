from typing import Optional


def delete_my_commands(scope: Optional[BotCommandScope] = None, language_code: Optional[str] = None) -> bool:
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
    # Your implementation here
    pass