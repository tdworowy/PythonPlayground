#BED
if __name__ == "__main__":

    L = [1,2,4,8,16,32,64]
    x =5
    found = False
    i =0
    while not found and i < len(L):
        if 2 ** x == L[i]:
            found = True
        else: i = i+1

    if found:
        print("found on index",i)
    else:
        print(x, "not Found")


    #GOD

    L = [2 **x for x in range(20)]
    x =5
    x2 = 2 ** x
    if x2 in L : print("Found on index %s" % L.index(x2))
    else: print("Not found")


    #ALSO GOD
    x=5

    L = list(map(lambda x : 2**x, range(20)))
    if (2**x) in L:
        print("Found on index %s" % L.index(x2))
    else: print("Not found")