from typing import Any
from .baseType import BaseType

class InlineQueryResult(BaseType):
    """
    This object represents one result of an inline query.
    Telegram clients currently support results of the following 20 types:

    - InlineQueryResultCachedAudio
    - InlineQueryResultCachedDocument
    - InlineQueryResultCachedGif
    - InlineQueryResultCachedMpeg4Gif
    - InlineQueryResultCachedPhoto
    - InlineQueryResultCachedSticker
    - InlineQueryResultCachedVideo
    - InlineQueryResultCachedVoice
    - InlineQueryResultArticle
    - InlineQueryResultAudio
    - InlineQueryResultContact
    - InlineQueryResultGame
    - InlineQueryResultDocument
    - InlineQueryResultGif
    - InlineQueryResultLocation
    - InlineQueryResultMpeg4Gif
    - InlineQueryResultPhoto
    - InlineQueryResultVenue
    - InlineQueryResultVideo
    - InlineQueryResultVoice

    Note: All URLs passed in inline query results will be available to end users and therefore must be assumed to be public.
    """

    def __init__(self, **kwargs: Any):
        """
        Initialize an InlineQueryResult object.

        Args:
            **kwargs: Additional fields that might be added in future Telegram Bot API updates
        """
        super().__init__(**kwargs)

        # Store any additional fields for future compatibility
        for key, value in kwargs.items():
            if not hasattr(self, key):
                setattr(self, key, value)

    def __str__(self) -> str:
        """
        Get a string representation of the inline query result.

        Returns:
            str: A string indicating this is an InlineQueryResult object
        """
        return "InlineQueryResult object"