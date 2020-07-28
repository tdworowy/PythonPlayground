class C1:
    def __init__(self, x):
        self.__X = x


class C2:
    def __init__(self, x):
        self.__X = x


class C3(C1, C2):
    def __init__(self, x, y):
        C1.__init__(self, x)
        C2.__init__(self, y)


if __name__ == "__main__":
    y = C3(1, 2)
    print(y.__dict__)
