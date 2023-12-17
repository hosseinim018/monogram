class WebAppData:
    """
    This class describes data sent from a Web App to the bot.
    """

    def __init__(self, data: str, button_text: str):
        """
        Initialize a WebAppData object.

        Args:
            data (str): The data. Be aware that a bad client can send arbitrary data in this field.
            button_text (str): Text of the web_app keyboard button from which the Web App was opened. Be aware that a bad client can send arbitrary data in this field.
        """
        self.data = data
        self.button_text = button_text
