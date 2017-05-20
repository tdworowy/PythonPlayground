class empty:
    def __getattr__(self, item):
        if item =='age':
            return "Age is: 40"
        else:
            raise ArithmeticError(item)
class dupa:
    def __getattr__(self, item):
            return "dupa"

x = empty()
print(x.age)
x.name = "Test"
x.age = 20
print(x.name)
print(x.age)


y = dupa()
print(y.wothever)