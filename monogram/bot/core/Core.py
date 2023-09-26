from cryptography.fernet import Fernet
from monogram.bot.config import TOKEN


class TokenEncryptor:
    """
    Utility class for encrypting and decrypting tokens using the Fernet encryption algorithm.
    """
    def __init__(self):
        """
               Encrypts a token string.
        """
        self.token: str = TOKEN
        self.secret_key: bytes = Fernet.generate_key()  # Generates a random secret key for encryption.
        self.cipher_suite = Fernet(self.secret_key)  # Sets up the cipher suite for encryption and decryption.
        # Encrypts a token string:
        self.encrypted_token: str = self.cipher_suite.encrypt(self.token.encode('utf-8')).decode()

    def decrypt(self, encrypted_token: bytes) -> str:
        """
        Decrypts an encrypted token.

        Args:
            encrypted_token (bytes): The encrypted token to be decrypted.

        Returns:
            str: The decrypted token.
        """
        decrypted_token = self.cipher_suite.decrypt(encrypted_token).decode()
        return decrypted_token


def validate_payload(_locals):
    _locals = _locals  # Create a copy of locals()
    _locals.pop('cls')  # Remove the key cls from _locals
    payload = {k: v for k, v in _locals.items() if v}  # Remove None values from payload
    return payload
