class Dice:
    """
    This class represents an animated emoji that displays a random value.
    """

    def __init__(
        self,
        emoji: str,
        value: int
    ):
        """
        Initialize a Dice object.

        Args:
            emoji (str): Emoji on which the dice throw animation is based.
            value (int): Value of the dice. The range of the value depends on the base emoji:
                - For "🎲", "🎯", and "🎳" base emoji, the value can be 1-6.
                - For "🏀" and "⚽" base emoji, the value can be 1-5.
                - For "🎰" base emoji, the value can be 1-64.
        """
        self.emoji = emoji
        self.value = value
