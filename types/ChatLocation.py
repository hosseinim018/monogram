from .Location import Location


class ChatLocation:
    """
    Represents a location to which a chat is connected.
    """

    def __init__(self, location: Location, address: str):
        """
        Initialize a ChatLocation object.

        Args:
            location (Location): The location to which the supergroup is connected. Cannot be a live location.
            address (str): Location address; 1-64 characters, as defined by the chat owner.
        """
        self.location = location
        self.address = address
