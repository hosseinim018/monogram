from typing import Optional
from .baseType import BaseType
from .User import User
from .OrderInfo import OrderInfo

class PreCheckoutQuery(BaseType):
    """
    This object contains information about an incoming pre-checkout query.
    """
    
    def __init__(self, dictionary: dict = None):
        super().__init__(dictionary)
        
        self.id: str = None  # Unique query identifier
        self.from_user: User = None  # User who sent the query
        self.currency: str = None  # Three-letter ISO 4217 currency code
        self.total_amount: int = None  # Total price in the smallest units of the currency
        self.invoice_payload: str = None  # Bot specified invoice payload
        self.shipping_option_id: Optional[str] = None  # Optional. Identifier of the shipping option chosen by the user
        self.order_info: Optional[OrderInfo] = None  # Optional. Order information provided by the user

        if dictionary is not None:
            self.from_user = dictionary.get('from')  # 'from' is a reserved word in Python
            self.from_dictionary(dictionary)

    def from_dictionary(self, dictionary: dict):
        super().from_dictionary(dictionary)
        
        self.id = dictionary.get('id')
        if 'from' in dictionary:
            self.from_user = User(dictionary.get('from'))
        self.currency = dictionary.get('currency')
        self.total_amount = dictionary.get('total_amount')
        self.invoice_payload = dictionary.get('invoice_payload')
        self.shipping_option_id = dictionary.get('shipping_option_id')
        if 'order_info' in dictionary:
            self.order_info = OrderInfo(dictionary.get('order_info'))
