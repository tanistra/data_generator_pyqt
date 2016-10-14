import random
import string


def generator(data_type, size, upper=True):
    if len(size) == 0:
        raise ValueError('Field length cannot be empty')
    size = int(size)
    choice_int = ''
    choice_str = ''
    choice_special = ''
    if data_type == 'str' or data_type == 'all':
        choice_str = string.ascii_uppercase
    if data_type == 'int' or data_type == 'all':
        choice_int = string.digits
    if data_type == 'special' or data_type == 'all':
        choice_special = '~`!@#$%^&*()_+=-{}:"|<>?/.,\'\\\;][|'

    value = _random_choice(size, choice_int, choice_str, choice_special)
    if not upper:
        value.lower()
    return value


def _random_choice(size, choice_int, choice_str, choice_spec):
    attributes = choice_int + choice_str + choice_spec
    print(attributes)
    return ''.join(random.choice(attributes) for _ in range(size))
