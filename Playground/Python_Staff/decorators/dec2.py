def dec1(f):
    def warp(*args, **kwds):
        print("Dec1")
        return f(*args, **kwds)

    return warp


def dec2(f):
    def warp(*args, **kwds):
        print("Dec2")
        return f(*args, **kwds)

    return warp


def dec3(f):
    def warp(*args, **kwds):
        print("Dec3")
        return f(*args, **kwds)

    return warp


@dec1
@dec2
@dec3
def func(x):
    print(x)


if __name__ == "__main__":
    func("TEST")
