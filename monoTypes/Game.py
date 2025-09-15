from typing import List, Optional
from .baseType import BaseType
from .PhotoSize import PhotoSize
from .MessageEntity import MessageEntity
from .Animation import Animation

class Game(BaseType):
    """
    This object represents a game. Use BotFather to create and edit games, 
    their short names will act as unique identifiers.
    https://core.telegram.org/bots/api#game
    """
    
    def __init__(self, dictionary: dict = None):
        super().__init__(dictionary)
        
        # Required fields
        self.title: str = None  # Title of the game
        self.description: str = None  # Description of the game
        self.photo: List[PhotoSize] = []  # Photo displayed in game message
        
        # Optional fields
        self.text: Optional[str] = None  # Brief description or high scores
        self.text_entities: Optional[List[MessageEntity]] = None  # Special entities in text
        self.animation: Optional[Animation] = None  # Animation in game message

        if dictionary is not None:
            self.from_dictionary(dictionary)

    def from_dictionary(self, dictionary: dict):
        super().from_dictionary(dictionary)
        
        self.title = dictionary.get('title')
        self.description = dictionary.get('description')
        
        if 'photo' in dictionary:
            self.photo = [PhotoSize(size) for size in dictionary.get('photo', [])]
            
        self.text = dictionary.get('text')
        
        if 'text_entities' in dictionary:
            self.text_entities = [MessageEntity(entity) for entity in dictionary.get('text_entities', [])]
            
        if 'animation' in dictionary:
            self.animation = Animation(dictionary.get('animation'))
