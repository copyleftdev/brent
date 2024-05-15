from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import base64
import os

class Decryption:
    def __init__(self, key):
        """
        Initialize the Decryption class with a secret key.

        :param key: The secret key used for decryption. Must be 32 bytes long for AES-256.
        """
        if len(key) != 32:
            raise ValueError("Key must be 32 bytes long for AES-256.")
        self.key = key

    def decrypt(self, encrypted_data):
        """
        Decrypt the provided encrypted data.

        :param encrypted_data: The encrypted data to decrypt.
        :return: The decrypted plaintext.
        """
        encrypted_data = base64.urlsafe_b64decode(encrypted_data)
        iv = encrypted_data[:16]
        ciphertext = encrypted_data[16:]

        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()

        padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()
        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()

        return plaintext.decode()
