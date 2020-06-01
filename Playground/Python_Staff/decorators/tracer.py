class Tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print("Call %s to %s" % (self.calls, self.func.__name__))
        self.func(*args, **kwargs)


# works only for functions


def tracer(func):
    calls = 0

    def onCall(*args, **kwargs):
        nonlocal calls
        calls += 1
        print("Call %s %s" % (calls, func.__name__))
        return func(*args, **kwargs)

    return onCall


# work for functions and methods

class Tracer2:
    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print("Call %s to %s" % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)

    def __get__(self, instance, owner):
        return wrapper(self, instance)


class wrapper:
    def __init__(self, desc, subj):
        self.desc = desc
        self.subj = subj

    def __call__(self, *args, **kwargs):
        return self.desc(self.subj, *args, **kwargs)


# also work for functions and methods


class Tracer3:
    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print("Call %s to %s" % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)

    def __get__(self, instance, owner):
        def wrapper(instance, *args, **kwargs):
            return self(instance, *args, **kwargs)

        return wrapper


if __name__ == "__main__":
    @Tracer
    def spam(a, b, c):
        print(a, b, c)


    spam(1, 2, 3)
    spam('a', 'b', 'c')


    @Tracer2
    def spam(a, b, c):
        print(a, b, c)


    spam(1, 2, 3)
    spam('a', 'b', 'c')


    @Tracer3
    def spam(a, b, c):
        print(a, b, c)


    spam(1, 2, 3)
    spam('a', 'b', 'c')
