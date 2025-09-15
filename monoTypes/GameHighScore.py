from .baseType import BaseType
from .User import User

class GameHighScore(BaseType):
    """
    This object represents one row of the high scores table for a game.
    https://core.telegram.org/bots/api#gamehighscore
    """
    
    def __init__(self, dictionary: dict = None):
        super().__init__(dictionary)
        
        self.position: int = None  # Position in high score table
        self.user: User = None  # User who scored
        self.score: int = None  # Score value

        if dictionary is not None:
            self.from_dictionary(dictionary)

    def from_dictionary(self, dictionary: dict):
        super().from_dictionary(dictionary)
        
        self.position = dictionary.get('position')
        if 'user' in dictionary:
            self.user = User(dictionary.get('user'))
        self.score = dictionary.get('score')
