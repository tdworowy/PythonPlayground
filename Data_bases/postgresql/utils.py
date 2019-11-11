import string
from random import choice


def random_string(size):
    val = "".join(choice(string.ascii_lowercase) for _ in range(size))
    return val
