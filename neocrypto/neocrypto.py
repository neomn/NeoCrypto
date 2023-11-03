from .PrivateKey       import PrivateKey
from .PublicKey        import PublicKey
from .Encrypt          import Encrypt


class NeoCrypto:
    
    def __init__(self, mod_value: int = 499):
        self.mod_value = mod_value
        self.private_key = PrivateKey(mod_value=mod_value)
        self.public_key = PublicKey(self.private_key, self.mod_value)

    
    def encrypt(self, message: str):
        return Encrypt(message=message, public_key=self.public_key)

        
    def decrypt(self, encrypted_message: str, private_key: str):
        return ''
