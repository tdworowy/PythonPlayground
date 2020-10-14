import sys
from random import randint

from Playground.my_utils.staff.timer3 import timer3

sys.setrecursionlimit(10000)


@timer3
def merge_sort(list_: list) -> list:
    result = []
    if len(list_) < 2:
        return list_
    mid = int(len(list_) / 2)
    part_list1 = merge_sort(list_[:mid])
    part_list2 = merge_sort(list_[mid:])
    i = 0
    j = 0
    while i < len(part_list1) and j < len(part_list2):
        if part_list1[i] > part_list2[j]:
            result.append(part_list2[j])
            j += 1
        else:
            result.append(part_list1[i])
            i += 1
    result.extend(part_list1[i:])
    result.extend(part_list2[j:])
    return result


if __name__ == '__main__':
    list_sort = [randint(0, 10000) for x in range(10000)]
    sorted_list = merge_sort(list_sort[:])

    list_sort.sort()
    assert sorted_list == list_sort
