import hashlib
import hmac
import base64
import os

class Authenticator:
    def __init__(self, secret_key=None):
        """
        Initialize the Authenticator with an optional secret key.
        If no secret key is provided, a new one will be generated.

        :param secret_key: The secret key used for HMAC. If None, a new key will be generated.
        """
        if secret_key is None:
            secret_key = base64.urlsafe_b64encode(os.urandom(32))
        self.secret_key = secret_key

    def hash_password(self, password):
        """
        Hash a password using SHA-256.

        :param password: The password to hash.
        :return: The hashed password as a hexadecimal string.
        """
        return hashlib.sha256(password.encode()).hexdigest()

    def verify_password(self, password, hashed_password):
        """
        Verify a password against its hash.

        :param password: The password to verify.
        :param hashed_password: The hashed password to verify against.
        :return: True if the password matches the hash, False otherwise.
        """
        return self.hash_password(password) == hashed_password

    def generate_token(self, message):
        """
        Generate an HMAC token for a given message.

        :param message: The message to generate a token for.
        :return: The generated HMAC token as a base64 encoded string.
        """
        return base64.urlsafe_b64encode(
            hmac.new(self.secret_key, message.encode(), hashlib.sha256).digest()
        ).decode()

    def verify_token(self, message, token):
        """
        Verify an HMAC token for a given message.

        :param message: The message to verify.
        :param token: The token to verify.
        :return: True if the token is valid, False otherwise.
        """
        expected_token = self.generate_token(message)
        return hmac.compare_digest(expected_token, token)

