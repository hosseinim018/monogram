from typing import Any
from .baseType import BaseType

class PreparedInlineMessage(BaseType):
    """
    Describes an inline message to be sent by a user of a Mini App.
    """

    def __init__(
        self,
        id: str,
        expiration_date: int,
        **kwargs: Any
    ):
        """
        Initialize a PreparedInlineMessage object.

        Args:
            id (str): Unique identifier of the prepared message
            expiration_date (int): Expiration date of the prepared message, in Unix time
            **kwargs: Additional fields that might be added in future Telegram Bot API updates
        """
        super().__init__(**kwargs)

        # Required fields
        self.id = id
        self.expiration_date = expiration_date

        # Store any additional fields for future compatibility
        for key, value in kwargs.items():
            if not hasattr(self, key):
                setattr(self, key, value)

    def __str__(self) -> str:
        """
        Get a string representation of the prepared inline message.

        Returns:
            str: A string containing the ID and expiration date
        """
        return f"PreparedInlineMessage: {self.id}, Expires: {self.expiration_date}"
