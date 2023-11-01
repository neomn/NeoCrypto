from .Helpers import return_random_int

def GeneratePrivateKey(mod_value: int):
    assert isinstance(mod_value, int)
    vectors = []
    for _ in range(mod_value):
            vectors.append(return_random_int(mod_value, True))
    return vectors
