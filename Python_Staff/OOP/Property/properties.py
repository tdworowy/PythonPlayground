class Person:
    def __init__(self,name):
        self._name = name

    def getName(self):
        print("Get...")
        return self._name

    def setName(self,name):
        print("Set...")
        self._name = name

    def delName(self):
        print("Delete...")
        del self._name

    name = property(getName,setName,delName,"DOCUMENTATION: Property name documentation")


homer  = Person("Homer Simpson")
print(homer.name)
homer.name = "Homer2"
print(homer.name)
del homer.name
try:
    print(homer.name)
except Exception as ex :
   print(ex)


print(Person.name.__doc__)