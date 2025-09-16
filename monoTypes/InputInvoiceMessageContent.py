from typing import Optional, List, Dict, Any
from .baseType import BaseType

class InputInvoiceMessageContent(BaseType):
    """
    Represents the content of an invoice message to be sent as the result of an inline query.
    """

    def __init__(
        self,
        title: str,
        description: str,
        payload: str,
        provider_token: Optional[str],
        currency: str,
        prices: List[Dict],
        max_tip_amount: Optional[int] = None,
        suggested_tip_amounts: Optional[List[int]] = None,
        provider_data: Optional[str] = None,
        photo_url: Optional[str] = None,
        photo_size: Optional[int] = None,
        photo_width: Optional[int] = None,
        photo_height: Optional[int] = None,
        need_name: Optional[bool] = None,
        need_phone_number: Optional[bool] = None,
        need_email: Optional[bool] = None,
        need_shipping_address: Optional[bool] = None,
        send_phone_number_to_provider: Optional[bool] = None,
        send_email_to_provider: Optional[bool] = None,
        is_flexible: Optional[bool] = None,
        **kwargs: Any
    ):
        """
        Initialize an InputInvoiceMessageContent object.

        Args:
            title (str): Product name, 1-32 characters
            description (str): Product description, 1-255 characters
            payload (str): Bot-defined invoice payload, 1-128 bytes
            provider_token (str, optional): Payment provider token, obtained via @BotFather
            currency (str): Three-letter ISO 4217 currency code
            prices (List[Dict]): Price breakdown, a JSON-serialized list of components
            max_tip_amount (int, optional): The maximum accepted amount for tips in the smallest units of the currency
            suggested_tip_amounts (List[int], optional): A JSON-serialized array of suggested amounts of tip
            provider_data (str, optional): A JSON-serialized object for data about the invoice
            photo_url (str, optional): URL of the product photo for the invoice
            photo_size (int, optional): Photo size in bytes
            photo_width (int, optional): Photo width
            photo_height (int, optional): Photo height
            need_name (bool, optional): Pass True if you require the user's full name to complete the order
            need_phone_number (bool, optional): Pass True if you require the user's phone number to complete the order
            need_email (bool, optional): Pass True if you require the user's email address to complete the order
            need_shipping_address (bool, optional): Pass True if you require the user's shipping address to complete the order
            send_phone_number_to_provider (bool, optional): Pass True if the user's phone number should be sent to the provider
            send_email_to_provider (bool, optional): Pass True if the user's email address should be sent to the provider
            is_flexible (bool, optional): Pass True if the final price depends on the shipping method
            **kwargs: Additional fields that might be added in future Telegram Bot API updates
        """
        super().__init__(**kwargs)

        # Required fields
        self.title = title
        self.description = description
        self.payload = payload
        self.provider_token = provider_token
        self.currency = currency
        self.prices = prices

        # Optional fields
        self.max_tip_amount = max_tip_amount
        self.suggested_tip_amounts = suggested_tip_amounts
        self.provider_data = provider_data
        self.photo_url = photo_url
        self.photo_size = photo_size
        self.photo_width = photo_width
        self.photo_height = photo_height
        self.need_name = need_name
        self.need_phone_number = need_phone_number
        self.need_email = need_email
        self.need_shipping_address = need_shipping_address
        self.send_phone_number_to_provider = send_phone_number_to_provider
        self.send_email_to_provider = send_email_to_provider
        self.is_flexible = is_flexible

        # Store any additional fields for future compatibility
        for key, value in kwargs.items():
            if not hasattr(self, key):
                setattr(self, key, value)

    def __str__(self) -> str:
        """
        Get a string representation of the input invoice message content.

        Returns:
            str: A string containing the title and description
        """
        return f"Invoice: {self.title}, {self.description}"