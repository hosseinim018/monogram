from typing import Optional

class MessageEntity:
    """
    This class represents one special entity in a text message.
    """

    def __init__(
        self,
        entity_type: str,
        offset: int,
        length: int,
        url: Optional[str] = None,
        user: Optional[str] = None,
        language: Optional[str] = None,
        custom_emoji_id: Optional[str] = None
    ):
        """
        Initialize a MessageEntity object.

        Args:
            entity_type (str): Type of the entity.
            offset (int): Offset in UTF-16 code units to the start of the entity.
            length (int): Length of the entity in UTF-16 code units.
            url (str, optional): URL that will be opened after user taps on the text (for "text_link" only).
            user (User, optional): The mentioned user (for "text_mention" only).
            language (str, optional): The programming language of the entity text (for "pre" only).
            custom_emoji_id (str, optional): Unique identifier of the custom emoji (for "custom_emoji" only).
        """
        self.entity_type = entity_type
        self.offset = offset
        self.length = length
        self.url = url
        self.user = user
        self.language = language
        self.custom_emoji_id = custom_emoji_id
