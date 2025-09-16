from monogram.monoTypes.baseType import BaseType
from monogram.monoTypes.InlineKeyboardMarkup import InlineKeyboardMarkup
from monogram.monoTypes.InputTextMessageContent import InputTextMessageContent
from monogram.monoTypes.MessageEntity import MessageEntity

class InlineQueryResultAudio(BaseType):
    """
    Represents a link to an MP3 audio file. By default, this audio file will be sent by the user.
    Alternatively, you can use input_message_content to send a message with the specified content
    instead of the audio.
    
    Attributes:
        type (str): Type of the result, must be 'audio'.
        id (str): Unique identifier for this result, 1-64 bytes.
        audio_url (str): A valid URL for the audio file.
        title (str): Title of the audio.
        caption (str, optional): Caption, 0-1024 characters after entities parsing.
        parse_mode (str, optional): Mode for parsing entities in the caption.
        caption_entities (list[MessageEntity], optional): List of special entities that appear in the caption.
        performer (str, optional): Performer of the audio.
        audio_duration (int, optional): Audio duration in seconds.
        reply_markup (InlineKeyboardMarkup, optional): Inline keyboard attached to the message.
        input_message_content (InputTextMessageContent, optional): Content of the message to be sent instead of the audio.
    """

    def __init__(self, *, id, audio_url, title, caption=None, parse_mode=None, caption_entities=None, performer=None,
                 audio_duration=None, reply_markup=None, input_message_content=None, **kwargs):
        super().__init__(**kwargs)
        self.type = 'audio'
        self.id = id
        self.audio_url = audio_url
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.performer = performer
        self.audio_duration = audio_duration
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content

    @staticmethod
    def validate_fields(data):
        """Validates the required fields for InlineQueryResultAudio."""
        required_fields = ['id', 'audio_url', 'title']
        for field in required_fields:
            if field not in data or not data[field]:
                raise ValueError(f"Field {field} is required and cannot be empty.")

        if 'type' in data and data['type'] != 'audio':
            raise ValueError("Field 'type' must be 'audio'.")

        return True