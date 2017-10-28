import string

from MyUtils.compareStrings import get_diff
from MyUtils.myList import RoundList


def cesar_crypt(text, index):
    return ''.join([get_letter(char, index) for char in text.lower()])


def cesar_uncrypt(text, index):
    return ''.join([get_letter(char, -index) for char in text.lower()])


def get_letter(char, jump):
    if char.isalpha():
        alpha = RoundList(string.ascii_lowercase)
        index = alpha.index(char) + jump
        return alpha[index]
    else:
        return char


if __name__ == '__main__':
    test = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin rhoncus laoreet erat, sed lobortis nibh " \
           "venenatis sit amet. Nullam quis. "
    encrypted = cesar_crypt(test, 100)
    unEncrypted = cesar_uncrypt(encrypted, 100)

    print("ENCRYPTED: ", encrypted)

    print("ORYGINAL: ", test.lower())
    print("UNENCRYPTED: ", unEncrypted)
    print(get_diff(unEncrypted, test.lower()))
    assert not get_diff(unEncrypted, test.lower())
