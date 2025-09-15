from typing import Optional
from .baseType import BaseType
from .User import User
from .Location import Location

class InlineQuery(BaseType):
    """
    This object represents an incoming inline query.
    """
    
    def __init__(self, dictionary: dict = None):
        super().__init__(dictionary)
        
        self.id: str = None  # Unique identifier for this query
        self.from_user: User = None  # Sender
        self.query: str = None  # Text of the query (up to 256 characters)
        self.offset: str = None  # Offset of the results to be returned
        self.chat_type: Optional[str] = None  # Optional. Type of the chat from which the inline query was sent
        self.location: Optional[Location] = None  # Optional. Sender location, only for bots that request user location

        if dictionary is not None:
            self.from_user = dictionary.get('from')  # 'from' is a reserved word in Python
            self.from_dictionary(dictionary)

    def from_dictionary(self, dictionary: dict):
        super().from_dictionary(dictionary)
        
        self.id = dictionary.get('id')
        if 'from' in dictionary:
            self.from_user = User(dictionary.get('from'))
        self.query = dictionary.get('query')
        self.offset = dictionary.get('offset')
        self.chat_type = dictionary.get('chat_type')
        if 'location' in dictionary:
            self.location = Location(dictionary.get('location'))
