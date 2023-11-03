from .PrivateKey import PrivateKey
from .PublicKey  import PublicKey
from .Encrypt    import encrypt
from .Decrypt    import decrypt


class NeoCrypto:
    
    def __init__(self, mod_value: int = 499):
        self.mod_value   = mod_value
        self.private_key = PrivateKey(mod_value=mod_value)
        self.public_key  = PublicKey(self.private_key, self.mod_value)
        self.key         = self.private_key.generate()
        self.pub_key     = self.public_key.generate()
    

    def encrypt(self, message: str):
        return encrypt(message=message, public_key=self.public_key)

        
    def decrypt(self, encrypted_message: list):
        return decrypt(encrypted_message, self.private_key)
