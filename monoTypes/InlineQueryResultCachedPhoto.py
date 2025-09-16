from monogram.monoTypes.baseType import BaseType
from monogram.monoTypes.InlineKeyboardMarkup import InlineKeyboardMarkup
from monogram.monoTypes.InputTextMessageContent import InputTextMessageContent
from monogram.monoTypes.MessageEntity import MessageEntity
from typing import Optional, List, Dict, Any

class InlineQueryResultCachedPhoto(BaseType):
    """
    Represents a link to a photo stored on the Telegram servers.
    """

    def __init__(
        self,
        id: str,
        photo_file_id: str,
        title: Optional[str] = None,
        description: Optional[str] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List[Dict]] = None,
        show_caption_above_media: Optional[bool] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
        input_message_content: Optional[InputTextMessageContent] = None,
        *args,
        **kwargs: Any
    ):
        super().__init__(*args, **kwargs)
        self.type = 'photo'
        self.id = id
        self.photo_file_id = photo_file_id
        self.title = title
        self.description = description
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = [MessageEntity(**entity) for entity in caption_entities] if caption_entities else None
        self.show_caption_above_media = show_caption_above_media
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content

    def validate(self):
        if not self.id:
            raise ValueError("id is required")
        if not self.photo_file_id:
            raise ValueError("photo_file_id is required")