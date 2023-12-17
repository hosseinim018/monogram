class InputMediaAnimation:
    """
    Represents an animation file (GIF or H.264/MPEG-4 AVC video without sound) to be sent.
    """

    def __init__(self, media: str, thumbnail: str = None, caption: str = None, parse_mode: str = None,
                 caption_entities: list = None, width: int = None, height: int = None, duration: int = None,
                 has_spoiler: bool = None):
        """
        Initialize an InputMediaAnimation object.

        Args:
            media (str): The animation file to be sent. Pass a file_id to send a file that exists on the Telegram servers
                         (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass
                         "attach://<file_attach_name>" to upload a new one using multipart/form-data under
                         <file_attach_name> name.
            thumbnail (str, optional): Thumbnail of the animation file sent. Can be ignored if thumbnail generation
                                        for the file is supported server-side. The thumbnail should be in JPEG format
                                        and less than 200 kB in size. A thumbnail's width and height should not exceed
                                        320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails
                                        can't be reused and can be only uploaded as a new file, so you can pass
                                        "attach://<file_attach_name>" if the thumbnail was uploaded using multipart/form-data
                                        under <file_attach_name>.
            caption (str, optional): Caption of the animation to be sent.
            parse_mode (str, optional): Mode for parsing entities in the animation caption.
            caption_entities (list, optional): List of special entities that appear in the caption.
            width (int, optional): Animation width.
            height (int, optional): Animation height.
            duration (int, optional): Animation duration in seconds.
            has_spoiler (bool, optional): Pass True if the animation needs to be covered with a spoiler animation.
        """
        self.type = "animation"
        self.media = media
        self.thumbnail = thumbnail
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.width = width
        self.height = height
        self.duration = duration
        self.has_spoiler = has_spoiler
