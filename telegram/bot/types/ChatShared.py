class ChatShared:
    """
    This class contains information about the chat whose identifier was shared with the bot using a KeyboardButtonRequestChat button.
    """

    def __init__(self, request_id: int, chat_id: int):
        """
        Initialize a ChatShared object.

        Args:
            request_id (int): Identifier of the request.
            chat_id (int): Identifier of the shared chat. This number may have more than 32 significant bits and some programming
                           languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits,
                           so a 64-bit integer or double-precision float type are safe for storing this identifier. The bot may not
                           have access to the chat and could be unable to use this identifier, unless the chat is already known to
                           the bot by some other means.
        """
        self.request_id = request_id
        self.chat_id = chat_id
