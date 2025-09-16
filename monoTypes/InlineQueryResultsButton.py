from typing import Optional, Dict, Any
from .baseType import BaseType
from .WebAppInfo import WebAppInfo

class InlineQueryResultsButton(BaseType):
    """
    This object represents a button to be shown above inline query results.
    You must use exactly one of the optional fields.
    """

    def __init__(
        self,
        text: str,
        web_app: Optional[Dict] = None,
        start_parameter: Optional[str] = None,
        **kwargs: Any
    ):
        """
        Initialize an InlineQueryResultsButton object.

        Args:
            text (str): Label text on the button
            web_app (dict, optional): Description of the Web App that will be launched when the user presses the button.
            start_parameter (str, optional): Deep-linking parameter for the /start message.
            **kwargs: Additional fields.
        """
        super().__init__(**kwargs)
        self.text = text
        self.web_app = WebAppInfo(**web_app) if web_app else None
        self.start_parameter = start_parameter
        
        if web_app and start_parameter:
            raise ValueError("You must use exactly one of the optional fields 'web_app' or 'start_parameter'.")
