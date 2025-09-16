from monogram.monoTypes.baseType import BaseType

class InlineQueryResultContact(BaseType):
    """
    Represents a contact with a phone number.

    Attributes:
        type (str): Type of the result, must be 'contact'.
        id (str): Unique identifier for this result, 1-64 bytes.
        phone_number (str): Contact's phone number.
        first_name (str): Contact's first name.
        last_name (Optional[str]): Contact's last name.
        vcard (Optional[str]): Additional data about the contact in the form of a vCard.
    """

    def __init__(self, id: str, phone_number: str, first_name: str, last_name: str = None, vcard: str = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'contact'
        self.id = id
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.vcard = vcard

    def validate(self):
        """Validates the required fields."""
        if not self.id:
            raise ValueError("id is required")
        if not self.phone_number:
            raise ValueError("phone_number is required")
        if not self.first_name:
            raise ValueError("first_name is required")