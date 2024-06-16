import string
from random import choices


def generate_random_string(size):
    return "".join(choices(string.ascii_lowercase, k=size))


def generate_random_string_all(size):
    return "".join(choices(string.ascii_letters + string.digits, k=size))


if __name__ == "__main__":
    print(generate_random_string_all(12))
