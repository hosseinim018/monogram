from .baseType import BaseType
from .MaskPosition import MaskPosition
from typing import List

class InputSticker(BaseType):
    """
    This object describes a sticker to be added to a sticker set.
    https://core.telegram.org/bots/api#inputsticker
    """
    
    def __init__(self, dictionary: dict = None):
        super().__init__(dictionary)
        
        # Required fields
        self.sticker: str = None  # File to use as sticker (file_id, URL, or file upload)
        self.format: str = None  # Format of sticker: "static" (.WEBP/.PNG), "animated" (.TGS), "video" (.WEBM)
        self.emoji_list: List[str] = []  # List of 1-20 emoji associated with the sticker
        
        # Optional fields
        self.mask_position: MaskPosition = None
        self.keywords: List[str] = []

        if dictionary is not None:
            self.from_dictionary(dictionary)

    def from_dictionary(self, dictionary: dict):
        super().from_dictionary(dictionary)
        
        self.sticker = dictionary.get('sticker')
        self.format = dictionary.get('format')
        self.emoji_list = dictionary.get('emoji_list', [])
        
        if 'mask_position' in dictionary:
            self.mask_position = MaskPosition(dictionary.get('mask_position'))
        
        self.keywords = dictionary.get('keywords', [])
