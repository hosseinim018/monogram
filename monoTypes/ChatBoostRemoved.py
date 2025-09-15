from .baseType import BaseType
from .Chat import Chat

class ChatBoostRemoved(BaseType):
    """
    This object represents a boost removed from a chat.
    """
    
    def __init__(self, dictionary: dict = None):
        super().__init__(dictionary)
        
        self.chat: Chat = None  # Chat which was boosted
        self.boost_id: str = None  # Unique identifier of the boost
        self.remove_date: int = None  # Point in time when the boost was removed
        self.source: dict = None  # Source of the removed boost

        if dictionary is not None:
            self.from_dictionary(dictionary)

    def from_dictionary(self, dictionary: dict):
        super().from_dictionary(dictionary)
        
        if 'chat' in dictionary:
            self.chat = Chat(dictionary.get('chat'))
        self.boost_id = dictionary.get('boost_id')
        self.remove_date = dictionary.get('remove_date')
        self.source = dictionary.get('source')
