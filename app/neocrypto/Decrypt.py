from .PrivateKey                  import PrivateKey
from .DecryptedCharacterContainer import DecryptedCharacterContainer

def decrypt(encrypted_message: list, private_key: PrivateKey):
    message = ""
    for encrypted_ch in encrypted_message:
        ch = DecryptedCharacterContainer(private_key, encrypted_ch)
        message += ch.character_ascii_char
    return message
