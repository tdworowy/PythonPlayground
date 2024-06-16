def eggsFunc(obj):
    return obj.value * 4


def hamFunc(obj, value):
    return value + "Ham"


class Extender(type):
    def __new__(self, classname, supers, classdic):
        classdic["eggs"] = eggsFunc
        classdic["ham"] = hamFunc
        return type.__new__(self, classname, supers, classdic)


class Client1(metaclass=Extender):
    def __init__(self, value):
        self.value = value

    def spam(self):
        return self.value * 2


class Client2(metaclass=Extender):
    value = "ni?"


if __name__ == "__main__":
    X = Client1("NI!")
    print(X.spam())
    print(X.eggs())
    print(X.ham("Bacon"))

    X2 = Client2()
    print(X2.eggs())
    print(X2.ham("Bacon"))
