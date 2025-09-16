from monogram.monoTypes.baseType import BaseType
from monogram.monoTypes.InlineKeyboardMarkup import InlineKeyboardMarkup
from monogram.monoTypes.InputTextMessageContent import InputTextMessageContent
from monogram.monoTypes.MessageEntity import MessageEntity
from typing import Optional, List, Dict, Any

class InlineQueryResultCachedVideo(BaseType):
    """
    Represents a link to a video file stored on the Telegram servers.
    """

    def __init__(
        self,
        id: str,
        video_file_id: str,
        title: str,
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
        self.type = 'video'
        self.id = id
        self.video_file_id = video_file_id
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
        if not self.video_file_id:
            raise ValueError("video_file_id is required")
        if not self.title:
            raise ValueError("title is required")