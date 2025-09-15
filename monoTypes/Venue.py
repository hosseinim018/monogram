from typing import Optional
from .Location import Location


class Venue:
    """
    This class represents a venue.
    """

    def __init__(
        self,
        location: Location,
        title: str,
        address: str,
        foursquare_id: Optional[str] = None,
        foursquare_type: Optional[str] = None,
        google_place_id: Optional[str] = None,
        google_place_type: Optional[str] = None,
    ):
        """
        Initialize a Venue object.

        Args:
            location (Location): Venue location. Can't be a live location.
            title (str): Name of the venue.
            address (str): Address of the venue.
            foursquare_id (str, optional): Foursquare identifier of the venue.
            foursquare_type (str, optional): Foursquare type of the venue.
            google_place_id (str, optional): Google Places identifier of the venue.
            google_place_type (str, optional): Google Places type of the venue.
        """
        self.location = location
        self.title = title
        self.address = address
        self.foursquare_id = foursquare_id
        self.foursquare_type = foursquare_type
        self.google_place_id = google_place_id
        self.google_place_type = google_place_type
