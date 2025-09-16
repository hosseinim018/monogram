from typing import Optional, Dict, Any, Union
from .baseType import BaseType
from .InputTextMessageContent import InputTextMessageContent
from .InlineKeyboardMarkup import InlineKeyboardMarkup

class InlineQueryResultArticle(BaseType):
    """
    Represents a link to an article or web page.
    """

    def __init__(
        self,
        id: str,
        title: str,
        input_message_content: Dict,
        reply_markup: Optional[Union[InlineKeyboardMarkup, Dict]] = None,
        url: Optional[str] = None,
        description: Optional[str] = None,
        thumbnail_url: Optional[str] = None,
        thumbnail_width: Optional[int] = None,
        thumbnail_height: Optional[int] = None,
        **kwargs: Any
    ):
        """
        Initialize an InlineQueryResultArticle object that represents a link to an article or web page.

        Args:
            id (str): Unique identifier for this result, 1-64 Bytes
            title (str): Title of the result
            input_message_content (dict): Content of the message to be sent
            reply_markup (Union[InlineKeyboardMarkup, dict], optional): Inline keyboard attached to the message
            url (str, optional): URL of the result
            description (str, optional): Short description of the result
            thumbnail_url (str, optional): Url of the thumbnail for the result
            thumbnail_width (int, optional): Thumbnail width
            thumbnail_height (int, optional): Thumbnail height
            **kwargs: Additional fields that might be added in future Telegram Bot API updates

        Raises:
            ValueError: If id length is invalid
        """
        super().__init__(**kwargs)
        
        # Validate id length (1-64 bytes)
        if not (1 <= len(id.encode('utf-8')) <= 64):
            raise ValueError("id must be between 1 and 64 bytes")

        # Required fields
        self.type = 'article'  # Type of the result, must be article
        self.id = id
        self.title = title
        
        # Handle input message content
        if isinstance(input_message_content, dict):
            self.input_message_content = InputTextMessageContent(**input_message_content)
        elif isinstance(input_message_content, InputTextMessageContent):
            self.input_message_content = input_message_content
        else:
            raise ValueError("input_message_content must be either a dict or InputTextMessageContent instance")

        # Optional fields
        self.reply_markup = reply_markup if isinstance(reply_markup, InlineKeyboardMarkup) else \
                          InlineKeyboardMarkup(**reply_markup) if reply_markup else None
        self.url = url
        self.description = description
        self.thumbnail_url = thumbnail_url
        self.thumbnail_width = thumbnail_width
        self.thumbnail_height = thumbnail_height

        # Store any additional fields for future compatibility
        for key, value in kwargs.items():
            if not hasattr(self, key):
                setattr(self, key, value)

    def __str__(self) -> str:
        """
        Get a string representation of the inline query result article.

        Returns:
            str: A string containing the title and description (if available)
        """
        result = f"Article: {self.title}"
        if self.description:
            result += f" - {self.description[:50]}..."
        return result
