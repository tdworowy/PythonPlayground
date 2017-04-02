class overloadingClass():
    def __init__(self,value):
        self.data = value
    def __add__(self,other):
        return overloadingClass(self.data + other)
    def __str__(self):
        return '["Data: %s "]' % self.data
    def mul(self,other):
        self.data *=other

    def display(self):
        print("Value: %s" %self.data)

a = overloadingClass('abc')
a.display()
print(a)

b = a + 'xyz'
b.display()
print(b)

a.mul(3)
a.display()
print(a)

a1= overloadingClass(10)
c= a1 + 1
c.display()
print(c)