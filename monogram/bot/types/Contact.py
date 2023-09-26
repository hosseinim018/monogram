from typing import Optional


class Contact:
    """
    This class represents a phone contact.
    """

    def __init__(
            self,
            phone_number: str,
            first_name: str,
            last_name: Optional[str] = None,
            user_id: Optional[int] = None,
            vcard: Optional[str] = None
    ) -> object:
        """
        Initialize a Contact object.

        Args:
            phone_number (str): Contact's phone number.
            first_name (str): Contact's first name.
            last_name (str, optional): Contact's last name.
            user_id (int, optional): Contact's user identifier in Telegram. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier.
            vcard (str, optional): Additional data about the contact in the form of a vCard.
        """
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id
        self.vcard = vcard
