import os
from .Helpers import load_from_file,save_to_file, return_random_int

mod_value = 499

class PrivateKey:
    def __init__(self, file_path, mod_value):
        assert isinstance(file_path, str)
        assert isinstance(mod_value, int)
        self.file_path = file_path
        self.mod_value = mod_value
        self.vectors = []
        if os.path.isfile(self.file_path):
            self.vectors = eval(load_from_file(self.file_path))
        else:
            for _ in range(self.mod_value):
                self.vectors.append(return_random_int(self.mod_value, True))
            save_to_file(str(self.vectors), self.file_path)
