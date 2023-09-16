from cryptography.fernet import Fernet

class TokenEncryptor:
    """
    Utility class for encrypting and decrypting tokens using the Fernet encryption algorithm.
    """

    def generate_secret_key(self) -> bytes:
        """
        Generates a random secret key for encryption.

        Returns:
            bytes: The secret key.
        """
        return Fernet.generate_key()

    def set_cipher_suite(self, secret_key: bytes) -> None:
        """
        Sets up the cipher suite for encryption and decryption.

        Args:
            secret_key (bytes): The secret key used for encryption and decryption.
        """
        self.cipher_suite = Fernet(secret_key)

    def encrypt(self, token: str) -> bytes:
        """
        Encrypts a token string.

        Args:
            token (str): The token to be encrypted.

        Returns:
            bytes: The encrypted token.
        """
        encrypted_token = self.cipher_suite.encrypt(token.encode())
        return encrypted_token

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


def validate_payload(locals):
    _locals = locals  # Create a copy of locals()
    _locals.pop('cls')  # Remove the key cls from _locals
    payload = {k: v for k, v in _locals.items() if v}  # Remove None values from payload
    return payload


