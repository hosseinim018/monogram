class ForceReply:
    """
    This class represents a reply markup object that, when sent as a reply to a message,
    forces the user to reply and displays a reply interface in the Telegram client.
    """

    def __init__(
        self,
        input_field_placeholder: str = None,
        selective: bool = False
    ):
        """
        Initialize a ForceReply object.

        Args:
            input_field_placeholder (str, optional): The placeholder to be shown in the input field when the reply is active.
                This field is optional and can have 1-64 characters.
            selective (bool, optional): Use this parameter if you want to force a reply from specific users only.
                Targets: 1) users that are @mentioned in the text of the Message object;
                2) if the bot's message is a reply (has reply_to_message_id), sender of the original message.
                This field is optional and defaults to False.
        """
        self.force_reply = True
        self.input_field_placeholder = input_field_placeholder
        self.selective = selective
