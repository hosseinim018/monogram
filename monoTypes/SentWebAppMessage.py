from typing import Optional, Any
from .baseType import BaseType

class SentWebAppMessage(BaseType):
    """
    Describes an inline message sent by a Web App on behalf of a user.
    """

    def __init__(
        self,
        inline_message_id: Optional[str] = None,
        **kwargs: Any
    ):
        """
        Initialize a SentWebAppMessage object.

        Args:
            inline_message_id (str, optional): Identifier of the sent inline message
            **kwargs: Additional fields that might be added in future Telegram Bot API updates
        """
        super().__init__(**kwargs)

        # Optional fields
        self.inline_message_id = inline_message_id

        # Store any additional fields for future compatibility
        for key, value in kwargs.items():
            if not hasattr(self, key):
                setattr(self, key, value)

    def __str__(self) -> str:
        """
        Get a string representation of the sent Web App message.

        Returns:
            str: A string containing the inline message ID
        """
        return f"SentWebAppMessage: {self.inline_message_id}"