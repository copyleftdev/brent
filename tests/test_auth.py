import unittest
import base64
import os
from unittest.mock import patch, MagicMock
from brent.security.auth import Authenticator

class TestAuthenticator(unittest.TestCase):

    def setUp(self):
        self.secret_key = base64.urlsafe_b64encode(os.urandom(32))
        self.authenticator = Authenticator(secret_key=self.secret_key)
        self.password = "my_secure_password"
        self.message = "my_message"

    def test_hash_password(self):
        hashed_password = self.authenticator.hash_password(self.password)
        self.assertIsInstance(hashed_password, str)
        self.assertEqual(len(hashed_password), 64)  # SHA-256 hash length in hexadecimal

    def test_verify_password(self):
        hashed_password = self.authenticator.hash_password(self.password)
        self.assertTrue(self.authenticator.verify_password(self.password, hashed_password))
        self.assertFalse(self.authenticator.verify_password("wrong_password", hashed_password))

    def test_generate_token(self):
        token = self.authenticator.generate_token(self.message)
        self.assertIsInstance(token, str)

    def test_verify_token(self):
        token = self.authenticator.generate_token(self.message)
        self.assertTrue(self.authenticator.verify_token(self.message, token))
        self.assertFalse(self.authenticator.verify_token("wrong_message", token))

    @patch('os.urandom')
    @patch('base64.urlsafe_b64encode')
    def test_generate_secret_key(self, mock_b64encode, mock_urandom):
        mock_urandom.return_value = b'some_random_bytes'
        mock_b64encode.return_value = b'base64_encoded_key'
        auth = Authenticator(secret_key=None)
        self.assertEqual(auth.secret_key, b'base64_encoded_key')

if __name__ == '__main__':
    unittest.main()
