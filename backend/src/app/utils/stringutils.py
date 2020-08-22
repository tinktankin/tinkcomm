import random
import string

# check if string is empty
def is_string_empty(str):
    if not str or str.isspace():
        return True
    return False


def generate_random_string(no_of_digit=5):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=no_of_digit))