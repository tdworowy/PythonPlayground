class PrivateExc(Exception): pass


class Privacy:
    def __setattr__(self, key, value):
        if key in self.privates:
            raise PrivateExc(key, self)
        else:
            self.__dict__[key] = value


class Privates1(Privacy):
    privates = ['age']


class Privates2(Privacy):
    privates = ['name', 'pay']

    def __init__(self):
        self.__dict__['name'] = "Homer"


if __name__ == "__main__":
    x = Privates1()
    y = Privates2()

    x.name = "Test"
    y.pay = 20

    y.age = 30
