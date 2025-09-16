from monogram.monoTypes.baseType import BaseType
from monogram.monoTypes.InlineKeyboardMarkup import InlineKeyboardMarkup
from monogram.monoTypes.InputTextMessageContent import InputTextMessageContent
from monogram.monoTypes.MessageEntity import MessageEntity

class InlineQueryResultDocument(BaseType):
    """
    Represents a link to a file. By default, this file will be sent by the user with an optional caption.
    Alternatively, you can use input_message_content to send a message with the specified content instead of the file.
    Currently, only .PDF and .ZIP files can be sent using this method.

    Attributes:
        type (str): Type of the result, must be 'document'.
        id (str): Unique identifier for this result, 1-64 bytes.
        title (str): Title for the result.
        caption (str, optional): Caption of the document to be sent, 0-1024 characters after entities parsing.
        parse_mode (str, optional): Mode for parsing entities in the document caption.
        caption_entities (list[MessageEntity], optional): List of special entities that appear in the caption.
        document_url (str): A valid URL for the file.
        mime_type (str): MIME type of the content of the file, either “application/pdf” or “application/zip”.
        description (str, optional): Short description of the result.
        reply_markup (InlineKeyboardMarkup, optional): Inline keyboard attached to the message.
        input_message_content (InputTextMessageContent, optional): Content of the message to be sent instead of the file.
        thumbnail_url (str, optional): URL of the thumbnail (JPEG only) for the file.
        thumbnail_width (int, optional): Thumbnail width.
        thumbnail_height (int, optional): Thumbnail height.
    """

    def __init__(self, *, id, title, document_url, mime_type, caption=None, parse_mode=None, caption_entities=None,
                 description=None, reply_markup=None, input_message_content=None, thumbnail_url=None,
                 thumbnail_width=None, thumbnail_height=None, **kwargs):
        super().__init__(**kwargs)
        self.type = 'document'
        self.id = id
        self.title = title
        self.document_url = document_url
        self.mime_type = mime_type
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.description = description
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
        self.thumbnail_url = thumbnail_url
        self.thumbnail_width = thumbnail_width
        self.thumbnail_height = thumbnail_height

    @staticmethod
    def validate_fields(data):
        """Validates the required fields for InlineQueryResultDocument."""
        required_fields = ['id', 'title', 'document_url', 'mime_type']
        for field in required_fields:
            if field not in data or not data[field]:
                raise ValueError(f"Field {field} is required and cannot be empty.")

        if 'type' in data and data['type'] != 'document':
            raise ValueError("Field 'type' must be 'document'.")

        return True