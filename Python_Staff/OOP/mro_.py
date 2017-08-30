


class base0:
        pass
class base1(base0):
        pass
class base2(base0):
        pass
class First(base1,base2):
        pass
class Second(First):
        pass
class Third(Second):
        pass


print(Third.__mro__)
print(Third.mro())