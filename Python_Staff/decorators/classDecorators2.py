def decorator(cls):
    class wrapped:
        def __init__(self,*args):
            self.wrapped = cls(*args)
        def __getattr__(self, item):
            print("Wrapped!!")
            return getattr(self.wrapped,item)

    return wrapped


@decorator
class c:
    def __init__(self,x,y):
        self.atr = 'spam'


x = c(6,7)
print(x)
print(x.atr)
print(dir(x))