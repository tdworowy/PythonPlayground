if __name__ == "__main__":

    def f(a):
        a = 99

    b = 88
    f(b)
    print(b)

    def changer(a, b):
        a = 2
        b[0] = "spam"

    X = 1
    L = [1, 2]

    print(X, L)

    changer(X, L)
    print(X, L)

    L = [1, 2]
    changer(X, L[:])
    print(X, L)

    def f(a, b, c):
        print(a, b, c)

    f(1, 2, 3)
    f(c=1, b=2, a=3)

    def f(a, b=2, c=3):
        print(a, b, c)

    f(1)

    def func(spam, eggs, toast=0, ham=0):
        print(spam, eggs, toast, ham)

    func(1, 2)
    func(1, ham=1, eggs=0)
    func(toast=1, eggs=2, spam=3)
    func(1, 2, 3, 4)

    def f(*args):
        print(args)

    f(0)
    f(1, 2, 3, 4, 5)
    f("spam", 1, "dupa")

    def f(**args):
        print(args)

    f()
    f(a=1, b=2)
    f(x="spam", y="dupa")

    def func(a, *pargs, **kargs):
        print(a, pargs, kargs)

    func(1, 2, 3, x=1, y=2)
