from .GeneratePrivateKey import GeneratePrivateKey

class NeoCrypto():
    def __init__(self, mod_val: int = 499):
        self.private_key = GeneratePrivateKey(mod_value = mod_val)
        self.public_key = ''

        
    def encrypt(self, message: str, public_key: str):
        return ''

        
    def decrypt(self, encrypted_message: str, private_key: str):
        return ''
