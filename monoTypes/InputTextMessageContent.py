from typing import Optional, List, Dict, Union, Any
from .baseType import BaseType
from .MessageEntity import MessageEntity

class InputTextMessageContent(BaseType):
    """
    Represents the content of a text message to be sent as the result of an inline query.
    """

    def __init__(
        self,
        message_text: str,
        parse_mode: Optional[str] = None,
        entities: Optional[List[Dict]] = None,
        link_preview_options: Optional[Dict] = None,
        **kwargs: Any
    ):
        """
        Initialize an InputTextMessageContent object that represents text content for an inline query result.

        Args:
            message_text (str): Text of the message to be sent, 1-4096 characters
            parse_mode (str, optional): Mode for parsing entities in the message text.
                                     Can be 'HTML', 'Markdown', or 'MarkdownV2'
            entities (List[dict], optional): List of special entities that appear in message text,
                                         which can be specified instead of parse_mode
            link_preview_options (dict, optional): Link preview generation options for the message
            **kwargs: Additional fields that might be added in future Telegram Bot API updates

        Raises:
            ValueError: If message_text length is invalid or if parse_mode and entities are used together
        """
        super().__init__(**kwargs)

        # Validate message_text length
        if not (1 <= len(message_text) <= 4096):
            raise ValueError("message_text must be between 1 and 4096 characters")

        # Validate parse_mode and entities mutual exclusivity
        if parse_mode and entities:
            raise ValueError("parse_mode and entities cannot be used together")

        # Required field
        self.message_text = message_text

        # Optional fields with proper type conversion
        self.parse_mode = parse_mode
        self.entities = [MessageEntity(**entity) for entity in entities] if entities else None
        self.link_preview_options = link_preview_options

        # Store any additional fields for future compatibility
        for key, value in kwargs.items():
            if not hasattr(self, key):
                setattr(self, key, value)

    def __str__(self) -> str:
        """
        Get a string representation of the input text message content.

        Returns:
            str: A preview of the message text (truncated if too long)
        """
        preview = self.message_text[:50] + ('...' if len(self.message_text) > 50 else '')
        return f"Text Message: {preview}"
