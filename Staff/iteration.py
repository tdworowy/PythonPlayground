import functools
import operator
import random
import string

L = [1,2,3,4]
I = iter(L)
print(next(I))
print(next(I))
print(next(I))
print(next(I))


D= {'a':1,'b':2,'c':3}

for key in D:
    print(key ,D[key])

    f2 = open('testFile2.txt', 'r+')
    for _ in range(1, 30):
        print(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(50)), file=f2)
    lines = f2.readlines()
    print(lines)


print(sorted(open("testFile2.txt")))
print(list(enumerate(open("testfile2.txt"))))
print(list(filter(bool,open("testFile2.txt"))))
functools.reduce(operator.add,open("testFile2.txt"))

print(list(open("testFile2.txt")))
tuple((open("testFile2.txt")))

print(sum([1,2,3]))
print(max([1,2,3]))
print(min([1,2,3]))
print(any([1,2,3,"","Spam"]))
print(all([1,2,3,"","Spam"]))


M = map(abs,(-1,0,1))
print(next(M)) #ubywa elementów , same for zip i filter()
print(next(M))
print(next(M))

for x in M: print(x)

R = range(3) #Range obsługuje wielokortne  niezależne iteracje
I1 = iter(R)
print(next(I1))
print(next(I1))
I2 = iter(R)
print(next(I2))
print(next(I2))



D = dict(a=1,b=2,c=3)
K = D.keys()
I = iter(K)
print(next(I))
print(next(I))


I = iter(D)
print(next(I))
print(next(I))