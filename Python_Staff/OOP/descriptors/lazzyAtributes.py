class InitOnAccess:
    def __init__(self,klass,*args,**kwargs):
        self.klass = klass
        self.args = args
        self.kwargs = kwargs
        self._initialized = None

    def __get__(self, instance, owner):
        if self._initialized is None:
            print("Initialization")
            self._initialized = self.klass(*self.args,**self.kwargs)
        else:
            print("Attribute was already initialized")
        return self._initialized


if __name__ =='__main__':
    class MyClass:
        lazily_initilized = InitOnAccess(list,'Argument')

    m  = MyClass()
    print(m.lazily_initilized)
    print(m.lazily_initilized)