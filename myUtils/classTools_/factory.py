def Factory(aclass, *args, **kwargs):
    return aclass(*args,kwargs)




if __name__ == '__main__':
    class Spam:
        def doit(self,message):
            print(message)
    class Person:
        def __init__(self,name,job):
            self.name = name
            self.job = job


    object1 = Factory(Spam)
    object1.doit("Test")
    object2 = Factory(Person,"Archer","Spy")