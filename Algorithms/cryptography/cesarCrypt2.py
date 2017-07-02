import string

from MyUtils.compareStrings import getDiff
from MyUtils.myList import roundList


def CesarCrypt(text,index):
    return ''.join([getLetter(char,index) for char in text.lower()])

def CesarUnCrypt(text,index):
    return ''.join([getLetter(char,-index) for char in text.lower()])


def getLetter(char,jump):
    if char.isalpha():
        alpha =roundList(string.ascii_lowercase)
        index = alpha.index(char) + jump
        return alpha[index]
    else:
        return char


if __name__ == '__main__':
   test = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin rhoncus laoreet erat, sed lobortis nibh venenatis sit amet. Nullam quis."
   encrypted =  CesarCrypt(test,100)
   unEncrypted = CesarUnCrypt(encrypted,100)

   print("ENCRYPTED: ",encrypted)

   print("ORYGINAL: ",test.lower())
   print("UNENCRYPTED: ", unEncrypted)
   print(getDiff(unEncrypted, test.lower()))
   assert not getDiff(unEncrypted, test.lower())

