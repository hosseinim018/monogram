from .baseType import BaseType
from .User import User

class ChatBoost(BaseType):
    """
    This object contains information about a chat boost.
    """
    
    def __init__(self, dictionary: dict = None):
        super().__init__(dictionary)
        
        self.boost_id: str = None  # Unique identifier of the boost
        self.add_date: int = None  # Point in time when the boost was added
        self.expiration_date: int = None  # Point in time when the boost will expire
        self.source: dict = None  # Source of the added boost
        self.boost_count: int = None  # Number of boost slots added by this boost

        if dictionary is not None:
            self.from_dictionary(dictionary)

    def from_dictionary(self, dictionary: dict):
        super().from_dictionary(dictionary)
        
        self.boost_id = dictionary.get('boost_id')
        self.add_date = dictionary.get('add_date')
        self.expiration_date = dictionary.get('expiration_date')
        self.source = dictionary.get('source')
        self.boost_count = dictionary.get('boost_count')
