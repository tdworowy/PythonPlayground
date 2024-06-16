traceMy = False


def trace(*args):
    if traceMy:
        print("[" + " ".join(map(str, args)) + "]")


def access_control(fail_if):
    def on_decorator(a_class):
        class OnInstance:
            def __init__(self, *args, **kwargs):
                self.__wrapped = a_class(*args, **kwargs)

            def __getattr__(self, attr):
                trace("Get: ", attr)
                if fail_if(attr):
                    raise TypeError("Attribute is private: " + attr)
                else:
                    return getattr(self.wrapped, attr)

            def __setattr__(self, attr, value):
                trace("SET: ", attr, value)
                if attr == "wrapped":
                    self.__dict__[attr] = value
                elif fail_if(attr):
                    raise TypeError("Attribute is private: " + attr)
                else:
                    setattr(self.wrapped, attr, value)

        return OnInstance

    return on_decorator


def Private(*attributes):
    return access_control(fail_if=lambda attr: attr in attributes)


def Public(*attributes):
    return access_control(fail_if=lambda attr: attr not in attributes)


if __name__ == "__main__":

    traceMy = True

    @Private("data", "size")
    class Doubler:
        def __init__(self, label, start):
            self.label = label
            self.data = start

        def size(self):
            return len(self.data)

        def double(self):
            for i in range(self.size()):
                self.data[i] = self.data[i] * 2

        def disply(self):
            print("%s => %s" % (self.label, self.data))

    x = Doubler("X: ", [1, 2, 3, 4])

    x.disply()
    x.double()
    x.disply()

    try:
        print(x.size())
    except TypeError as e:
        print(e)
    try:
        print(x.data)
    except TypeError as e:
        print(e)
    try:
        x.size = lambda S: 0
    except TypeError as e:
        print(e)
    try:
        x.data = [1, 1, 1]
    except TypeError as e:
        print(e)
