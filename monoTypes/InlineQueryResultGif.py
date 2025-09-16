from typing import Optional, Dict, Any, List, Union
from .baseType import BaseType
from .MessageEntity import MessageEntity
from .InlineKeyboardMarkup import InlineKeyboardMarkup
from .InputTextMessageContent import InputTextMessageContent

class InlineQueryResultGif(BaseType):
    """
    Represents a link to an animated GIF file.
    """

    def __init__(
        self,
        id: str,
        gif_url: str,
        gif_width: Optional[int] = None,
        gif_height: Optional[int] = None,
        gif_duration: Optional[int] = None,
        thumbnail_url: Optional[str] = None,
        thumbnail_mime_type: Optional[str] = None,
        title: Optional[str] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List[Dict]] = None,
        show_caption_above_media: Optional[bool] = None,
        reply_markup: Optional[Union[InlineKeyboardMarkup, Dict]] = None,
        input_message_content: Optional[Dict] = None,
        **kwargs: Any
    ):
        super().__init__(**kwargs)

        self.type = 'gif'
        self.id = id
        self.gif_url = gif_url
        self.gif_width = gif_width
        self.gif_height = gif_height
        self.gif_duration = gif_duration
        self.thumbnail_url = thumbnail_url
        self.thumbnail_mime_type = thumbnail_mime_type
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = [MessageEntity(**e) for e in caption_entities] if caption_entities else None
        self.show_caption_above_media = show_caption_above_media

        if isinstance(reply_markup, InlineKeyboardMarkup):
            self.reply_markup = reply_markup
        elif isinstance(reply_markup, dict):
            self.reply_markup = InlineKeyboardMarkup(**reply_markup)
        else:
            self.reply_markup = None

        if isinstance(input_message_content, dict):
            self.input_message_content = InputTextMessageContent(**input_message_content)
        elif isinstance(input_message_content, InputTextMessageContent):
            self.input_message_content = input_message_content
        else:
            self.input_message_content = None

        for key, value in kwargs.items():
            if not hasattr(self, key):
                setattr(self, key, value)

    def __str__(self):
        return f"GIF: {self.title or self.id}"