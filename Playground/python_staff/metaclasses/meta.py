class Meta(type):
    def __new__(metaclass, class_name,suppesrs,classdic):
        print("In Meta :",class_name,suppesrs,classdic,sep='\n')
        return type.__new__(metaclass, class_name,suppesrs,classdic)


class Eggs:
    pass


class Spam(Eggs,metaclass=Meta):
    data =1
    def meth(self,arg):
        print(arg)
if __name__ == '__main__':
    print('_'*15)
    print("Create instance")
    X = Spam()
    X.meth("Test")