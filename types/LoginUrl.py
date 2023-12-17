class LoginUrl:
    """
    This class represents a parameter of the inline keyboard button used to automatically authorize a user.
    """

    def __init__(
        self,
        url: str,
        forward_text: str = None,
        bot_username: str = None,
        request_write_access: bool = False
    ):
        """
        Initialize a LoginUrl object.

        Args:
            url (str): An HTTPS URL to be opened with user authorization data added to the query string when the button is pressed.
                If the user refuses to provide authorization data, the original URL without information about the user will be opened.
                The data added is the same as described in Receiving authorization data.
            forward_text (str, optional): New text of the button in forwarded messages. This field is optional.
            bot_username (str, optional): Username of a bot, which will be used for user authorization.
                See Setting up a bot for more details. If not specified, the current bot's username will be assumed.
                The url's domain must be the same as the domain linked with the bot. See Linking your domain to the bot for more details.
                This field is optional.
            request_write_access (bool, optional): Pass True to request the permission for your bot to send messages to the user.
                This field is optional and defaults to False.
        """
        self.url = url
        self.forward_text = forward_text
        self.bot_username = bot_username
        self.request_write_access = request_write_access
