from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import base64
import os

class Encryption:
    def __init__(self, key):
        """
        Initialize the Encryption class with a secret key.

        :param key: The secret key used for encryption. Must be 32 bytes long for AES-256.
        """
        if len(key) != 32:
            raise ValueError("Key must be 32 bytes long for AES-256.")
        self.key = key

    def encrypt(self, plaintext):
        """
        Encrypt the provided plaintext.

        :param plaintext: The plaintext to encrypt.
        :return: The encrypted data as a base64 encoded string.
        """
        iv = os.urandom(16)
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()

        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        padded_plaintext = padder.update(plaintext.encode()) + padder.finalize()

        ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()
        encrypted_data = iv + ciphertext

        return base64.urlsafe_b64encode(encrypted_data).decode()
