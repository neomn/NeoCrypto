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
    

    def read_key_from_string(self, string: str):
        key = eval(string)
        assert isinstance(key, list)
        for num in key:
            assert isinstance(num, int)
        self.key = key
        return key

    
    def read_key_from_file(self, file_path: str):
        assert isfile(file_path)
        with open(file_path, 'r') as file:
            content = file.read()
        return self.read_key_from_string(content)
         
    
    def save_to_file(self, file_path: str):
        try:
            with open(file_path, 'w') as file:
                file.write(str(self.key))
            return True
        except IOError as e:
            if e.errno == errno.EACCES:
                print('Permission denied') 
            elif e.errno == errno.ENOSPC:
                print('No space left on device')
        except Exception as e:
            print('Unknown exception:', e)



