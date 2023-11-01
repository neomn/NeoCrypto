from .Helpers import return_random_int

class GeneratePrivateKey:
    def __init__(self, mod_value):
        assert isinstance(mod_value, int)
        vectors = []
        for _ in range(mod_value):
                vectors.append(return_random_int(mod_value, True))
        return str(vectors)
