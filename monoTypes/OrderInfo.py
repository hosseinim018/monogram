from typing import Optional
from .baseType import BaseType
from .ShippingAddress import ShippingAddress

class OrderInfo(BaseType):
    """
    This object represents information about an order.
    """
    
    def __init__(self, dictionary: dict = None):
        super().__init__(dictionary)
        
        self.name: Optional[str] = None  # Optional. User name
        self.phone_number: Optional[str] = None  # Optional. User's phone number
        self.email: Optional[str] = None  # Optional. User email
        self.shipping_address: Optional[ShippingAddress] = None  # Optional. User shipping address

        if dictionary is not None:
            self.from_dictionary(dictionary)

    def from_dictionary(self, dictionary: dict):
        super().from_dictionary(dictionary)
        
        self.name = dictionary.get('name')
        self.phone_number = dictionary.get('phone_number')
        self.email = dictionary.get('email')
        if 'shipping_address' in dictionary:
            self.shipping_address = ShippingAddress(dictionary.get('shipping_address'))
