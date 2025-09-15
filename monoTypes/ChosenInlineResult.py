from typing import Optional
from .baseType import BaseType
from .User import User
from .Location import Location

class ChosenInlineResult(BaseType):
    """
    This object represents a result of an inline query that was chosen by the user and sent to their chat partner.
    """
    
    def __init__(self, dictionary: dict = None):
        super().__init__(dictionary)
        
        self.result_id: str = None  # Unique identifier for the result that was chosen
        self.from_user: User = None  # User that chose the result
        self.location: Optional[Location] = None  # Optional. Sender location, only for bots that require user location
        self.inline_message_id: Optional[str] = None  # Optional. Identifier of the sent inline message
        self.query: str = None  # The query that was used to obtain the result

        if dictionary is not None:
            self.from_user = dictionary.get('from')  # 'from' is a reserved word in Python
            self.from_dictionary(dictionary)

    def from_dictionary(self, dictionary: dict):
        super().from_dictionary(dictionary)
        
        self.result_id = dictionary.get('result_id')
        if 'from' in dictionary:
            self.from_user = User(dictionary.get('from'))
        if 'location' in dictionary:
            self.location = Location(dictionary.get('location'))
        self.inline_message_id = dictionary.get('inline_message_id')
        self.query = dictionary.get('query')
