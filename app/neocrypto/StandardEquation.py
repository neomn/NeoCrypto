from .Helpers import error_tolerance

class StandardEquation:
    def __init__(self, coefficients, constant):
        assert isinstance(coefficients, list)
        assert isinstance(constant, int)
        self.coefficients = coefficients
        self.constant = constant

    def add_equation(self, standard_equation):
        assert isinstance(standard_equation, StandardEquation)
        for index, coefficient in enumerate(standard_equation.coefficients):
            if len(self.coefficients) < len(standard_equation.coefficients):
                self.coefficients.append(coefficient)
            else:
                self.coefficients[index] = self.coefficients[index] + coefficient
        self.constant = self.constant + standard_equation.constant

    def embed_data(self, data):
        assert isinstance(data, int)
        self.constant = self.constant + data

    def extract_data(self, vectors, mod_value):
        assert isinstance(vectors, list)
        assert isinstance(mod_value, int)
        tolerance = error_tolerance(mod_value)
        affirmative = mod_value // 2
        affirmative_lower_boundary = affirmative - tolerance
        affirmative_upper_boundary = affirmative + tolerance
        negative = 0
        negative_lower_boundary = negative - tolerance
        negative_upper_boundary = negative + tolerance
        actual_solution = 0
        for index, vector in enumerate(vectors):
            product = vector * self.coefficients[index]
            actual_solution = actual_solution + product
        difference = self.constant - actual_solution
        if affirmative_upper_boundary >= difference >= affirmative_lower_boundary:
            data = str(1)
        elif negative_upper_boundary >= difference >= negative_lower_boundary:
            data = str(0)
        else:
            data = str(0)
        return data

    def stringify(self):
        return [self.coefficients, self.constant]

