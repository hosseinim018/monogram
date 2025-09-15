from .baseType import BaseType
from .Chat import Chat
from .ChatBoost import ChatBoost

class ChatBoostUpdated(BaseType):
    """
    This object represents a boost added to a chat or updated.
    """
    
    def __init__(self, dictionary: dict = None):
        super().__init__(dictionary)
        
        self.chat: Chat = None  # Chat which was boosted
        self.boost: ChatBoost = None  # Information about the chat boost

        if dictionary is not None:
            self.from_dictionary(dictionary)

    def from_dictionary(self, dictionary: dict):
        super().from_dictionary(dictionary)
        
        if 'chat' in dictionary:
            self.chat = Chat(dictionary.get('chat'))
        if 'boost' in dictionary:
            self.boost = ChatBoost(dictionary.get('boost'))
