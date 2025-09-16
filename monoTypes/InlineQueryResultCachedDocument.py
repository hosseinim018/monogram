from typing import Optional, List, Dict, Any, Union
from .baseType import BaseType
from .MessageEntity import MessageEntity
from .InlineKeyboardMarkup import InlineKeyboardMarkup
from .InputTextMessageContent import InputTextMessageContent

class InlineQueryResultCachedDocument(BaseType):
    """
    Represents a link to a file stored on the Telegram servers.
    By default, this file will be sent by the user with an optional caption.
    Alternatively, you can use input_message_content to send a message with the specified content instead of the file.
    """

    def __init__(
        self,
        id: str,
        title: str,
        document_file_id: str,
        description: Optional[str] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List[Dict]] = None,
        reply_markup: Optional[Union[InlineKeyboardMarkup, Dict]] = None,
        input_message_content: Optional[Union[InputTextMessageContent, Dict]] = None,
        **kwargs: Any
    ):
        """
        Initialize an InlineQueryResultCachedDocument object.

        Args:
            id (str): Unique identifier for this result, 1-64 bytes
            title (str): Title for the result
            document_file_id (str): A valid file identifier for the file
            description (str, optional): Short description of the result
            caption (str, optional): Caption of the document to be sent, 0-1024 characters after entities parsing
            parse_mode (str, optional): Mode for parsing entities in the document caption
            caption_entities (List[dict], optional): List of special entities that appear in the caption
            reply_markup (InlineKeyboardMarkup, optional): Inline keyboard attached to the message
            input_message_content (InputTextMessageContent, optional): Content of the message to be sent instead of the file
            **kwargs: Additional fields that might be added in future Telegram Bot API updates

        Raises:
            ValueError: If id length is invalid
        """
        super().__init__(**kwargs)

        # Validate id length (1-64 bytes)
        if not (1 <= len(id.encode('utf-8')) <= 64):
            raise ValueError("id must be between 1 and 64 bytes")

        # Required fields
        self.type = 'document'  # Type of the result, must be document
        self.id = id
        self.title = title
        self.document_file_id = document_file_id

        # Optional fields
        self.description = description
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = [MessageEntity(**entity) for entity in caption_entities] if caption_entities else None
        self.reply_markup = reply_markup if isinstance(reply_markup, InlineKeyboardMarkup) else \
                          InlineKeyboardMarkup(**reply_markup) if reply_markup else None
        self.input_message_content = input_message_content if isinstance(input_message_content, InputTextMessageContent) else \
                                     InputTextMessageContent(**input_message_content) if input_message_content else None

        # Store any additional fields for future compatibility
        for key, value in kwargs.items():
            if not hasattr(self, key):
                setattr(self, key, value)

    def __str__(self) -> str:
        """
        Get a string representation of the inline query result cached document.

        Returns:
            str: A string containing the title and description (if available)
        """
        result = f"Cached Document: {self.title}"
        if self.description:
            result += f" - {self.description[:50]}..."
        return result