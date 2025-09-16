from typing import Optional, Any
from .baseType import BaseType

class InputLocationMessageContent(BaseType):
    """
    Represents the content of a location message to be sent as the result of an inline query.
    """

    def __init__(
        self,
        latitude: float,
        longitude: float,
        horizontal_accuracy: Optional[float] = None,
        live_period: Optional[int] = None,
        heading: Optional[int] = None,
        proximity_alert_radius: Optional[int] = None,
        **kwargs: Any
    ):
        """
        Initialize an InputLocationMessageContent object.

        Args:
            latitude (float): Latitude of the location in degrees
            longitude (float): Longitude of the location in degrees
            horizontal_accuracy (float, optional): The radius of uncertainty for the location, measured in meters; 0-1500
            live_period (int, optional): Period in seconds during which the location can be updated, should be between 60 and 86400
            heading (int, optional): For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified
            proximity_alert_radius (int, optional): For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified
            **kwargs: Additional fields that might be added in future Telegram Bot API updates
        """
        super().__init__(**kwargs)

        # Required fields
        self.latitude = latitude
        self.longitude = longitude

        # Optional fields
        self.horizontal_accuracy = horizontal_accuracy
        self.live_period = live_period
        self.heading = heading
        self.proximity_alert_radius = proximity_alert_radius

        # Store any additional fields for future compatibility
        for key, value in kwargs.items():
            if not hasattr(self, key):
                setattr(self, key, value)

    def __str__(self) -> str:
        """
        Get a string representation of the input location message content.

        Returns:
            str: A string containing the latitude and longitude
        """
        return f"Location: ({self.latitude}, {self.longitude})"