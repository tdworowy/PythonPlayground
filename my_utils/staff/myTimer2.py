import sys
import time

if sys.platform[:3] == 'win':
    time_func = time.clock
else:
    time_func = time.time


def trace(*args): pass


def timer(func, *pargs, **kargs):
    _reps = kargs.pop('_reps', 1000)
    trace(func, pargs, kargs, _reps)
    replist = range(_reps)
    start = time_func()
    for i in replist:
        ret = func(*pargs, **kargs)
    elapsed = time_func() - start
    return elapsed, ret


def best(func, *pargs, **kargs):
    _reps = kargs.pop('_reps', 50)
    best = 2 ** 32
    for i in range(_reps):
        (time, ret) = timer(func, *pargs, _reps=1, **kargs)
        if time < best: best = time
    return best, ret
