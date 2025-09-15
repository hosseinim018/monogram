from .baseType import BaseType
from .PhotoSize import PhotoSize
from .File import File
from .MaskPosition import MaskPosition

class Sticker(BaseType):
    """
    This object represents a sticker.
    https://core.telegram.org/bots/api#sticker
    """
    
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
    
        if 'thumbnail' in kwargs:
            self.thumbnail = PhotoSize(**kwargs['thumbnail'])
            
        if 'premium_animation' in kwargs:
            self.premium_animation = File(**kwargs['premium_animation'])

        if 'mask_position' in kwargs:
            self.mask_position = MaskPosition(**kwargs['mask_position'])