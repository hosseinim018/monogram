from typing import List, Optional
from .baseType import BaseType
from .MessageEntity import MessageEntity

class ReplyParameters(BaseType):
    def __init__(self, dictionary: dict = None):
        super().__init__(dictionary)
        
        # Required field
        self.message_id: int = None
        
        # Optional fields
        self.chat_id: int = None
        self.allow_sending_without_reply: bool = None
        self.quote: str = None
        self.quote_parse_mode: str = None
        self.quote_entities: List[MessageEntity] = []
        self.quote_position: int = None

        if dictionary is not None:
            self.from_dictionary(dictionary)

    def from_dictionary(self, dictionary: dict):
        super().from_dictionary(dictionary)
        
        self.message_id = dictionary.get('message_id')
        self.chat_id = dictionary.get('chat_id')
        self.allow_sending_without_reply = dictionary.get('allow_sending_without_reply')
        self.quote = dictionary.get('quote')
        self.quote_parse_mode = dictionary.get('quote_parse_mode')
        
        if 'quote_entities' in dictionary:
            self.quote_entities = [MessageEntity(entity) for entity in dictionary.get('quote_entities', [])]
            
        self.quote_position = dictionary.get('quote_position')
