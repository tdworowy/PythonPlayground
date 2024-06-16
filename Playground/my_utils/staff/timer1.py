import time

reps = 1000
reps_list = range(reps)


def timer(func, *params, **kargs):
    start = time.process_time()
    for i in reps_list:
        ret = func(*params, **kargs)
    elapsed = time.process_time() - start
    return elapsed, ret
