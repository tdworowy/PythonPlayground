class newprops:

    def __init__(self):
        self._age =40

    def getage(self):
        return self._age

    def setage(self,value):
        print("Set age: ",value)
        self._age= value

    age = property(getage,setage,None,None)

x = newprops()
print(x.age)
x.age = 2
print(x.age)