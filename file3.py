L = [1,2,3,4]
while L:
    front , L =L[0],L[1:]
    print(front,L)

L = [1, 2, 3, 4]
while L:
        front, *L= L
        print(front, L)