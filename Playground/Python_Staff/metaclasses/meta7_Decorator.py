
def eggsFunc(obj):
    return obj.value * 4

def hamFunc(obj,value):
    return value + "Ham"


def Extedner(aClass):
    aClass.eggs = eggsFunc
    aClass.ham = hamFunc
    return aClass



@Extedner
class Client1:
    def __init__(self,value):
        self.value = value
    def spam(self):
        return self.value * 2

@Extedner
class Client2:
     value = "ni?"
if __name__ == '__main__':
    X = Client1("NI!")
    print(X.spam())
    print(X.eggs())
    print(X.ham("Bacon"))

    X2 = Client2()
    print(X2.eggs())
    print(X2.ham("Bacon"))