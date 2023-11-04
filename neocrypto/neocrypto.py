from .Helpers     import read_from_file, save_to_file
from .PrivateKey import *
from .PublicKey  import *
from .Encrypt    import encrypt
from .Decrypt    import decrypt


class NeoCrypto:
    
    def __init__(self, mod_value: int = 499):
        self.mod_value   = mod_value
        self.private_key = PrivateKey(mod_value=mod_value)             # private key instance
        self.public_key  = PublicKey(self.private_key, self.mod_value) # public key instance
        self.k           = self.private_key.generate()                 # stringified private key
        self.pk          = self.public_key.generate()                  # stringified public key
    
        
#--------------------------------------------------------------------------
    def encrypt(self, message: str):
        return encrypt(message=message, public_key=self.public_key)

        
    def decrypt(self, encrypted_message: list):
        return decrypt(encrypted_message, self.private_key)

    

