from typing import Optional, Dict, Any, List, Union
from .baseType import BaseType
from .MessageEntity import MessageEntity
from .InlineKeyboardMarkup import InlineKeyboardMarkup
from .InputTextMessageContent import InputTextMessageContent

class InlineQueryResultPhoto(BaseType):
    """
    Represents a link to a photo.
    """

    def __init__(
        self,
        id: str,
        photo_url: str,
        thumbnail_url: str,
        photo_width: Optional[int] = None,
        photo_height: Optional[int] = None,
        title: Optional[str] = None,
        description: Optional[str] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List[Dict]] = None,
        show_caption_above_media: Optional[bool] = None,
        reply_markup: Optional[Union[InlineKeyboardMarkup, Dict]] = None,
        input_message_content: Optional[Dict] = None,
        **kwargs: Any
    ):
        super().__init__(**kwargs)

        self.type = 'photo'
        self.id = id
        self.photo_url = photo_url
        self.thumbnail_url = thumbnail_url
        self.photo_width = photo_width
        self.photo_height = photo_height
        self.title = title
        self.description = description
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
        return f"Photo: {self.title or self.id}"