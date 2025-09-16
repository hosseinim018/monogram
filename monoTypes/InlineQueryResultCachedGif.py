from monogram.monoTypes.baseType import BaseType
from monogram.monoTypes.InlineKeyboardMarkup import InlineKeyboardMarkup
from monogram.monoTypes.InputTextMessageContent import InputTextMessageContent

class InlineQueryResultCachedGif(BaseType):
    """
    Represents a link to an animated GIF file stored on the Telegram servers. By default, this animated GIF file will
    be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message
    with specified content instead of the animation.

    Attributes:
        type (str): Type of the result, must be 'gif'.
        id (str): Unique identifier for this result, 1-64 bytes.
        gif_file_id (str): A valid file identifier for the GIF file.
        title (str, optional): Title for the result.
        caption (str, optional): Caption of the GIF file to be sent, 0-1024 characters after entities parsing.
        parse_mode (str, optional): Mode for parsing entities in the caption.
        caption_entities (list[MessageEntity], optional): List of special entities that appear in the caption.
        show_caption_above_media (bool, optional): Pass True, if the caption must be shown above the message media.
        reply_markup (InlineKeyboardMarkup, optional): Inline keyboard attached to the message.
        input_message_content (InputTextMessageContent, optional): Content of the message to be sent instead of the GIF animation.
    """

    def __init__(self, *, id, gif_file_id, title=None, caption=None, parse_mode=None, caption_entities=None,
                 show_caption_above_media=None, reply_markup=None, input_message_content=None, **kwargs):
        super().__init__(**kwargs)
        self.type = 'gif'
        self.id = id
        self.gif_file_id = gif_file_id
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content

    @staticmethod
    def validate_fields(data):
        """Validates the required fields for InlineQueryResultCachedGif."""
        required_fields = ['id', 'gif_file_id']
        for field in required_fields:
            if field not in data or not data[field]:
                raise ValueError(f"Field {field} is required and cannot be empty.")

        if 'type' in data and data['type'] != 'gif':
            raise ValueError("Field 'type' must be 'gif'.")

        return True