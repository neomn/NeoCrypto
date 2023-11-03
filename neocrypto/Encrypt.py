from .PublicKey                   import PublicKey
from .EncryptedCharacterContainer import EncryptedCharacterContainer


class Encrypt:
    def __init__(self, message: str, public_key: PublicKey):
        self.encrypted_string_structured = []
        encrypted_message = []
        for ch in message:
            encrypted_ch = EncryptedCharacterContainer(public_key, ch)
            self.encrypted_string_structured.append(encrypted_ch.encapsulation_equations_structured)
            encrypted_message.append(encrypted_ch.encapsulation_equations_stringified)
        return encrypted_message
   

