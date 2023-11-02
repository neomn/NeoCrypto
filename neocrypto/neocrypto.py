from .GeneratePrivateKey import GeneratePrivateKey
from .GeneratePublicKey  import GeneratePublicKey


class NeoCrypto():
    def __init__(self, mod_val: int = 499):
        self.mod_value = mod_val

    
    def generate_private_key(self):
        return GeneratePrivateKey(self.mod_value)
    
    
    def generate_public_key(self, private_key):
        return GeneratePublicKey(private_key, self.mod_value)

    
    def encrypt(self, message: str, public_key: str):
        return ''

        
    def decrypt(self, encrypted_message: str, private_key: str):
        return ''
