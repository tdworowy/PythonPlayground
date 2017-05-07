def show(f):
    def warp(*args, **kwds):
             print('Run:', f.__name__)
             return f(*args, **kwds)
    return warp



@show
def foo():
    pass

@show
def foo2():
    print("Foo")

foo()
foo2()