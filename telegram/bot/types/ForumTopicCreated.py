class ForumTopicCreated:
    """
    This class represents a service message about a new forum topic created in the chat.
    """

    def __init__(self, name: str, icon_color: int, icon_custom_emoji_id: str = None):
        """
        Initialize a ForumTopicCreated object.

        Args:
            name (str): Name of the topic.
            icon_color (int): Color of the topic icon in RGB format.
            icon_custom_emoji_id (str, optional): Unique identifier of the custom emoji shown as the topic icon.
        """
        self.name = name
        self.icon_color = icon_color
        self.icon_custom_emoji_id = icon_custom_emoji_id
