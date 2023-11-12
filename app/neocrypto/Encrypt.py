from .PublicKey                   import PublicKey
from .EncryptedCharacterContainer import EncryptedCharacterContainer


def encrypt(message: str, public_key: PublicKey)-> str:
    encrypted_message, encrypted_string_structured = [], []
    for ch in message:
        encrypted_ch = EncryptedCharacterContainer(public_key, ch)
        encrypted_string_structured.append(encrypted_ch.encapsulation_equations_structured)
        encrypted_message.append(encrypted_ch.encapsulation_equations_stringified)
    return str(encrypted_message)


