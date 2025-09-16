from typing import Optional, Any
from .baseType import BaseType

class InputVenueMessageContent(BaseType):
    """
    Represents the content of a venue message to be sent as the result of an inline query.
    """

    def __init__(
        self,
        latitude: float,
        longitude: float,
        title: str,
        address: str,
        foursquare_id: Optional[str] = None,
        foursquare_type: Optional[str] = None,
        google_place_id: Optional[str] = None,
        google_place_type: Optional[str] = None,
        **kwargs: Any
    ):
        """
        Initialize an InputVenueMessageContent object.

        Args:
            latitude (float): Latitude of the venue in degrees
            longitude (float): Longitude of the venue in degrees
            title (str): Name of the venue
            address (str): Address of the venue
            foursquare_id (str, optional): Foursquare identifier of the venue, if known
            foursquare_type (str, optional): Foursquare type of the venue, if known
            google_place_id (str, optional): Google Places identifier of the venue
            google_place_type (str, optional): Google Places type of the venue
            **kwargs: Additional fields that might be added in future Telegram Bot API updates
        """
        super().__init__(**kwargs)

        # Required fields
        self.latitude = latitude
        self.longitude = longitude
        self.title = title
        self.address = address

        # Optional fields
        self.foursquare_id = foursquare_id
        self.foursquare_type = foursquare_type
        self.google_place_id = google_place_id
        self.google_place_type = google_place_type

        # Store any additional fields for future compatibility
        for key, value in kwargs.items():
            if not hasattr(self, key):
                setattr(self, key, value)

    def __str__(self) -> str:
        """
        Get a string representation of the input venue message content.

        Returns:
            str: A string containing the title and address
        """
        return f"Venue: {self.title}, {self.address}"