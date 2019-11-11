x = [2, 1, 5, 3, 4]

def minimum_bribes(q):
    bribes =0
    started_q = sorted(q)
    if q == started_q:
        print(0)
        return 0
    for i,ele in enumerate(q):
        if ele - (i+1) > 2:
            print("Too chaotic")
            return 0
        for j in range(ele - 1, i):
            if q[j] > ele:
                bribes += 1

def minimum_bribes(q):
    bribes = 0
    list_sort = q[:]
    result = []
    i = 1
    while len(result) < len(q):
        for j in range(len(list_sort) - 1):
            if q[j] - (j + 1) > 2:
                print("Too chaotic")
                return 0
            if list_sort[j] > list_sort[i]:
                list_sort[j], list_sort[i] = list_sort[i], list_sort[j]
                bribes +=1
            i += 1
        i = 1
        result.append(list_sort[-1])
        list_sort = list_sort[:-1]
    print(bribes)

def minimum_bribes(q):
    bribes = 0
    print(list(range(len(q) - 1, -1, -1)))
    for i in range(len(q)-1,-1,-1):
        if q[i] - (i + 1) > 2:
            print('Too chaotic')
            return
        for j in range(max(0, q[i] - 2),i):
            if q[j] > q[i]:
                bribes+=1

    print(bribes)

if __name__ == "__main__":
    minimum_bribes(x)