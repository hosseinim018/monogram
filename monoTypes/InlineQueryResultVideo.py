from monogram.monoTypes.baseType import BaseType
from monogram.monoTypes.InlineKeyboardMarkup import InlineKeyboardMarkup
from monogram.monoTypes.InputTextMessageContent import InputTextMessageContent
from monogram.monoTypes.MessageEntity import MessageEntity

class InlineQueryResultVideo(BaseType):
    """
    Represents a link to a page containing an embedded video player or a video file. By default, this video file will
    be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message
    with the specified content instead of the video.

    Attributes:
        type (str): Type of the result, must be 'video'.
        id (str): Unique identifier for this result, 1-64 bytes.
        video_url (str): A valid URL for the embedded video player or video file.
        mime_type (str): MIME type of the content of the video URL, “text/html” or “video/mp4”.
        thumbnail_url (str): URL of the thumbnail (JPEG only) for the video.
        title (str): Title for the result.
        caption (str, optional): Caption of the video to be sent, 0-1024 characters after entities parsing.
        parse_mode (str, optional): Mode for parsing entities in the video caption.
        caption_entities (list[MessageEntity], optional): List of special entities that appear in the caption.
        show_caption_above_media (bool, optional): Pass True, if the caption must be shown above the message media.
        video_width (int, optional): Video width.
        video_height (int, optional): Video height.
        video_duration (int, optional): Video duration in seconds.
        description (str, optional): Short description of the result.
        reply_markup (InlineKeyboardMarkup, optional): Inline keyboard attached to the message.
        input_message_content (InputTextMessageContent, optional): Content of the message to be sent instead of the video.
    """

    def __init__(self, *, id, video_url, mime_type, thumbnail_url, title, caption=None, parse_mode=None,
                 caption_entities=None, show_caption_above_media=None, video_width=None, video_height=None,
                 video_duration=None, description=None, reply_markup=None, input_message_content=None, **kwargs):
        super().__init__(**kwargs)
        self.type = 'video'
        self.id = id
        self.video_url = video_url
        self.mime_type = mime_type
        self.thumbnail_url = thumbnail_url
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.video_width = video_width
        self.video_height = video_height
        self.video_duration = video_duration
        self.description = description
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content

    @staticmethod
    def validate_fields(data):
        """Validates the required fields for InlineQueryResultVideo."""
        required_fields = ['id', 'video_url', 'mime_type', 'thumbnail_url', 'title']
        for field in required_fields:
            if field not in data or not data[field]:
                raise ValueError(f"Field {field} is required and cannot be empty.")

        if 'type' in data and data['type'] != 'video':
            raise ValueError("Field 'type' must be 'video'.")

        return True