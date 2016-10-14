import random
import string


def generator(data_type, size, upper=True):
    a = None
    if len(size) == 0:
        raise ValueError('Field length cannot be empty')
    size = int(size)
    if data_type != 'special':
        if data_type == 'str':
            if upper:
                uppercase = string.ascii_uppercase
            else:
                uppercase = string.ascii_lowercase

            a = ''.join(random.choice(uppercase) for _ in range(size))

        elif data_type == 'int':
            a = ''.join(random.choice(string.digits) for _ in range(size))
    else:
        special = "~`!@#$%^&*()_+=-{}:|<\>?[];'\,./|"
        new_size = size - len(special)
        if new_size <= 0:
            a = special
        else:
            a = ''.join(random.choice("~`!@#$%^&*()_+=-{}:|<\>?[];'\,./|") for _ in range(size))
    return a