from types import FunctionType


def tracer(func):
    calls = 0
    def onCall(*args,**kwargs):
        nonlocal calls
        calls +=1
        print("Call %s %s" % (calls,func.__name__))
        return func(*args,**kwargs)
    return onCall


class MetaTrace(type):
    def __new__(cls, classname,supers,classdic):
        for attr,attrval in classdic.items():
            if type(attrval) is FunctionType:
                classdic[attr] = tracer(attrval)

        return type.__new__(cls, classname, supers, classdic)


class Person(metaclass=MetaTrace):
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