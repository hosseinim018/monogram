from monogram.monoTypes.baseType import BaseType

class InlineQueryResultGame(BaseType):
    """
    Represents a game.

    Attributes:
        type (str): Type of the result, must be 'game'.
        id (str): Unique identifier for this result, 1-64 bytes.
        game_short_name (str): Short name of the game.
    """

    def __init__(self, id: str, game_short_name: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'game'
        self.id = id
        self.game_short_name = game_short_name
        
        if not self.id:
            raise ValueError("id is required")
        if not self.game_short_name:
            raise ValueError("game_short_name is required")
