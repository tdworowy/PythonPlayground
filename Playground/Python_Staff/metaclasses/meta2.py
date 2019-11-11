class Meta(type):
    def __new__(cls,classname,supers,classdic):
        print("in Meta.new: ",classname,supers,classdic,sep='\n')
        return type.__new__(cls,classname,supers,classdic)


    def __init__(self,classname,supers,classdic):
        print("in Meta.init: ", classname, supers, classdic, sep='\n')
        print("...... Object initialized. Class:",list(self.__dict__.keys()))


class Eggs:
    pass
if __name__ == '__main__':
    print("Create class")
    class Spam(Eggs,metaclass=Meta):
        data = 1
        def meth(self,arg):
            pass

    print("Add instance")
    X =Spam()
    print("Data: ",X.data)