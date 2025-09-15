from .baseType import BaseType
from typing import Optional

class ReactionType(BaseType):
    """
    This object describes the type of a reaction.
    """
    
    def __init__(self, dictionary: dict = None):
        super().__init__(dictionary)
        
        self.type: str = None  # Type of reaction ("emoji" or "custom_emoji")
        self.emoji: Optional[str] = None  # Optional. Emoji reaction
        self.custom_emoji_id: Optional[str] = None  # Optional. Custom emoji identifier

        if dictionary is not None:
            self.from_dictionary(dictionary)

    def from_dictionary(self, dictionary: dict):
        super().from_dictionary(dictionary)
        
        self.type = dictionary.get('type')
        self.emoji = dictionary.get('emoji')
        self.custom_emoji_id = dictionary.get('custom_emoji_id')
