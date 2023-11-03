from .Helpers          import  max_error, generate_error, return_random_int
from .StandardEquation import StandardEquation
from .PrivateKey       import PrivateKey


class PublicKey():
    
    def __init__(self, private_key: PrivateKey, mod_value: int):
        self.mod_value = mod_value
        self.private_key = private_key
        

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
        return standard_equations_stringified

    
    def read_from_string(self, string: str):
        return ''

        
    def read_from_file(self, file_path: str):
        return ''

        
    def save_to_file(self, file_path: str):
        return ''

    
