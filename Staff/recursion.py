def mysum(L):
    print(L)
    try:
        if not L:
            return 0
        else:
            return L[0] + mysum(L[1:])
    except RecursionError  as re:
        print(re)
        return 0

def mysum2(L):
    try:
        first , *rest = L
        print(L)
        return first if not rest else first + mysum2(rest)
    except RecursionError  as re:
        print(re)
        return 0
    except MemoryError  as re:
        print(re)
        return 0

def sumTree(L):
    tot = 0
    for x in L:
        if not isinstance(x,list):
            tot +=x
        else:
            tot += sumTree(x)
    print(tot)
    return tot

#print(mysum([10, 10, 1, 2, 3, 50, 1]))

l = list(range(1, 999999, 1))
l2 = list(range(1, 99, 1))


#mysum(l)
#print(mysum2(l))

L = [1,[2,[3,[4,5,5],6,8],2],5]
print(sumTree(L))
