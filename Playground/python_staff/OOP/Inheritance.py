def display1():
    print("from c1")


class C1:
    pass


class C2(C1):
    def display2(self):
        print("from c2")


if __name__ == "__main__":
    test = C2()
    display1()
    test.display2()
