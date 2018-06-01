import sys

from MyUtils import myTimer2, mytimer

reps = 10000
replist = range(reps)


def for_loop():
    res = []
    for x in replist:
        res.append(abs(x))
    return res


def list_comp():
    return [abs(x) for x in replist]


def map_call():
    return list(map(abs, replist))


def gen_expr():
    return list(abs(x) for x in replist)


def gen_function():
    def gen():
        for x in replist:
            yield abs(x)

    return list(gen())


def for_loop2():
    res = []
    for x in replist:
        res.append(x + 10)
    return res


def list__comp2():
    return [x + 10 for x in replist]


def map_call2():
    return list(map((lambda x: x + 10), replist))


def gen_expr2():
    return list(x + 10 for x in replist)


def gen_function2():
    def gen():
        for x in replist:
            yield x + 10

    return list(gen())


print(sys.version)
for test in (for_loop, list_comp, map_call, gen_expr, gen_function):
    elapsed, result = mytimer.timer(test)
    print('-' * 33)
    print('%-9s: %.5f =>[%s...%s]' % (test.__name__, elapsed, result[0], result[-1]))

print(sys.version)
for test in (for_loop2, list__comp2, map_call2, gen_expr2, gen_function2):
    elapsed, result = mytimer.timer(test)
    print('-' * 33)
    print('%-9s: %.5f =>[%s...%s]' % (test.__name__, elapsed, result[0], result[-1]))

print(sys.version)
for tester in (myTimer2.timer, myTimer2.best):
    print(('<%s>' % tester.__name__))
    for test in (for_loop, list_comp, map_call, gen_expr, gen_function):
        elapsed, result = tester(test)
        print('-' * 33)
        print('%-9s: %.5f =>[%s...%s]' % (test.__name__, elapsed, result[0], result[-1]))

print(sys.version)
for tester in (myTimer2.timer, myTimer2.best):
    print(('<%s>' % tester.__name__))
    for test in (for_loop2, list__comp2, map_call2, gen_expr2, gen_function2):
        elapsed, result = tester(test)
        print('-' * 33)
        print('%-9s: %.5f =>[%s...%s]' % (test.__name__, elapsed, result[0], result[-1]))
