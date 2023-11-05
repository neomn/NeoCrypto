from .EncapsulationEquation import EncapsulationEquation
from .PublicKey             import PublicKey

class EncryptedCharacterContainer:
    def __init__(self, public_key:PublicKey, ch: str):
        assert len(ch)==1
        unicode = ord(ch)
        binary = bin(unicode)[2:].zfill(8)
        self.encapsulation_equations_stringified = []
        self.encapsulation_equations_structured = []
        for bit in binary:
            encapsulation_equation = EncapsulationEquation(public_key, bit == "1")
            self.encapsulation_equations_structured.append(encapsulation_equation)
            self.encapsulation_equations_stringified.append(encapsulation_equation.stringify())
