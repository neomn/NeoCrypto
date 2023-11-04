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

    
#--------------------------------------------------------------------------
    def save_private_key(self, file_path: str) -> None:
        '''
        save private key in a text file
        '''
        save_to_file(self.k, file_path)
        print('saved :)')

        
    def read_private_key(self, file_path) -> None:
        '''
        read private key from a text file
        '''
        content = read_from_file(file_path)
        key = self.private_key.validate_stringified_key(str(content))
        self.private_key.key = key
        self.k = key
        print('read private key from file successfully')
        

    def read_private_key_from_string(self, input: str) -> None:
        '''
        read private key from user input string
        '''
        key = self.private_key.validate_stringified_key(input)
        self.private_key.key = key
        self.k = key
        print('read private key from string successfully')




