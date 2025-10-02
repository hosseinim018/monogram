from typing import Optional, Dict, Any, Union
from .baseType import BaseType
from .InputTextMessageContent import InputTextMessageContent
from .InlineKeyboardMarkup import InlineKeyboardMarkup
from monogram.text import format_text

def _prepare_payload(raw_payload):
    """
    Prepares a payload dictionary for Telegram API requests.
    Removes None values and formats text/caption fields.

    Args:
        raw_payload: The dictionary of parameters for the API method.

    Returns:
        A cleaned and formatted payload dictionary.
    """
    if raw_payload:
        # Remove None values from payload
        payload = {k: v for k, v in raw_payload.items() if v is not None}

        if 'self' in payload:
            payload.pop('self')
        if 'cls' in payload:
            payload.pop('cls')
        if 'kwargs' in payload:
            payload.pop('kwargs')
        if 'args' in payload:
            payload.pop('args')
        # Apply text formatting if 'text' or 'caption' keys exist
        if 'text' in payload and payload['text'] is not None:
            payload['text'] = format_text(payload['text'])
        if 'caption' in payload and payload['caption'] is not None:
            payload['caption'] = format_text(payload['caption'])
            
        return payload
    return {}

class InlineQueryResultArticle(BaseType):
    """
    Represents a link to an article or web page.
    """

    def __new__(
        cls,
        id: str,
        title: str,
        input_message_content: Dict,
        reply_markup: Optional[Union[InlineKeyboardMarkup, Dict]] = None,
        url: Optional[str] = None,
        description: Optional[str] = None,
        thumbnail_url: Optional[str] = None,
        thumbnail_width: Optional[int] = None,
        thumbnail_height: Optional[int] = None,
        *args: Any,
        **kwargs: Any
    ) -> dict:
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
        
        # # Validate id length (1-64 bytes)
        # if not (1 <= len(id.encode('utf-8')) <= 64):
        #     raise ValueError("id must be between 1 and 64 bytes")

        # Required fields
        # cls.type = "article"  # Type of the result, must be article
        # cls.id = id
        # cls.title = title
        
        # # # Handle input message content
        # if isinstance(input_message_content, dict):
        #     cls.input_message_content = InputTextMessageContent(**input_message_content)
        # elif isinstance(input_message_content, InputTextMessageContent):
        #     cls.input_message_content = input_message_content
        # else:
        #     raise ValueError("input_message_content must be either a dict or InputTextMessageContent instance")

        # # Optional fields
        # cls.reply_markup = reply_markup if isinstance(reply_markup, InlineKeyboardMarkup) else \
        #                   InlineKeyboardMarkup(**reply_markup) if reply_markup else None
        # cls.url = url
        # cls.description = description
        # cls.thumbnail_url = thumbnail_url
        # cls.thumbnail_width = thumbnail_width
        # cls.thumbnail_height = thumbnail_height

        # # Store any additional fields for future compatibility
        # for key, value in kwargs.items():
        #     if not hasattr(cls, key):
        #         setattr(cls, key, value)

        payload = _prepare_payload(raw_payload=locals().copy())
        payload['type']= 'article'
        return payload
    
    # def __str__(cls) -> str:
    #     """
    #     Get a string representation of the inline query result article.

    #     Returns:
    #         str: A string containing the title and description (if available)
    #     """
    #     result = f"Article: {cls.title}"
    #     if cls.description:
    #         result += f" - {cls.description[:50]}..."
    #     return result
