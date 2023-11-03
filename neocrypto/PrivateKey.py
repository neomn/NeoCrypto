import errno
from os.path  import isfile
from .Helpers import return_random_int


class PrivateKey:

    def __init__(self, mod_value: int):
        self.mod_value = mod_value

    
    def generate(self):
        assert isinstance(self.mod_value, int)
        key = []
        for _ in range(self.mod_value):
                key.append(return_random_int(self.mod_value, True))
        self.key = key
        return key
    



    

         
    




