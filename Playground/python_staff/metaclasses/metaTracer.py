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

    def print_name(self):
        print(self.name)

    def set_name(self, name):
        self.name = name

if __name__ == '__main__':
    x = Person("Test")
    x.print_name()
    x.set_name("Test2")
    x.print_name()