class Tracer:
    def __init__(self,func):
        self.calls = 0
        self.func = func

    def __call__(self, *args):
        self.calls +=1
        print("Call %s to %s" % (self.calls, self.func.__name__))
        self.func(*args)


@Tracer
def spam(a,b,c):
    print(a,b,c)

spam(1,2,3)
spam('a','b','c')