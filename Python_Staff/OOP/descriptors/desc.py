class Descriptor:
    "Documantation abc 123"
    def __get__(self, instance, owner):
        print(self,instance,owner,sep='\n')

    def __set__(self, instance, value):
        print(self, instance, value,sep='\n')



class Subject:
    attr = Descriptor()

x = Subject()
x.attr
x.attr = "Test"
