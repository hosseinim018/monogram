from monogram.monoTypes.baseType import BaseType
from monogram.monoTypes.InlineKeyboardMarkup import InlineKeyboardMarkup
from monogram.monoTypes.InputTextMessageContent import InputTextMessageContent

class InlineQueryResultLocation(BaseType):
    """
    Represents a location on a map. By default, the location will be sent by the user.
    Alternatively, you can use input_message_content to send a message with the specified content instead of the location.

    Attributes:
        type (str): Type of the result, must be 'location'.
        id (str): Unique identifier for this result, 1-64 Bytes.
        latitude (float): Location latitude in degrees.
        longitude (float): Location longitude in degrees.
        title (str): Location title.
        horizontal_accuracy (float, optional): The radius of uncertainty for the location, measured in meters; 0-1500.
        live_period (int, optional): Period in seconds during which the location can be updated, should be between 60 and 86400.
        heading (int, optional): For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified.
        proximity_alert_radius (int, optional): For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified.
        reply_markup (InlineKeyboardMarkup, optional): Inline keyboard attached to the message.
        input_message_content (InputTextMessageContent, optional): Content of the message to be sent instead of the location.
        thumbnail_url (str, optional): URL of the thumbnail for the result.
        thumbnail_width (int, optional): Thumbnail width.
        thumbnail_height (int, optional): Thumbnail height.
    """

    def __init__(self, *, id, latitude, longitude, title, horizontal_accuracy=None, live_period=None, heading=None,
                 proximity_alert_radius=None, reply_markup=None, input_message_content=None, thumbnail_url=None,
                 thumbnail_width=None, thumbnail_height=None, **kwargs):
        super().__init__(**kwargs)
        self.type = 'location'
        self.id = id
        self.latitude = latitude
        self.longitude = longitude
        self.title = title
        self.horizontal_accuracy = horizontal_accuracy
        self.live_period = live_period
        self.heading = heading
        self.proximity_alert_radius = proximity_alert_radius
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
        self.thumbnail_url = thumbnail_url
        self.thumbnail_width = thumbnail_width
        self.thumbnail_height = thumbnail_height

    @staticmethod
    def validate_fields(data):
        """Validates the required fields for InlineQueryResultLocation."""
        required_fields = ['id', 'latitude', 'longitude', 'title']
        for field in required_fields:
            if field not in data or not data[field]:
                raise ValueError(f"Field {field} is required and cannot be empty.")

        if 'type' in data and data['type'] != 'location':
            raise ValueError("Field 'type' must be 'location'.")

        return True