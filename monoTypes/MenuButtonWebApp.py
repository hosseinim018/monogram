from .WebAppInfo import WebAppInfo


class MenuButtonWebApp:
    """
    Represents a menu button that launches a Web App.
    """

    def __init__(self, text: str, web_app: WebAppInfo):
        """
        Initialize a MenuButtonWebApp object.

        Args:
            text (str): Text on the button.
            web_app (WebAppInfo): Description of the Web App that will be launched when the button is pressed.
        """
        self.type = "web_app"
        self.text = text
        self.web_app = web_app
