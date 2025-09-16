from typing import Any
from .baseType import BaseType
from .InlineQueryResult import InlineQueryResult
from .SentWebAppMessage import SentWebAppMessage

class answerWebAppQuery(BaseType):
    """
    Use this method to set the result of an interaction with a Web App and send a corresponding message on behalf of the user to the chat from which the query originated.
    On success, a SentWebAppMessage object is returned.
    """

    def __init__(
        self,
        web_app_query_id: str,
        result: InlineQueryResult,
        **kwargs: Any
    ):
        """
        Initialize an answerWebAppQuery object.

        Args:
            web_app_query_id (str): Unique identifier for the query to be answered
            result (InlineQueryResult): A JSON-serialized object describing the message to be sent
            **kwargs: Additional fields that might be added in future Telegram Bot API updates
        """
        super().__init__(**kwargs)

        # Required fields
        self.web_app_query_id = web_app_query_id
        self.result = result

        # Store any additional fields for future compatibility
        for key, value in kwargs.items():
            if not hasattr(self, key):
                setattr(self, key, value)

    def __str__(self) -> str:
        """
        Get a string representation of the answerWebAppQuery object.

        Returns:
            str: A string containing the Web App query ID
        """
        return f"answerWebAppQuery: {self.web_app_query_id}"