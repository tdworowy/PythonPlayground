import string


def get_diff(string1, string2):
    char_list = list(string2)
    i = 0
    diff = []
    for char1 in string1:
        if i < len(char_list):
            if char1 != char_list[i]:
                diff.append((char_list[i], char1))
            i += 1
    return diff


class RoundList(list):
    def __getitem__(self, index):

        while index not in range(0, len(self)):
            if index >= len(self):
                index = index - len(self)
            else:
                if index < 0:
                    index = len(self) - (index * -1)

        return list.__getitem__(self, index)


def cesar_crypt(text, index):
    return "".join([get_letter(char, index) for char in text.lower()])


def cesar_uncrypt(text, index):
    return "".join([get_letter(char, -index) for char in text.lower()])


def get_letter(char, jump):
    if char.isalpha():
        alpha = RoundList(string.ascii_lowercase)
        index = alpha.index(char) + jump
        return alpha[index]
    else:
        return char


if __name__ == "__main__":
    test = (
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin rhoncus laoreet erat, sed lobortis nibh "
        "venenatis sit amet. Nullam quis. "
    )
    encrypted = cesar_crypt(test, 100)
    unEncrypted = cesar_uncrypt(encrypted, 100)

    print("ENCRYPTED: ", encrypted)

    print("ORYGINAL: ", test.lower())
    print("UNENCRYPTED: ", unEncrypted)
    print(get_diff(unEncrypted, test.lower()))
    assert not get_diff(unEncrypted, test.lower())
