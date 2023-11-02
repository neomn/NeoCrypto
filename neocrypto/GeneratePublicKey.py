from .Helpers          import  max_error, generate_error, return_random_int
from .StandardEquation import StandardEquation


def GeneratePublicKey(private_key: list, mod_value: int):
    standard_equations_stringified,  standard_equations_structured = [], []
    equation_count = mod_value // 2
    
    for _ in range(equation_count):
        coefficients = []
        constant = 0
        for i in range(mod_value):
            random_coefficient = return_random_int(mod_value, True)
            coefficients.append(random_coefficient)
            product = (coefficients[i] * private_key[i])
            constant = constant + product
        constant = constant + generate_error(max_error(mod_value))
        new_standard_equation = StandardEquation(coefficients, constant)
        standard_equations_structured.append(new_standard_equation)
        standard_equations_stringified.append(new_standard_equation.stringify())
    return standard_equations_stringified
