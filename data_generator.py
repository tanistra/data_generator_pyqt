import random
import string

def generator(data_type, size):
    # a = None
    size = int(size)
    if data_type != 'special':
        if data_type == 'str':
            a = ''.join(random.choice(string.ascii_uppercase) for _ in range(size))
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