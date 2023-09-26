class ForumTopicEdited:
    """
    This class represents a service message about an edited forum topic.
    """

    def __init__(self, name: str = None, icon_custom_emoji_id: str = None):
        """
        Initialize a ForumTopicEdited object.

        Args:
            name (str, optional): New name of the topic, if it was edited.
            icon_custom_emoji_id (str, optional): New identifier of the custom emoji shown as the topic icon, if it was edited; an empty string if the icon was removed.
        """
        self.name = name
        self.icon_custom_emoji_id = icon_custom_emoji_id

