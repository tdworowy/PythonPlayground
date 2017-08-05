import string
from random import choices


def generateRandomString(size):
    return "".join(choices(string.ascii_lowercase, k=size))

def generateRandomStringAll(size):
    return ''.join(choices(string.ascii_letters + string.digits, k=size))



if __name__ == '__main__':
    print(generateRandomStringAll(35))