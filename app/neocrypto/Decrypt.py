from .PrivateKey                  import PrivateKey
from .DecryptedCharacterContainer import DecryptedCharacterContainer

def decrypt(encrypted_message: str, private_key: PrivateKey)-> str:
    encrypted_message_list = eval(encrypted_message)
    message = ""
    for encrypted_ch_list in encrypted_message_list:
        ch = DecryptedCharacterContainer(private_key, encrypted_ch_list)
        message += ch.character_ascii_char
    return message
