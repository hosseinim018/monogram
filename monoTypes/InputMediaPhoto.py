class InputMediaPhoto:
    """
    Represents a photo to be sent.
    """

    def __init__(self, media: str, caption: str = None, parse_mode: str = None, caption_entities: list = None, has_spoiler: bool = None):
        """
        Initialize an InputMediaPhoto object.

        Args:
            media (str): The photo file to be sent. Pass a file_id to send a file that exists on the Telegram servers
                         (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass
                         "attach://<file_attach_name>" to upload a new one using multipart/form-data under
                         <file_attach_name> name.
            caption (str, optional): Caption of the photo to be sent.
            parse_mode (str, optional): Mode for parsing entities in the photo caption.
            caption_entities (list, optional): List of special entities that appear in the caption.
            has_spoiler (bool, optional): Pass True if the photo needs to be covered with a spoiler animation.
        """
        self.type = "photo"
        self.media = media
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.has_spoiler = has_spoiler
