class PollOption:
    """
    This class contains information about one answer option in a poll.
    """

    def __init__(
        self,
        text: str,
        voter_count: int
    ):
        """
        Initialize a PollOption object.

        Args:
            text (str): Option text, 1-100 characters.
            voter_count (int): Number of users that voted for this option.
        """
        self.text = text
        self.voter_count = voter_count

# Example usage
option = PollOption(text="Option A", voter_count=10)
print(f"Text: {option.text}")
print(f"Voter Count: {option.voter_count}")