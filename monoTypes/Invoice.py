from .baseType import BaseType

class Invoice(BaseType):
    """
    This object contains basic information about an invoice.
    https://core.telegram.org/bots/api#invoice
    """
    
    def __init__(self, dictionary: dict = None):
        super().__init__(dictionary)
        
        # Required fields
        self.title: str = None  # Product name
        self.description: str = None  # Product description
        self.start_parameter: str = None  # Unique bot deep-linking parameter
        self.currency: str = None  # Three-letter ISO 4217 currency code
        self.total_amount: int = None  # Total price in the smallest units of the currency

        if dictionary is not None:
            self.from_dictionary(dictionary)

    def from_dictionary(self, dictionary: dict):
        super().from_dictionary(dictionary)
        
        self.title = dictionary.get('title')
        self.description = dictionary.get('description')
        self.start_parameter = dictionary.get('start_parameter')
        self.currency = dictionary.get('currency')
        self.total_amount = dictionary.get('total_amount')
