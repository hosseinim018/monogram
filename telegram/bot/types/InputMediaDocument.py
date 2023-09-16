class InputMediaDocument:
    """
    Represents a general file to be sent.
    """

    def __init__(self, media: str, thumbnail: str = None, caption: str = None, parse_mode: str = None,
                 caption_entities: list = None, disable_content_type_detection: bool = None):
        """
        Initialize an InputMediaDocument object.

        Args:
            media (str): The document file to be sent. Pass a file_id to send a file that exists on the Telegram servers
                         (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass
                         "attach://<file_attach_name>" to upload a new one using multipart/form-data under
                         <file_attach_name> name.
            thumbnail (str, optional): Thumbnail of the document file sent. Can be ignored if thumbnail generation
                                        for the file is supported server-side. The thumbnail should be in JPEG format
                                        and less than 200 kB in size. A thumbnail's width and height should not exceed
                                        320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails
                                        can't be reused and can be only uploaded as a new file, so you can pass
                                        "attach://<file_attach_name>" if the thumbnail was uploaded using multipart/form-data
                                        under <file_attach_name>.
            caption (str, optional): Caption of the document to be sent.
            parse_mode (str, optional): Mode for parsing entities in the document caption.
            caption_entities (list, optional): List of special entities that appear in the caption.
            disable_content_type_detection (bool, optional): Whether to disable automatic server-side content type
                                                              detection for files uploaded using multipart/form-data.
                                                              Set it to True if the document is sent as part of an album.
        """
        self.type = "document"
        self.media = media
        self.thumbnail = thumbnail
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.disable_content_type_detection = disable_content_type_detection
