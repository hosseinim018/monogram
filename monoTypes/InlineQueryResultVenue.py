from monogram.monoTypes.baseType import BaseType
from monogram.monoTypes.InlineKeyboardMarkup import InlineKeyboardMarkup
from monogram.monoTypes.InputTextMessageContent import InputTextMessageContent

class InlineQueryResultVenue(BaseType):
    """
    Represents a venue. By default, the venue will be sent by the user.
    Alternatively, you can use input_message_content to send a message with the specified content instead of the venue.

    Attributes:
        type (str): Type of the result, must be 'venue'.
        id (str): Unique identifier for this result, 1-64 Bytes.
        latitude (float): Latitude of the venue location in degrees.
        longitude (float): Longitude of the venue location in degrees.
        title (str): Title of the venue.
        address (str): Address of the venue.
        foursquare_id (str, optional): Foursquare identifier of the venue if known.
        foursquare_type (str, optional): Foursquare type of the venue, if known.
        google_place_id (str, optional): Google Places identifier of the venue.
        google_place_type (str, optional): Google Places type of the venue.
        reply_markup (InlineKeyboardMarkup, optional): Inline keyboard attached to the message.
        input_message_content (InputTextMessageContent, optional): Content of the message to be sent instead of the venue.
        thumbnail_url (str, optional): URL of the thumbnail for the result.
        thumbnail_width (int, optional): Thumbnail width.
        thumbnail_height (int, optional): Thumbnail height.
    """

    def __init__(self, *, id, latitude, longitude, title, address, foursquare_id=None, foursquare_type=None,
                 google_place_id=None, google_place_type=None, reply_markup=None, input_message_content=None,
                 thumbnail_url=None, thumbnail_width=None, thumbnail_height=None, **kwargs):
        super().__init__(**kwargs)
        self.type = 'venue'
        self.id = id
        self.latitude = latitude
        self.longitude = longitude
        self.title = title
        self.address = address
        self.foursquare_id = foursquare_id
        self.foursquare_type = foursquare_type
        self.google_place_id = google_place_id
        self.google_place_type = google_place_type
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
        self.thumbnail_url = thumbnail_url
        self.thumbnail_width = thumbnail_width
        self.thumbnail_height = thumbnail_height

    @staticmethod
    def validate_fields(data):
        """Validates the required fields for InlineQueryResultVenue."""
        required_fields = ['id', 'latitude', 'longitude', 'title', 'address']
        for field in required_fields:
            if field not in data or not data[field]:
                raise ValueError(f"Field {field} is required and cannot be empty.")

        if 'type' in data and data['type'] != 'venue':
            raise ValueError("Field 'type' must be 'venue'.")

        return True