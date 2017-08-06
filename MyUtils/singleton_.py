instances = {}
def getInstance(aClass,*args):
    if aClass not in instances:
        instances[aClass] = aClass(*args)
    return instances[aClass]


def singleton(aClass):
    def onCall(*args):
        return getInstance(aClass,*args)
    return onCall



def singleton2(aClass):
    instances = None
    def onCall(*args):
        nonlocal  instances
        if instances == None:
            instances = aClass(*args)
        return instances
    return onCall

#best version IMHO
class Singleton3:
    def __init__(self,aClaas):
        self.aClass = aClaas
        self.instances = None

    def __call__(self, *args, **kwargs):
        if self.instances == None:
            self.instances = self.aClass(*args,**kwargs)
        return self.instances


if __name__ == '__main__':

   @singleton
   class X:
       def __init__(self,value):
            self.value = value

       def getvalue(self):
            print(self.value)

#will create only one instance
   x = X('z')
   x.getvalue()
   y = X('a')
   y.getvalue()