import math, os, errno
from time import perf_counter_ns



def read_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = str(file.read())
        return content
    except Exception as e:
        print(f'read from file failed, {e}')


def save_to_file(content , file_path: str):
    try:
        with open(file_path, 'w') as file:
            file.write(str(content))
    except IOError as e:
        if e.errno == errno.EACCES:
            print('Permission denied') 
        elif e.errno == errno.ENOSPC:
            print('No space left on device')
    except Exception as e:
        print('Unknown exception:', e)


def generate_error(max_error_size: int):
    negative = return_random_int(2, False)
    index = return_random_int(max_error_size, False)
    error = index + 1
    if negative:
        return error * -1
    return error


def select_random_equation(public_key):
    equation_count = public_key.mod_value // 2
    index = return_random_int(equation_count, False)
    return public_key.key[index]


def return_random_int(mod_value: int, non_zero: bool):
    nanoseconds = perf_counter_ns()
    factor = 1
    for digit in str(nanoseconds):
        if int(digit) != 0:
            factor = (factor + int(digit)) * int(digit)
    factor = factor % mod_value
    if factor == 0 and non_zero:
        return 1
    return factor


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


# def create_public_key(mod_value: int):
#     key_identifier_input = input("Enter a Key identifier string: ")
#     public_key_path = preflight_checks_create_key(key_identifier_input)
#     public_key = PublicKey(public_key_path, mod_value)
#     return public_key


def preflight_checks_create_key(proposed_path: str):
    full_path_public_key = proposed_path + "_public_key.txt"
    full_path_private_key = proposed_path + "_private_key.txt"
    if os.path.isfile(full_path_public_key) or os.path.isfile(full_path_private_key):
        raise Exception("The proposed action would overwrite one or more existing files.")
    return full_path_public_key


# def load_key(key_type: str):
#     key_identifier_input = input("Enter a Key identifier string: ")
#     key_path = preflight_checks_load_key(key_identifier_input, key_type)
#     mod_value = derive_mod_from_key(key_type, key_path)
#     if key_type == "private":
#         return PrivateKey(key_path, mod_value)
#     else:
#         return PublicKey(key_path, mod_value)
#
#
# def derive_mod_from_key(key_type: str, path: str):
#     if key_type == "private":
#         return len(eval(read_from_file(path)))
#     else:
#         public_key = eval(load_from_file(path))
#         public_key_first_item_list = public_key[0]
#         return len(public_key_first_item_list[0])

def get_private_key_mod_value(private_key: list)-> int:
    key_len = len(private_key)
    if is_prime(key_len):
        return key_len
    else:
        raise ValueError('wrong prime number!, invalid private key')



def get_public_key_mod_value(public_key: list[list])-> int:
    key_len = len(public_key[0][0])
    print(f"len key[0] is {key_len}")
    if is_prime(key_len):
        return key_len
    else:
        raise ValueError('wrong prime number!, invalid public key')



def preflight_checks_load_key(proposed_path: str, key_type: str):
    if key_type == "public":
        public_key_path = proposed_path + "_public_key.txt"
        if not os.path.isfile(public_key_path):
            raise Exception("The specified file does not exist.")
        return public_key_path
    else:
        private_key_path = proposed_path + "_private_key.txt"
        if not os.path.isfile(private_key_path):
            raise Exception("The specified file does not exist.")
        return private_key_path


def return_prospective_encrypted_path():
    identifier = input("Enter an identifier string: ")
    proposed_path = os.path.join(os.getcwd(), identifier)
    return preflight_checks_encrypt(proposed_path)


def return_decrypted_and_encrypted_paths():
    identifier = input("Enter an identifier string: ")
    proposed_path = os.path.join(os.getcwd(), identifier)
    return preflight_checks_decrypt(proposed_path)


def preflight_checks_decrypt(proposed_path: str):
    full_path_decrypted = proposed_path + "_decrypted.txt"
    full_path_encrypted = proposed_path + "_encrypted.txt"
    if not os.path.isfile(full_path_encrypted):
        raise Exception("The specified file does not exist.")
    if os.path.isfile(full_path_decrypted):
        raise Exception("The proposed action would overwrite an existing file.")
    return [full_path_encrypted, full_path_decrypted]


def preflight_checks_encrypt(proposed_path: str):
    full_path_encrypted = proposed_path + "_encrypted.txt"
    if os.path.isfile(full_path_encrypted):
        raise Exception("The proposed action would overwrite an existing file.")
    return full_path_encrypted


def error_tolerance(mod_value: int):
    return (mod_value // 4) - 1


def max_error(mod_value: int):
    return math.floor(mod_value * 0.05)


def encapsulation_component_limit(mod_value: int):
    return error_tolerance(mod_value) // max_error(mod_value)
