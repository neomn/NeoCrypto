from .Helpers          import  max_error, generate_error, return_random_int
from .StandardEquation import StandardEquation


def GeneratePublicKey(private_key: list, mod_value: int):
    standard_equations_stringified = []
    standard_equations_structured = []
    equation_count = mod_value // 2

    private_key = private_key
    for _ in range(equation_count):
        coefficients = []
        constant = 0
        for coefficient_index in range(mod_value):
            random_coefficient = return_random_int(mod_value, True)
            coefficients.append(random_coefficient)
            product = (coefficients[coefficient_index] * private_key[coefficient_index])
            constant = constant + product
        constant = constant + generate_error(max_error(mod_value))
        new_standard_equation = StandardEquation(coefficients, constant)
        standard_equations_structured.append(new_standard_equation)
        standard_equations_stringified.append(new_standard_equation.stringify())
    return standard_equations_stringified
