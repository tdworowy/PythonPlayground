import sys

from Staff.myUtils import myTimer2
from Staff.myUtils import mytimer
reps = 10000
replist = range(reps)

def forLoop():
    res= []
    for x in replist:
        res.append(abs(x))
    return res

def listComp():
    return [abs(x) for x in replist]

def mapCall():
    return list(map(abs,replist))

def genExpr():
    return list(abs(x)for x in replist)

def genFunction():
    def gen():
        for x in replist:
            yield  abs(x)
    return list(gen())


def forLoop2():
    res= []
    for x in replist:
        res.append(x+ 10)
    return res

def listComp2():
    return [x+10 for x in replist]

def mapCall2():
    return list(map( (lambda  x : x+10),replist))

def genExpr2():
    return list(x+10for x in replist)

def genFunction2():
    def gen():
        for x in replist:
            yield  x + 10
    return list(gen())


print(sys.version)
for test in (forLoop,listComp,mapCall,genExpr,genFunction):
    elapsed,result = mytimer.timer(test)
    print('-' * 33)
    print('%-9s: %.5f =>[%s...%s]' % (test.__name__,elapsed,result[0],result[-1]))

print(sys.version)
for test in (forLoop2,listComp2,mapCall2,genExpr2,genFunction2):
    elapsed,result = mytimer.timer(test)
    print('-' * 33)
    print('%-9s: %.5f =>[%s...%s]' % (test.__name__,elapsed,result[0],result[-1]))


print(sys.version)
for tester in(myTimer2.timer,myTimer2.best()):
    print(('<%s>' % tester.__name__))
    for test in (forLoop,listComp,mapCall,genExpr,genFunction):
        elapsed,result = tester(test)
        print('-' * 33)
        print('%-9s: %.5f =>[%s...%s]' % (test.__name__,elapsed,result[0],result[-1]))

print(sys.version)
for tester in(myTimer2.timer,myTimer2.best()):
    print(('<%s>' % tester.__name__))
    for test in (forLoop2,listComp2,mapCall2,genExpr2,genFunction2):
        elapsed,result = tester(test)
        print('-' * 33)
        print('%-9s: %.5f =>[%s...%s]' % (test.__name__,elapsed,result[0],result[-1]))
