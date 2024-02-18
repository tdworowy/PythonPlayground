import sys
from random import randint

from Playground.my_utils.staff.timer3 import timer3

sys.setrecursionlimit(10000)


@timer3
def shell_sort(list_: list) -> list:
    distance = len(list_) // 2
    list_len = len(list_)

    while distance > 0:

        for i in range(distance, list_len):
            temp = list_[i]
            j = i
            while j >= distance and list_[j - distance] > temp:
                list_[j] = list_[j - distance]
                j = j - distance
            list_[j] = temp

        distance = distance // 2

    return list_


if __name__ == '__main__':
    list_ = [randint(0, 10000) for x in range(100000)]
    sorted_list = shell_sort(list_[:])

    list_.sort()
    assert list_ == sorted_list
