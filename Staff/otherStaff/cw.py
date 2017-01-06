import math

test5 = [x **2 for x in [2,4,9,16,25]]
print(test5)

test6 = map((lambda x : x **2),[2,4,9,16,25] )
print(list(test6))
list_ =[2,4,9,16,25]
test7 = map((math.pow),list_,[2 for i in range(len(list_))] )
print(list(test7))

def func(list):
    newList = []
    for x in list:
        newList.append(x **2)
    return newList

print(func([2,4,9,16,25]))