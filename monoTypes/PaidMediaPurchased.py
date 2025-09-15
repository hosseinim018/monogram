from .baseType import BaseType

class PaidMediaPurchased(BaseType):
    """
    This object represents a purchased media subscription.
    """
    
    def __init__(self, dictionary: dict = None):
        super().__init__(dictionary)
        
        self.telegram_payment_charge_id: str = None  # Telegram payment identifier
        self.provider_payment_charge_id: str = None  # Provider payment identifier
        self.media_type: str = None  # Type of the purchased media ("article", "video", etc.)
        self.media_id: str = None  # Identifier of the purchased media content
        self.amount: int = None  # Amount paid in the smallest units of the currency
        self.currency: str = None  # Three-letter ISO 4217 currency code

        if dictionary is not None:
            self.from_dictionary(dictionary)

    def from_dictionary(self, dictionary: dict):
        super().from_dictionary(dictionary)
        
        self.telegram_payment_charge_id = dictionary.get('telegram_payment_charge_id')
        self.provider_payment_charge_id = dictionary.get('provider_payment_charge_id')
        self.media_type = dictionary.get('media_type')
        self.media_id = dictionary.get('media_id')
        self.amount = dictionary.get('amount')
        self.currency = dictionary.get('currency')
