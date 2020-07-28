registry = {}


def register(obj):
    registry[obj.__name__] = obj
    return obj


if __name__ == '__main__':
    @register
    def spam(x):
        return x ** 2


    @register
    def ham(x):
        return x ** 3


    print("Manual Call")
    print(spam(2))
    print(ham(3))

    print("Calls from registry")

    for name in registry:
        print(name, '=>', registry[name](4))
