from typing import List
from .baseType import BaseType
from .Chat import Chat

class BusinessMessagesDeleted(BaseType):
    """
    This object represents a notification about deleted business messages.
    """
    
    def __init__(self, dictionary: dict = None):
        super().__init__(dictionary)
        
        self.business_connection_id: str = None  # Unique identifier of the business connection
        self.chat: Chat = None  # Chat where messages were deleted
        self.message_ids: List[int] = []  # List of deleted message identifiers

        if dictionary is not None:
            self.from_dictionary(dictionary)

    def from_dictionary(self, dictionary: dict):
        super().from_dictionary(dictionary)
        
        self.business_connection_id = dictionary.get('business_connection_id')
        if 'chat' in dictionary:
            self.chat = Chat(dictionary.get('chat'))
        self.message_ids = dictionary.get('message_ids', [])
