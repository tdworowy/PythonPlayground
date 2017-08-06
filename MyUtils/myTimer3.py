import time



def timer(label = ' ',trace = True):
    class Timer:
        def __init__(self,func):
            self.func = func
            self.alltime =0
        def __call__(self, *args, **kwargs):
            start = time.clock()
            result = self.func(*args,**kwargs)
            elapsed = time.clock() - start
            self.alltime +=elapsed
            if trace:
                format = '%s %s: %.5f, %.5f'
                values = (label,self.func.__name__,elapsed,self.alltime)
                print(format % values)
            return result
    return Timer
#dosen't work on methods


def timer2(label = ' ',trace = True):
    def onDecorator(func):
        def onCall(*args, **kwargs):
            start = time.clock()
            result =func(*args,**kwargs)
            elapsed = time.clock() - start
            onCall.alltime +=elapsed
            if trace:
                format = '%s %s: %.5f, %.5f'
                values = (label,func.__name__,elapsed,onCall.alltime)
                print(format % values)
            return result
        onCall.alltime += 0
        return onCall
    return onDecorator




@timer("==>")
def listcomp(x):
    return [x * 2 for x in range(x)]


if __name__ == "__main__":
    listcomp(10000000)