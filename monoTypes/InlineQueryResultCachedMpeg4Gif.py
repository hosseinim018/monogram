from typing import Optional, Dict, Any, Union, List
from .baseType import BaseType
from .InputTextMessageContent import InputTextMessageContent
from .InlineKeyboardMarkup import InlineKeyboardMarkup
from .MessageEntity import MessageEntity

class InlineQueryResultCachedMpeg4Gif(BaseType):
    """
    Represents a link to a video animation (H.264/MPEG-4 AVC video without sound) stored on the Telegram servers.
    By default, this animated MPEG-4 file will be sent by the user with an optional caption.
    Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.
    """

    def __init__(
        self,
        id: str,
        mpeg4_file_id: str,
        title: Optional[str] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List[Dict]] = None,
        show_caption_above_media: Optional[bool] = None,
        reply_markup: Optional[Union[InlineKeyboardMarkup, Dict]] = None,
        input_message_content: Optional[Union[InputTextMessageContent, Dict]] = None,
        **kwargs: Any
    ):
        """
        Initialize an InlineQueryResultCachedMpeg4Gif object.

        Args:
            id (str): Unique identifier for this result, 1-64 bytes.
            mpeg4_file_id (str): A valid file identifier for the MPEG4 file.
            title (str, optional): Title for the result.
            caption (str, optional): Caption of the MPEG-4 file to be sent, 0-1024 characters after entities parsing.
            parse_mode (str, optional): Mode for parsing entities in the caption.
            caption_entities (List[dict], optional): List of special entities that appear in the caption.
            show_caption_above_media (bool, optional): Pass True, if the caption must be shown above the message media.
            reply_markup (Union[InlineKeyboardMarkup, dict], optional): Inline keyboard attached to the message.
            input_message_content (Union[InputTextMessageContent, dict], optional): Content of the message to be sent instead of the video animation.
            **kwargs: Additional fields for future compatibility.

        Raises:
            ValueError: If id length is invalid.
        """
        super().__init__(**kwargs)

        # Validate id length (1-64 bytes)
        if not (1 <= len(id.encode('utf-8')) <= 64):
            raise ValueError("id must be between 1 and 64 bytes")

        # Required fields
        self.type = 'mpeg4_gif'  # Type of the result, must be mpeg4_gif
        self.id = id
        self.mpeg4_file_id = mpeg4_file_id

        # Optional fields
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = [MessageEntity(**entity) for entity in caption_entities] if caption_entities else None
        self.show_caption_above_media = show_caption_above_media
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
        Get a string representation of the InlineQueryResultCachedMpeg4Gif.

        Returns:
            str: A string containing the title and caption (if available).
        """
        result = f"Cached MPEG4 GIF: {self.title or self.id}"
        if self.caption:
            result += f" - {self.caption[:50]}..."
        return result