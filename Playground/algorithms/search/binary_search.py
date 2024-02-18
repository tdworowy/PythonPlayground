from random import randint

from Playground.my_utils.staff.timer3 import timer3


@timer3
def binary_search(list_: list, item):
    """list_ must be sorted"""
    first = 0
    last = len(list_) - 1

    while first <= last:
        mind_point = (first + last) // 2
        if list_[mind_point] == item:
            return True
        else:
            if item < list_[mind_point]:
                last = mind_point - 1
            else:
                first = mind_point + 1

    return False


if __name__ == '__main__':
    list_ = [randint(0, 10000) for x in range(100000)]
    list_.sort()
    print(binary_search(list_, 500))
