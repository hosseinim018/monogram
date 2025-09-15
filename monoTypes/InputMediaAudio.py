class InputMediaAudio:
    """
    Represents an audio file to be treated as music to be sent.
    """

    def __init__(self, media: str, thumbnail: str = None, caption: str = None, parse_mode: str = None,
                 caption_entities: list = None, duration: int = None, performer: str = None, title: str = None):
        """
        Initialize an InputMediaAudio object.

        Args:
            media (str): The audio file to be sent. Pass a file_id to send a file that exists on the Telegram servers
                         (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass
                         "attach://<file_attach_name>" to upload a new one using multipart/form-data under
                         <file_attach_name> name.
            thumbnail (str, optional): Thumbnail of the audio file sent. Can be ignored if thumbnail generation
                                        for the file is supported server-side. The thumbnail should be in JPEG format
                                        and less than 200 kB in size. A thumbnail's width and height should not exceed
                                        320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails
                                        can't be reused and can be only uploaded as a new file, so you can pass
                                        "attach://<file_attach_name>" if the thumbnail was uploaded using multipart/form-data
                                        under <file_attach_name>.
            caption (str, optional): Caption of the audio to be sent.
            parse_mode (str, optional): Mode for parsing entities in the audio caption.
            caption_entities (list, optional): List of special entities that appear in the caption.
            duration (int, optional): Duration of the audio in seconds.
            performer (str, optional): Performer of the audio.
            title (str, optional): Title of the audio.
        """
        self.type = "audio"
        self.media = media
        self.thumbnail = thumbnail
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.duration = duration
        self.performer = performer
        self.title = title
