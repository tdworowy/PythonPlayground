def MetaFunc(classname,supers,classdict):
    print("In MetaFunc: ",classname,supers,classdict,sep='\n')
    return type(classname,supers,classdict)


class Eggs:
    pass
if __name__ == '__main__':
    print("Create class")
    class Spam(Eggs,metaclass=MetaFunc):
        data = 1
        def meth(self,arg):
            pass

    print("Add instance")
    X =Spam()
    print("Data: ",X.data)