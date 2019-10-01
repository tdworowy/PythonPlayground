import time

reps = 1000
repslist = range(reps)


def timer(func, *params, **kargs):
    start = time.clock()
    for i in repslist:
        ret = func(*params, **kargs)
    elapsed = time.clock() - start
    return elapsed, ret



