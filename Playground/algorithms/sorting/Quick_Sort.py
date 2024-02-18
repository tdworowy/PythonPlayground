import sys
from random import randint

from Playground.my_utils.staff.timer3 import timer3

sys.setrecursionlimit(10000)


@timer3
def quick_sort(list_: list) -> list:
    if not list_: return []
    ran = randint(0, len(list_) - 1)
    pivot = list_[ran]

    pivots = [x for x in list_ if x == pivot]
    list_smaller = [x for x in list_ if x < pivot]
    list_bigger = [x for x in list_ if x > pivot]

    return quick_sort(list_smaller) + pivots + quick_sort(list_bigger)


if __name__ == '__main__':
    list_sort = [randint(0, 10000) for x in range(10000)]
    sorted_list = quick_sort(list_sort[:])

    list_sort.sort()
    assert sorted_list == list_sort
