def Tracer(aClass):
    class Wrapper:
        def __init__(self,*args,**kwargs):
            self.fetches = 0
            self.wrapped = aClass(*args,**kwargs)
        def __getattr__(self, item):
            print("Trace: %s" % item)
            self.fetches +=1
            return getattr(self.wrapped,item)
    return Wrapper



if __name__ == '__main__':
    @Tracer
    class spam:
        def display(self):
            print('SPAM')

x = spam()
y = spam()
x.display()
x.display()
y.display()
x.test = 'Test'
print(x.test)
print(x.fetches)
print(y.fetches)