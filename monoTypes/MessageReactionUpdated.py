from typing import List
from .baseType import BaseType
from .Chat import Chat
from .User import User
from .ReactionType import ReactionType

class MessageReactionUpdated(BaseType):
    """
    This object represents a change of a reaction on a message.
    """
    
    def __init__(self, dictionary: dict = None):
        super().__init__(dictionary)
        
        self.chat: Chat = None  # Chat containing the message
        self.message_id: int = None  # Message identifier
        self.user: User = None  # User that changed the reaction
        self.actor_chat: Chat = None  # Optional. Chat that changed the reaction, if the reaction was changed by an anonymous chat administrator
        self.date: int = None  # Date of the change in Unix time
        self.old_reaction: List[ReactionType] = []  # Previous list of reaction types
        self.new_reaction: List[ReactionType] = []  # New list of reaction types

        if dictionary is not None:
            self.from_dictionary(dictionary)

    def from_dictionary(self, dictionary: dict):
        super().from_dictionary(dictionary)
        
        if 'chat' in dictionary:
            self.chat = Chat(dictionary.get('chat'))
        self.message_id = dictionary.get('message_id')
        if 'user' in dictionary:
            self.user = User(dictionary.get('user'))
        if 'actor_chat' in dictionary:
            self.actor_chat = Chat(dictionary.get('actor_chat'))
        self.date = dictionary.get('date')
        if 'old_reaction' in dictionary:
            self.old_reaction = [ReactionType(reaction) for reaction in dictionary.get('old_reaction', [])]
        if 'new_reaction' in dictionary:
            self.new_reaction = [ReactionType(reaction) for reaction in dictionary.get('new_reaction', [])]
