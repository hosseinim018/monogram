from typing import Optional
from .baseType import BaseType
from .OrderInfo import OrderInfo

class SuccessfulPayment(BaseType):
    """
    This object contains basic information about a successful payment.
    https://core.telegram.org/bots/api#successfulpayment
    """
    
    def __init__(self, dictionary: dict = None):
        super().__init__(dictionary)
        
        # Required fields
        self.currency: str = None  # Three-letter ISO 4217 currency code
        self.total_amount: int = None  # Total price in the smallest units of the currency
        self.invoice_payload: str = None  # Bot specified invoice payload
        self.telegram_payment_charge_id: str = None  # Telegram payment identifier
        self.provider_payment_charge_id: str = None  # Provider payment identifier
        
        # Optional fields
        self.shipping_option_id: Optional[str] = None  # Identifier of the shipping option chosen by the user
        self.order_info: Optional[OrderInfo] = None  # Order information provided by the user

        if dictionary is not None:
            self.from_dictionary(dictionary)

    def from_dictionary(self, dictionary: dict):
        super().from_dictionary(dictionary)
        
        self.currency = dictionary.get('currency')
        self.total_amount = dictionary.get('total_amount')
        self.invoice_payload = dictionary.get('invoice_payload')
        self.telegram_payment_charge_id = dictionary.get('telegram_payment_charge_id')
        self.provider_payment_charge_id = dictionary.get('provider_payment_charge_id')
        self.shipping_option_id = dictionary.get('shipping_option_id')
        
        if 'order_info' in dictionary:
            self.order_info = OrderInfo(dictionary.get('order_info'))
