from typing import Optional, Any
from .baseType import BaseType

class InputContactMessageContent(BaseType):
    """
    Represents the content of a contact message to be sent as the result of an inline query.
    """

    def __init__(
        self,
        phone_number: str,
        first_name: str,
        last_name: Optional[str] = None,
        vcard: Optional[str] = None,
        **kwargs: Any
    ):
        """
        Initialize an InputContactMessageContent object.

        Args:
            phone_number (str): Contact's phone number
            first_name (str): Contact's first name
            last_name (str, optional): Contact's last name
            vcard (str, optional): Additional data about the contact in the form of a vCard, 0-2048 bytes
            **kwargs: Additional fields that might be added in future Telegram Bot API updates
        """
        super().__init__(**kwargs)

        # Required fields
        self.phone_number = phone_number
        self.first_name = first_name

        # Optional fields
        self.last_name = last_name
        self.vcard = vcard

        # Store any additional fields for future compatibility
        for key, value in kwargs.items():
            if not hasattr(self, key):
                setattr(self, key, value)

    def __str__(self) -> str:
        """
        Get a string representation of the input contact message content.

        Returns:
            str: A string containing the contact's first name and phone number
        """
        return f"Contact: {self.first_name}, {self.phone_number}"