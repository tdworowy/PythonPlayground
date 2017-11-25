import sys
from random import randint

sys.setrecursionlimit(10000)


def quick_sort(list_):
    if not list_: return []
    ran = randint(0, len(list_) - 1)
    pivot = list_[ran]

    pivots = [x for x in list_ if x == pivot]
    list_smaller = [x for x in list_ if x < pivot]
    list_bigger = [x for x in list_ if x > pivot]

    return quick_sort(list_smaller) + pivots + quick_sort(list_bigger)


if __name__ == '__main__':
    list_sort = [randint(0, 1000) for x in range(10000)]
    sortedList = quick_sort(list_sort)
    print(sortedList)

    list_sort.sort()
    print(list_sort)
    assert sortedList == list_sort
