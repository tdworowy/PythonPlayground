def show(f):
    def warp(*args, **kwds):
             print('Run:', f.__name__)
             return f(*args, **kwds)
    return warp

def dupa(f):
    def warp():
        print("Dupa")
    return warp


@show
def foo():
    pass

@show
def foo2():
    print("Foo2")

@dupa
def foo3():
    print("Foo3")


foo()
foo2()
foo3()