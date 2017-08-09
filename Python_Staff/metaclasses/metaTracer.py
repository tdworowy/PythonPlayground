def Tracer(classname,supers,classdic):
    aClass = type(classname,supers,classdic)
    class Wrapper:
        def __init__(self,*args,**kwargs):
            self.wrapped = aClass(*args,**kwargs)
        def __getattr__(self, item):
            print("Trace:",item)
            return getattr(self.wrapped,item)

    return Wrapper


class Person(metaclass=Tracer):
    def __init__(self,name):
        self.name = name

    def printName(self):
        print(self.name)

    def setName(self,name):
        self.name = name


x = Person("Test")
x.printName()
x.setName("Test2")
x.printName()