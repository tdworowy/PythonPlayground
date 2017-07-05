import string
from random import choice


def generateRandomString(size):
    val = "".join(choice(string.ascii_lowercase) for i in range(size))
    return val


if __name__ == '__main__':
    print(generateRandomString(100))