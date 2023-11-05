from .Helpers           import  encapsulation_component_limit, select_random_equation
from .StandardEquation  import StandardEquation
from .PublicKey         import PublicKey

class EncapsulationEquation:
    def __init__(self, public_key: PublicKey, data):
        self.component_standard_equations = []
        self.encapsulation_equation = StandardEquation([], 0)
        self.component_limit = encapsulation_component_limit(public_key.mod_value)
        for _ in range(self.component_limit):
            self.component_standard_equations.append(select_random_equation(public_key))
        for equation in self.component_standard_equations:
            self.encapsulation_equation.add_equation(equation)
        self.processed_data = ((public_key.mod_value // 2) * data)
        self.encapsulation_equation.embed_data(self.processed_data)

    def stringify(self):
        return [self.encapsulation_equation.coefficients, self.encapsulation_equation.constant]
