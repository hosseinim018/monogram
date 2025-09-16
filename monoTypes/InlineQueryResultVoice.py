from monogram.monoTypes.baseType import BaseType
from monogram.monoTypes.InlineKeyboardMarkup import InlineKeyboardMarkup
from monogram.monoTypes.InputTextMessageContent import InputTextMessageContent
from monogram.monoTypes.MessageEntity import MessageEntity

class InlineQueryResultVoice(BaseType):
    """
    Represents a link to a voice recording in an .OGG container encoded with OPUS. By default, this voice recording
    will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified
    content instead of the voice message.

    Attributes:
        type (str): Type of the result, must be 'voice'.
        id (str): Unique identifier for this result, 1-64 bytes.
        voice_url (str): A valid URL for the voice recording.
        title (str): Recording title.
        caption (str, optional): Caption, 0-1024 characters after entities parsing.
        parse_mode (str, optional): Mode for parsing entities in the voice message caption.
        caption_entities (list[MessageEntity], optional): List of special entities that appear in the caption.
        voice_duration (int, optional): Recording duration in seconds.
        reply_markup (InlineKeyboardMarkup, optional): Inline keyboard attached to the message.
        input_message_content (InputTextMessageContent, optional): Content of the message to be sent instead of the voice recording.
    """

    def __init__(self, *, id, voice_url, title, caption=None, parse_mode=None, caption_entities=None, voice_duration=None,
                 reply_markup=None, input_message_content=None, **kwargs):
        super().__init__(**kwargs)
        self.type = 'voice'
        self.id = id
        self.voice_url = voice_url
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.voice_duration = voice_duration
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content

    @staticmethod
    def validate_fields(data):
        """Validates the required fields for InlineQueryResultVoice."""
        required_fields = ['id', 'voice_url', 'title']
        for field in required_fields:
            if field not in data or not data[field]:
                raise ValueError(f"Field {field} is required and cannot be empty.")

        if 'type' in data and data['type'] != 'voice':
            raise ValueError("Field 'type' must be 'voice'.")

        return True