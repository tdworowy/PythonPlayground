class Methods:
    def imeth(self, X):
        print(self, X)

    def smeth(X):
        print(X)

    def cmeth(cls, X):
        print(cls, X)

    smeth = staticmethod(smeth)
    cmeth = classmethod(cmeth)  # zawsze przekazuje klase(najniższą w hierarhi)


class Methods2:
    def imeth(self, X):
        print(self, X)

    @staticmethod
    def smeth(X):
        print(X)

    @classmethod
    def cmeth(cls, X):
        print(cls, X)


class Spam:
    numInstances = 0

    def count(cls):
        cls.numInstances += 1

    def __init__(self):
        self.count()

    count = classmethod(count)


class Sub(Spam):
    numInstances = 0

    def __init__(self):
        Spam.__init__(self)


class Other(Spam):
    numInstances = 0


if __name__ == "__main__":
    x = Methods()

    x.smeth("Test1")
    x.cmeth("Test2")

    Methods.smeth("Test3")
    Methods.cmeth("Test4")

    x = Spam()
    y1, y2 = Sub(), Sub()
    z1, z2, z3 = Other(), Other(), Other()
    print(x.numInstances, y1.numInstances, z1.numInstances)
    print(Spam.numInstances, Sub.numInstances, Other.numInstances)
