from threading import  RLock
loc = RLock()

def synchronized(function):
    def _synchronized(*args,**kw):
        loc.acquire()
        print(loc)
        try:
            return function(*args,**kw)
        finally:
            loc.release()
            print(loc)
    return _synchronized

@synchronized
def thread_safe():
    pass

@synchronized
def thread_safe2():
    pass

thread_safe()
thread_safe2()