traceMy = False
def trace(*args):
    if traceMy : print('['+' '.join(map(str,args))+']')

def accesControl(failIF):
    def onDecorator(aClass):
        class onInstance:
            def __init__(self,*args,**kwargs):
                self.__wrapped = aClass(*args,**kwargs)
            def __getattr__(self, attr):
                trace('Get: ',attr)
                if failIF(attr):
                    raise  TypeError("Attribute is private: "+attr)
                else:
                    return getattr(self.wrapped,attr)

            def __setattr__(self, attr, value):
                trace("SET: ",attr,value)
                if attr =='wrapped':
                    self.__dict__[attr] = value
                elif failIF(attr):
                    raise TypeError("Attribute is private: "+attr)
                else:
                    setattr(self.wrapped,attr,value)
        return onInstance
    return onDecorator

def Private(*attributes):
    return accesControl(failIF=lambda attr: attr in attributes)

def Public(*attributes):
    return accesControl(failIF=lambda attr: attr not in attributes)

if __name__ == '__main__':



    traceMy = True

    @Private('data','size')
    class Doubler:
        def __init__(self,label,start):
            self.label = label
            self.data = start
        def size(self):
            return len(self.data)
        def double(self):
            for i in range(self.size()):
                self.data[i] = self.data[i] *2
        def disply(self):
            print('%s => %s' % (self.label,self.data))

    x = Doubler('X: ',[1,2,3,4])

    x.disply()
    x.double()
    x.disply()

    try:
        print(x.size())
    except TypeError as e:
        print(e)
    try:
       print(x.data)
    except TypeError as e:
        print(e)
    try:
        x.size = lambda S:0
    except TypeError as e:
        print(e)
    try:
        x.data = [1,1,1]
    except TypeError as e:
        print(e)