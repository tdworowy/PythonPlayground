class Base0:
    pass


class Base1(Base0):
    pass


class Base2(Base0):
    pass


class First(Base1, Base2):
    pass


class Second(First):
    pass


class Third(Second):
    pass


if __name__ == "__main__":
    print(Third.__mro__)
    print(Third.mro())
