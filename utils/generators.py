from random import choice
from string import (
    ascii_letters,
    digits,
)


def random_string_generator(len, hash_value):
    values = ascii_letters + digits
    value = ''
    for i in range(0, len):
        value = value + choice(values)
    return value + str(hash(hash_value))
