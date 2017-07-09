import string
from random import choice


def generateRandomString(size):
    return "".join(choice(string.ascii_lowercase) for i in range(size))



if __name__ == '__main__':
    print(generateRandomString(100))