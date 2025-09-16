from monogram.monoTypes.baseType import BaseType
from monogram.monoTypes.InlineKeyboardMarkup import InlineKeyboardMarkup
from monogram.monoTypes.InputTextMessageContent import InputTextMessageContent
from typing import Optional, Any

class InlineQueryResultCachedSticker(BaseType):
    """
    Represents a link to a sticker stored on the Telegram servers.
    """

    def __init__(
        self,
        id: str,
        sticker_file_id: str,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
        input_message_content: Optional[InputTextMessageContent] = None,
        *args,
        **kwargs: Any
    ):
        super().__init__(*args, **kwargs)
        self.type = 'sticker'
        self.id = id
        self.sticker_file_id = sticker_file_id
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content

    def validate(self):
        if not self.id:
            raise ValueError("id is required")
        if not self.sticker_file_id:
            raise ValueError("sticker_file_id is required")