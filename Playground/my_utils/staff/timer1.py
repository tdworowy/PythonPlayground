import time

reps = 1000
reps_list = range(reps)


def timer(func, *params, **kargs):
    start = time.clock()
    for i in reps_list:
        ret = func(*params, **kargs)
    elapsed = time.clock() - start
    return elapsed, ret



