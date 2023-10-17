# import os
#
# mod_value = 499
#
# class PublicKey:
#     def __init__(self, file_path, mod_value):
#         assert isinstance(file_path, str)
#         assert isinstance(mod_value, int)
#         self.file_path = file_path
#         self.mod_value = mod_value
#         self.standard_equations_stringified = []
#         self.standard_equations_structured = []
#         self.equation_count = mod_value // 2
#         if os.path.isfile(self.file_path):
#             self.standard_equations_stringified = eval(Helpers.load_from_file(self.file_path))
#             for _, equation in enumerate(self.standard_equations_stringified):
#                 coefficient_list = list(equation[0])
#                 constant = equation[1]
#                 self.standard_equations_structured.append(StandardEquation(coefficient_list, constant))
#         else:
#             private_key = PrivateKey(self.file_path.replace("public", "private"), self.mod_value)
#             for _ in range(self.equation_count):
#                 coefficients = []
#                 constant = 0
#                 for coefficient_index in range(self.mod_value):
#                     random_coefficient = Helpers.return_random_int(self.mod_value, True)
#                     coefficients.append(random_coefficient)
#                     product = (coefficients[coefficient_index] * private_key.vectors[coefficient_index])
#                     constant = constant + product
#                 constant = constant + Helpers.generate_error(Helpers.max_error(mod_value))
#                 new_standard_equation = StandardEquation(coefficients, constant)
#                 self.standard_equations_structured.append(new_standard_equation)
#                 self.standard_equations_stringified.append(new_standard_equation.stringify())
#             Helpers.save_to_file(self.standard_equations_stringified, self.file_path)
