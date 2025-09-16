from typing import Optional, Dict, Any
from .baseType import BaseType
from .User import User
from .Location import Location

class InlineQuery(BaseType):
    """
    This object represents an incoming inline query. When the user sends an empty query,
    your bot could return some default or trending results.
    """
    
    def __init__(
        self,
        id: str,
        query: str,
        offset: str,
        bot: Any = None,
        chat_type: Optional[str] = None,
        location: Optional[Dict] = None,
        **kwargs: Any
    ):
        """
        Initialize an InlineQuery object that represents an incoming inline query in the Telegram Bot API.

        Args:
            id (str): Unique identifier for this query
            query (str): Text of the query (up to 256 characters)
            offset (str): Offset of the results to be returned, can be controlled by the bot
            bot (Any, optional): Bot instance handling this inline query
            chat_type (str, optional): Type of the chat from which the inline query was sent.
                                     Can be "sender", "private", "group", "supergroup", or "channel"
            location (dict, optional): Sender location information (only for bots that request user location)
            **kwargs: Additional fields that might be added in future Telegram Bot API updates
        """
        super().__init__(**kwargs)
        
        # Basic query information
        self.id = id
        self.query = query
        self.offset = offset
        self.bot = bot

        # Chat information
        self.chat_type = chat_type
        self.from_user = User(**self.from_user) if 'from_user' in self else None
        
        # Location information (optional)
        self.location = Location(**location) if location else None

        # Store any additional fields for future compatibility
        for key, value in kwargs.items():
            if not hasattr(self, key):
                setattr(self, key, value)
