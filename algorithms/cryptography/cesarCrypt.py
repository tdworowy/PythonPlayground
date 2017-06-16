import string

# TODO refactor
from myUtils.compareStrings import getDiff


def CesarCrypt(text,index):
    return ''.join([getLetterUP(char,index) for char in text.lower()])

def CesarUnCrypt(text,index):
    return ''.join([getLetterDOWN(char,index) for char in text.lower()])


def getLetterUP(char,jump):
    if  char.isalpha():
        alpha = string.ascii_lowercase
        index = alpha.index(char)+jump
        while index not in range(0,len(alpha)):
            index =setIndexUP(index,len(alpha))
        return alpha[index]
    else:
        return char


def getLetterDOWN(char,jump):
    if  char.isalpha():
        alpha = string.ascii_lowercase
        index = alpha.index(char)-jump
        while index not in range(0,len(alpha)):
            index =setIndexDOWN(index,len(alpha))

        return alpha[index]
    else:
        return char


def setIndexUP(i,alphabetSize):
    index = i
    if index >= alphabetSize: index = alphabetSize - index
    if index < 0: index =  index * -1
    return index

def setIndexDOWN(i,alphabetSize):
    index = -i
    index = alphabetSize - index
    return index


if __name__ == '__main__':
   test = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin rhoncus laoreet erat, sed lobortis nibh venenatis sit amet. Nullam quis."
   # test = "venenatis"
   encrypted =  CesarCrypt(test,100)
   unEncrypted = CesarUnCrypt(encrypted,100)

   assert not getDiff(unEncrypted, test.lower())

