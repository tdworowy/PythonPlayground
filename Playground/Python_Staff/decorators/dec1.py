def show(f):
    def warp(*args, **kwds):
        print('Run:', f.__name__)
        return f(*args, **kwds)

    return warp


def test(f):
    def warp():
        print("test")

    return warp


@show
def foo():
    pass


@show
def foo2():
    print("Foo2")


@test
def foo3():
    print("Foo3")


if __name__ == "__main__":
    foo()
    foo2()
    foo3()
