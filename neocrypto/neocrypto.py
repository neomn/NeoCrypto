from .GeneratePrivateKey import GeneratePrivateKey

class NeoCrypto():
    def __init__(self):
        self.private_key = GeneratePrivateKey(499)
        

