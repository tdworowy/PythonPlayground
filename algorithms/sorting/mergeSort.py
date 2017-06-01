import sys
from random import randint


class mergesort:
    def __init__(self):
        sys.setrecursionlimit(10000)

    def sort(self,list):
        result = []
        if len(list) < 2:
            return list
        mid = int(len(list)/2)
        newList1 = self.sort(list[:mid])
        newList2 = self.sort(list[mid:])
        i = 0
        j = 0
        while i < len(newList1) and j < len(newList2):
            if newList1[i] > newList2[j]:
                result.append(newList2[j])
                j+=1
            else:
                result.append(newList1[i])
                i+=1
        result.extend(newList1[i:])
        result.extend(newList2[j:])
        return result


if __name__ == '__main__':

    list = [randint(0,10000) for x in range(1000)]
    ms = mergesort()
    sortedList= ms.sort(list)
    print(sortedList)

    list.sort()
    print(list)
    assert sortedList == list