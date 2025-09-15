from .baseType import BaseType

class MaskPosition(BaseType):
    """
    This object describes the position on faces where a mask should be placed by default.
    https://core.telegram.org/bots/api#maskposition
    """
    
    def __init__(self, dictionary: dict = None):
        super().__init__(dictionary)
        
        # Required fields
        self.point: str = None  # The part of the face: "forehead", "eyes", "mouth", or "chin"
        self.x_shift: float = None  # Shift by X-axis measured in widths of the mask (-1.0 to 1.0)
        self.y_shift: float = None  # Shift by Y-axis measured in heights of the mask (-1.0 to 1.0)
        self.scale: float = None  # Mask scaling coefficient (1.0 is default, 2.0 doubles size)

        if dictionary is not None:
            self.from_dictionary(dictionary)

    def from_dictionary(self, dictionary: dict):
        super().from_dictionary(dictionary)
        
        self.point = dictionary.get('point')
        self.x_shift = dictionary.get('x_shift')
        self.y_shift = dictionary.get('y_shift')
        self.scale = dictionary.get('scale')
