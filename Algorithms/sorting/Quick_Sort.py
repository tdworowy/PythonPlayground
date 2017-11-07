import sys
from random import randint

sys.setrecursionlimit(10000)


def quick_sort(list):
    if not list: return []
    ran = randint(0, len(list) - 1)
    pivot = list[ran]

    piwots = [x for x in list if x == pivot]
    list_smaller = [x for x in list if x < pivot]
    list_bigger = [x for x in list if x > pivot]

    return quick_sort(list_smaller) + piwots + quick_sort(list_bigger)


if __name__ == '__main__':
    list = [randint(0, 1000) for x in range(10000)]
    sortedList = quick_sort(list)
    print(sortedList)

    list.sort()
    print(list)
    assert sortedList == list
