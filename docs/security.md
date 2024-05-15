# Security

The `brent.security` package provides tools and utilities for handling authentication, encryption, and decryption. This package is designed to help developers secure their applications and manage sensitive data securely.

## Modules

The `brent.security` package includes the following modules:

- `auth.py`: Provides functionality for user authentication.
- `encryption.py`: Provides functionality for encrypting data.
- `decryption.py`: Provides functionality for decrypting data.

## auth.py

### Overview

The `auth.py` module contains the `Authenticator` class, which is used to handle user authentication.

### Authenticator Class

#### Initialization

```python
Authenticator(users: dict)
```

- `users`: A dictionary containing usernames as keys and passwords as values.

#### Methods

- `authenticate(username: str, password: str) -> bool`
  - Authenticates a user.
  - `username`: The username of the user.
  - `password`: The password of the user.
  - Returns `True` if authentication is successful, otherwise `False`.

- `add_user(username: str, password: str)`
  - Adds a new user.
  - `username`: The username of the new user.
  - `password`: The password of the new user.

- `remove_user(username: str)`
  - Removes an existing user.
  - `username`: The username of the user to remove.

#### Example Usage

```python
from brent.security.auth import Authenticator

users = {'admin': 'admin123', 'user1': 'password1'}
authenticator = Authenticator(users)

# Authenticate a user
if authenticator.authenticate('admin', 'admin123'):
    print("Authentication successful")
else:
    print("Authentication failed")

# Add a new user
authenticator.add_user('user2', 'password2')

# Remove a user
authenticator.remove_user('user1')
```

## encryption.py

### Overview

The `encryption.py` module contains the `Encryptor` class, which is used to encrypt data.

### Encryptor Class

#### Initialization

```python
Encryptor(key: bytes)
```

- `key`: The encryption key (must be 16, 24, or 32 bytes long).

#### Methods

- `encrypt(data: str) -> bytes`
  - Encrypts data.
  - `data`: The data to be encrypted.
  - Returns the encrypted data as bytes.

#### Example Usage

```python
from brent.security.encryption import Encryptor

key = b'mysecretpassword'
encryptor = Encryptor(key)

data = "Sensitive information"
encrypted_data = encryptor.encrypt(data)
print(f"Encrypted data: {encrypted_data}")
```

## decryption.py

### Overview

The `decryption.py` module contains the `Decryptor` class, which is used to decrypt data.

### Decryptor Class

#### Initialization

```python
Decryptor(key: bytes)
```

- `key`: The decryption key (must be the same key used for encryption).

#### Methods

- `decrypt(encrypted_data: bytes) -> str`
  - Decrypts data.
  - `encrypted_data`: The encrypted data to be decrypted.
  - Returns the decrypted data as a string.

#### Example Usage

```python
from brent.security.decryption import Decryptor

key = b'mysecretpassword'
decryptor = Decryptor(key)

encrypted_data = b'...'  # Encrypted data obtained from Encryptor
decrypted_data = decryptor.decrypt(encrypted_data)
print(f"Decrypted data: {decrypted_data}")
```

## Detailed Descriptions

### Authenticator

The `Authenticator` class provides a simple interface for managing user authentication. It supports adding and removing users and authenticating user credentials.

### Encryptor

The `Encryptor` class uses a symmetric encryption algorithm (such as AES) to encrypt data. It requires a key for encryption, which must be kept secure.

### Decryptor

The `Decryptor` class uses the same symmetric encryption algorithm (such as AES) to decrypt data that was encrypted using the `Encryptor` class. It requires the same key that was used for encryption.

## Notes

- Ensure that the encryption key used with the `Encryptor` and `Decryptor` classes is kept secure and not hard-coded in the source code.
- The `Authenticator` class does not store passwords securely. In a real-world application, passwords should be hashed and salted before storage.
- The `Encryptor` and `Decryptor` classes use symmetric encryption, meaning the same key is used for both encryption and decryption. Ensure that the key management practices are robust and secure.
- Proper error handling should be implemented to handle cases where decryption fails due to incorrect keys or corrupted data.


### Explanation

- **Modules**: Lists the modules included in the `brent.security` package.
- **auth.py**: Provides an overview and detailed description of the `Authenticator` class, including its initialization, methods, and example usage.
- **encryption.py**: Provides an overview and detailed description of the `Encryptor` class, including its initialization, methods, and example usage.
- **decryption.py**: Provides an overview and detailed description of the `Decryptor` class, including its initialization, methods, and example usage.
- **Detailed Descriptions**: Elaborates on the functionality and use cases of the `Authenticator`, `Encryptor`, and `Decryptor` classes.
- **Notes**: Provides additional information and considerations for using the classes in the `brent.security` package.