from .User import User


class ProximityAlertTriggered:
    """
    This class represents the content of a service message, sent whenever a user in the chat triggers a proximity alert set by another user.
    """

    def __init__(self, traveler: User, watcher: User, distance: int):
        """
        Initialize a ProximityAlertTriggered object.

        Args:
            traveler (User): User that triggered the alert.
            watcher (User): User that set the alert.
            distance (int): The distance between the users.
        """
        self.traveler = traveler
        self.watcher = watcher
        self.distance = distance
