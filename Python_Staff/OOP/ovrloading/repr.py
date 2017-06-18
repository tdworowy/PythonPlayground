class adder():
    def __init__(self,value =0):
        self.data =value
    def __add__(self, other):
        self.data +=other

    def __radd__(self, other):
        self.data += other

class multip():
    def __init__(self,value =0):
        self.data =value
    def __mul__(self,x):
        self.data = self.data *x

    def __rmul__(self, other):
        self.data = self.data * x


class addrepr(adder,multip):
    def __repr__(self):
        return 'addrepr(%s)' % self.data


x = addrepr(2)
y = addrepr(3)
x +1
print(x)
x+2
print(x)
1+ x
print(x)

x*2
print(x)

z = y + x
print("y: ",y)
print("x: ",x)
print("z: ",z)


x = addrepr(2)
y = addrepr(3)

z = x + y
print("y: ",y)
print("x: ",x)
print("z: ",z)