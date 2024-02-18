class SuperMeta(type):
    def __call__(cls, classname, supers, classdic):
        print("in SuperMeta.call: ", classname, supers, classdic, sep='\n')
        return type.__call__(cls, classname, supers, classdic)


class SubMeta(type,metaclass=SuperMeta):
    def __new__(cls,classname,supers,classdic):
        print("in SubMeta.new: ",classname,supers,classdic,sep='\n')
        return type.__new__(cls,classname,supers,classdic)


    def __init__(self,classname,supers,classdic):
        print("in SubMeta.init: ", classname, supers, classdic, sep='\n')
        print("...... Object initialized. Class:",list(self.__dict__.keys()))


class Eggs:
    pass
if __name__ == '__main__':
    print("Create class")
    class Spam(Eggs,metaclass=SubMeta):
        data = 1
        def meth(self,arg):
            pass

    print("Add instance")
    X =Spam()
    print("Data: ",X.data)