from .baseType import BaseType
from .Sticker import Sticker
from .PhotoSize import PhotoSize
from typing import List

class StickerSet(BaseType):
    """
    This object represents a sticker set.
    https://core.telegram.org/bots/api#stickerset
    """
    
    def __init__(self, dictionary: dict = None):
        super().__init__(dictionary)
        
        # Required fields
        self.name: str = None  # Sticker set name
        self.title: str = None  # Sticker set title
        self.sticker_type: str = None  # Type of stickers: "regular", "mask", or "custom_emoji"
        self.stickers: List[Sticker] = []  # List of all stickers in this set
        
        # Optional field
        self.thumbnail: PhotoSize = None

        if dictionary is not None:
            self.from_dictionary(dictionary)

    def from_dictionary(self, dictionary: dict):
        super().from_dictionary(dictionary)
        
        self.name = dictionary.get('name')
        self.title = dictionary.get('title')
        self.sticker_type = dictionary.get('sticker_type')
        
        if 'stickers' in dictionary:
            self.stickers = [Sticker(sticker) for sticker in dictionary.get('stickers')]
        
        if 'thumbnail' in dictionary:
            self.thumbnail = PhotoSize(dictionary.get('thumbnail'))
