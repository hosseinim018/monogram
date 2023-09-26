
def get_my_commands(scope: Optional[BotCommandScope] = None, language_code: Optional[str] = None) -> List[BotCommand]:
    """
    Use this method to get the current list of the bot's commands for the given scope and user language.
    Returns a list of BotCommand objects. If commands aren't set, an empty list is returned.

    :param scope: An object describing the scope of users.
                  Defaults to BotCommandScopeDefault.
    :param language_code: A two-letter ISO 639-1 language code or an empty string.
    :return: A list of BotCommand objects
    """
    # Your implementation here
    pass