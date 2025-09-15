from .baseType import BaseType

class ShippingAddress(BaseType):
    """
    This object represents a shipping address.
    """
    
    def __init__(self, dictionary: dict = None):
        super().__init__(dictionary)
        
        self.country_code: str = None  # Two-letter ISO 3166-1 alpha-2 country code
        self.state: str = None  # State, if applicable
        self.city: str = None  # City
        self.street_line1: str = None  # First line for the address
        self.street_line2: str = None  # Second line for the address
        self.post_code: str = None  # Address post code

        if dictionary is not None:
            self.from_dictionary(dictionary)

    def from_dictionary(self, dictionary: dict):
        super().from_dictionary(dictionary)
        
        self.country_code = dictionary.get('country_code')
        self.state = dictionary.get('state')
        self.city = dictionary.get('city')
        self.street_line1 = dictionary.get('street_line1')
        self.street_line2 = dictionary.get('street_line2')
        self.post_code = dictionary.get('post_code')
