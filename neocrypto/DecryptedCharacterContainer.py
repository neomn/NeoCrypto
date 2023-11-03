import random
from .PrivateKey       import PrivateKey
from .StandardEquation import StandardEquation

class DecryptedCharacterContainer:
    def __init__(self, private_key: PrivateKey, character_encrypted: list):
        self.character_encrypted = character_encrypted
        self.character_binary_string = ""
        for equation_string in character_encrypted:
            equation_list = list(equation_string)
            equation_coefficient_list = list(equation_list[0])
            equation_constant = equation_list[1]
            equation = StandardEquation(equation_coefficient_list, equation_constant)
            self.character_binary_string = self.character_binary_string + equation.extract_data(
                private_key.key, private_key.mod_value)
        self.character_unicode_int = int(self.character_binary_string, 2)
        if self.character_unicode_int < 32 or self.character_unicode_int > 126:
            self.character_unicode_int = random.randint(32, 126)
        self.character_ascii_char = chr(self.character_unicode_int)
