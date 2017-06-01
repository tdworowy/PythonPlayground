import sys
from random import randint


class quicksort:
    def __init__(self):
         sys.setrecursionlimit(10000)

    def sort(self,list):
        if not list: return []
        ran =  randint(0,len(list)-1)
        pivot =list[ran]

        piwots = [x for x in list if x == pivot]
        listSmaller = [x for x in list if x < pivot]
        listBigger = [x for x in list if x > pivot]

        return self.sort(listSmaller)+piwots +self.sort(listBigger)




if __name__ == '__main__':

    list = [randint(0,1000) for x in range(10000) ]
    qs = quicksort()
    sortedList= qs.sort(list)
    print(sortedList)

    list.sort()
    print(list)
    assert sortedList == list