class WriteAccessAllowed:
    """
    This class represents a service message about a user allowing a bot to write messages after adding the bot to the attachment menu or launching a Web App from a link.
    """

    def __init__(self, web_app_name: str = None):
        """
        Initialize a WriteAccessAllowed object.

        Args:
            web_app_name (str, optional): Name of the Web App which was launched from a link.
        """
        self.web_app_name = web_app_name

