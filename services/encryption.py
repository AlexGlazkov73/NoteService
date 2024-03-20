import os
from pathlib import Path
from abc import ABC, abstractmethod, ABCMeta

from cryptography.fernet import Fernet


class AbstractEncryption(ABC):
    @abstractmethod
    def encrypt(self, text: str) -> str:
        raise NotImplementedError

    @abstractmethod
    def decrypt(self, text: str):
        raise NotImplementedError


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class EncryptionMeta(Singleton, ABCMeta):
    pass


class Encryption(AbstractEncryption, metaclass=EncryptionMeta):
    """Data encryption service. Saves the encryption key in the project root directory.
    It is needed to encrypt and decrypt data"""

    def __init__(self):
        self.root_path = Path(__file__).resolve().parent.parent
        self.key_path = os.path.join(self.root_path, 'crypto.key')
        self.write_key()

    def write_key(self):
        """Create crypto key and save it in the file"""
        key = Fernet.generate_key()
        with open(self.key_path, 'wb') as key_file:
            key_file.write(key)

    def load_key(self):
        """Get crypto key from current directory"""
        with open(self.key_path, 'rb') as key_file:
            key_data = key_file.read()
        return key_data

    def encrypt(self, text: str) -> str:
        key = self.load_key()
        encrypted_data = Fernet(key).encrypt(text.encode('utf-8'))
        return encrypted_data.decode('utf-8')

    def decrypt(self, text: str) -> str:
        key = self.load_key()
        decrypted_data = Fernet(key).decrypt(text)
        return decrypted_data.decode('utf-8')
