from typing import Optional
class ReplyKeyboardRemove:
    """
    Upon receiving a message with this object, Telegram clients will remove the current custom keyboard and display the default letter-keyboard.
    """
    def __init__(self, remove_keyboard: bool = True, selective: Optional[bool] = None):
        """
        Initialize a ReplyKeyboardRemove object.

        :param remove_keyboard: Boolean indicating if the custom keyboard should be removed.
        :param selective: Optional. Boolean indicating if the removal should be selective.
        """
        self.remove_keyboard = remove_keyboard
        self.selective = selective
