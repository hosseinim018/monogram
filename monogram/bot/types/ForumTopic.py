class ForumTopic:
    """
    Represents a forum topic.
    """

    def __init__(self, message_thread_id: int, name: str, icon_color: int, icon_custom_emoji_id: str = None):
        """
        Initialize a ForumTopic object.

        Args:
            message_thread_id (int): Unique identifier of the forum topic.
            name (str): Name of the topic.
            icon_color (int): Color of the topic icon in RGB format.
            icon_custom_emoji_id (str, optional): Unique identifier of the custom emoji shown as the topic icon.
                Defaults to None.
        """
        self.message_thread_id = message_thread_id
        self.name = name
        self.icon_color = icon_color
        self.icon_custom_emoji_id = icon_custom_emoji_id
