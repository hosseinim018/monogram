from typing import Optional

class Location:
    """
    This class represents a point on the map.
    """

    def __init__(
        self,
        longitude: float,
        latitude: float,
        horizontal_accuracy: Optional[float] = None,
        live_period: Optional[int] = None,
        heading: Optional[int] = None,
        proximity_alert_radius: Optional[int] = None
    ):
        """
        Initialize a Location object.

        Args:
            longitude (float): Longitude as defined by sender.
            latitude (float): Latitude as defined by sender.
            horizontal_accuracy (float, optional): The radius of uncertainty for the location, measured in meters; 0-1500.
            live_period (int, optional): Time relative to the message sending date, during which the location can be updated; in seconds. For active live locations only.
            heading (int, optional): The direction in which the user is moving, in degrees; 1-360. For active live locations only.
            proximity_alert_radius (int, optional): The maximum distance for proximity alerts about approaching another chat member, in meters. For sent live locations only.
        """
        self.longitude = longitude
        self.latitude = latitude
        self.horizontal_accuracy = horizontal_accuracy
        self.live_period = live_period
        self.heading = heading
        self.proximity_alert_radius = proximity_alert_radius

