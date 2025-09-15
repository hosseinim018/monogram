from .baseType import BaseType
from .User import User
from .ShippingAddress import ShippingAddress

class ShippingQuery(BaseType):
    """
    This object contains information about an incoming shipping query.
    """
    
    def __init__(self, dictionary: dict = None):
        super().__init__(dictionary)
        
        self.id: str = None  # Unique query identifier
        self.from_user: User = None  # User who sent the query
        self.invoice_payload: str = None  # Bot specified invoice payload
        self.shipping_address: ShippingAddress = None  # User specified shipping address

        if dictionary is not None:
            self.from_user = dictionary.get('from')  # 'from' is a reserved word in Python
            self.from_dictionary(dictionary)

    def from_dictionary(self, dictionary: dict):
        super().from_dictionary(dictionary)
        
        self.id = dictionary.get('id')
        if 'from' in dictionary:
            self.from_user = User(dictionary.get('from'))
        self.invoice_payload = dictionary.get('invoice_payload')
        if 'shipping_address' in dictionary:
            self.shipping_address = ShippingAddress(dictionary.get('shipping_address'))
