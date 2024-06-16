class Wrapper:
    def __init__(self, object):
        self.wrapped = object

    def __getattr__(self, attrname):
        print("trace: ", attrname)
        return getattr(self.wrapped, attrname)


if __name__ == "__main__":
    x = Wrapper([1, 2, 3, 4])
    x.append(5)
    print(x.wrapped)

    y = Wrapper({"a": 1, "b": 2})
    print(y.keys())
    print(y.wrapped)
