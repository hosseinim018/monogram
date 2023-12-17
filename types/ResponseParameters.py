class ResponseParameters:
    """
    Describes why a request was unsuccessful.
    """

    def __init__(self, migrate_to_chat_id: int = None, retry_after: int = None):
        """
        Initialize a ResponseParameters object.

        Args:
            migrate_to_chat_id (int, optional): The group has been migrated to a supergroup with the specified identifier.
            retry_after (int, optional): In case of exceeding flood control, the number of seconds left to wait before
                                         the request can be repeated.
        """
        self.migrate_to_chat_id = migrate_to_chat_id
        self.retry_after = retry_after
