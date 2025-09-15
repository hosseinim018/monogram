from .baseType import BaseType

class CallbackGame(BaseType):
    """
    A placeholder, currently holds no information. Use BotFather to set up your game.
    https://core.telegram.org/bots/api#callbackgame
    """
    
    def __init__(self, dictionary: dict = None):
        super().__init__(dictionary)
        # Currently holds no information
        pass

    def from_dictionary(self, dictionary: dict):
        super().from_dictionary(dictionary)
        # Currently holds no information
        pass
