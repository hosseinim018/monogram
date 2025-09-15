from typing import List
from .baseType import BaseType
from .Chat import Chat
from .ReactionType import ReactionType

class MessageReactionCountUpdated(BaseType):
    """
    This object represents reaction changes on a message with anonymous reactions.
    """
    
    def __init__(self, dictionary: dict = None):
        super().__init__(dictionary)
        
        self.chat: Chat = None  # Chat containing the message
        self.message_id: int = None  # Message identifier
        self.date: int = None  # Date of the change in Unix time
        self.reactions: List[dict] = []  # List of reactions that are present on the message

        if dictionary is not None:
            self.from_dictionary(dictionary)

    def from_dictionary(self, dictionary: dict):
        super().from_dictionary(dictionary)
        
        if 'chat' in dictionary:
            self.chat = Chat(dictionary.get('chat'))
        self.message_id = dictionary.get('message_id')
        self.date = dictionary.get('date')
        if 'reactions' in dictionary:
            self.reactions = [
                {
                    'type': ReactionType(reaction.get('type')),
                    'total_count': reaction.get('total_count')
                }
                for reaction in dictionary.get('reactions', [])
            ]
