from .Helpers          import  max_error, generate_error, return_random_int
from .StandardEquation import StandardEquation
from .PrivateKey       import PrivateKey


class PublicKey():
    
    def __init__(self, private_key: PrivateKey, mod_value: int):
        self.mod_value = mod_value
        self.private_key = private_key
        self.key_string = ''
        

    def generate(self):
        standard_equations_stringified,  standard_equations_structured = [], []
        equation_count = self.mod_value // 2
        for _ in range(equation_count):
            coefficients = []
            constant = 0
            for i in range(self.mod_value):
                random_coefficient = return_random_int(self.mod_value, True)
                coefficients.append(random_coefficient)
                product = coefficients[i] * self.private_key.key[i]
                constant += product
            constant += generate_error(max_error(self.mod_value))
            new_standard_equation = StandardEquation(coefficients, constant)
            standard_equations_structured.append(new_standard_equation)
            standard_equations_stringified.append(new_standard_equation.stringify())
        self.key = standard_equations_structured
        self.key_string = standard_equations_stringified
        return self.key_string

    
    def string_to_structured(self, string: str):
        _list = self.validate_stringified_key(string)
        structured_key = []
        for _, equation in enumerate(_list):
                coefficient_list = list(equation[0])
                constant = equation[1]
                structured_key.append(StandardEquation(coefficient_list, constant))
        return structured_key
    
    
    def validate_stringified_key(self, string: str) -> list:
        key = eval(string) 
        assert isinstance(key, list)
        for coefficient, equation in key:
            assert isinstance(coefficient, list)
            assert isinstance(equation, int)
        return key
            




