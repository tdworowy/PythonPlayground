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
        partList1 = self.sort(list[:mid])
        partList2 = self.sort(list[mid:])
        i = 0
        j = 0
        while i < len(partList1) and j < len(partList2):
            if partList1[i] > partList2[j]:
                result.append(partList2[j])
                j+=1
            else:
                result.append(partList1[i])
                i+=1
        result.extend(partList1[i:])
        result.extend(partList2[j:])
        return result


if __name__ == '__main__':

    list = [randint(0,10000) for x in range(1000)]
    ms = mergesort()
    sortedList= ms.sort(list)
    print(sortedList)

    list.sort()
    print(list)
    assert sortedList == list