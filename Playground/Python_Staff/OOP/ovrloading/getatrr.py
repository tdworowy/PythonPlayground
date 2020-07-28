class Empty:
    def __getattr__(self, item):
        if item == 'age':
            return "Age is: 40"
        else:
            raise ArithmeticError(item)


class Test:
    def __getattr__(self, item):
        return "Test"


if __name__ == '__main__':
    x = Empty()
    print(x.age)
    x.name = "Test"
    x.age = 20
    print(x.name)
    print(x.age)

    y = Test()
    print(y.wothever)
