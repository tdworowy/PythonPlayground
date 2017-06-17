import string

from myUtils.compareStrings import getDiff


def CesarCrypt(text,index):
    return ''.join([getLetter(char,index,setIndexUP) for char in text.lower()])

def CesarUnCrypt(text,index):
    return ''.join([getLetter(char,-index,setIndexDOWN) for char in text.lower()])


def getLetter(char,jump,setIndexFunction):
    if char.isalpha():
        alpha = string.ascii_lowercase
        index = alpha.index(char) + jump
        while index not in range(0,len(alpha)):
            index =setIndexFunction(index,len(alpha))
        return alpha[index]
    else:
        return char


def setIndexUP(i,alphabetSize):
    index = i
    if index >= alphabetSize: index = alphabetSize - index
    if index < 0: index = index * -1
    return index

def setIndexDOWN(i,alphabetSize):
    index = -i
    index = alphabetSize - index
    return index


if __name__ == '__main__':
   test = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin rhoncus laoreet erat, sed lobortis nibh venenatis sit amet. Nullam quis."
   encrypted =  CesarCrypt(test,100)
   unEncrypted = CesarUnCrypt(encrypted,100)

   print("ENCRYPTED: ", encrypted)
   print("ORYGINAL: ", test.lower())
   print("UNENCRYPTED: ", unEncrypted)
   print(getDiff(unEncrypted, test.lower()))

   assert not getDiff(unEncrypted, test.lower())

