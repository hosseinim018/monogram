from .baseType import BaseType

class BusinessConnection(BaseType):
    """
    This object represents a business connection with a user or a bot.
    """
    
    def __init__(self, dictionary: dict = None):
        super().__init__(dictionary)
        
        self.business_connection_id: str = None  # Unique identifier for the business connection
        self.status: str = None  # Status of the connection
        self.is_active: bool = None  # Whether the connection is currently active
        self.expiration_date: int = None  # Optional. Date when connection expires, unix time
        self.metadata: dict = None  # Optional. Additional business connection metadata

        if dictionary is not None:
            self.from_dictionary(dictionary)

    def from_dictionary(self, dictionary: dict):
        super().from_dictionary(dictionary)
        
        self.business_connection_id = dictionary.get('business_connection_id')
        self.status = dictionary.get('status')
        self.is_active = dictionary.get('is_active')
        self.expiration_date = dictionary.get('expiration_date')
        self.metadata = dictionary.get('metadata')
