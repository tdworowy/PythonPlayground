class Calle:
    def __call__(self, *args, **kwargs):
        print("Call: ",args,kwargs)


class Prod:
    def __init__(self,value):
        self.value = value
    def __call__(self, other):
        return self.value * other

C = Calle()
C(1,2,3)
C(['a','b','c'])
C("Spam")
C({'a':1})


x = Prod(2)
print(x(3))
print(x.value)
print(x(4))
print(x.value)